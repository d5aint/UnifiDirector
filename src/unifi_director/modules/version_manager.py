"""UniFi Network Application version checker."""

__version__ = "1.0.0"

import json
import logging

import httpx

from ..api_client.api.application_info import get_info
from ..api_client.client import Client
from ..api_client.errors import UnexpectedStatus
from ..registry import REGISTRY

logger = logging.getLogger(__name__)

# WHY: This must be updated whenever the API client is regenerated from a new spec.
# It drives the "Update available" status — comparing this against the latest spec
# on GitHub tells the operator whether a client regeneration is warranted.
SPEC_BUILT_ON = "10.5.54"

_GITHUB_URL = "https://api.github.com/repos/beezly/unifi-apis/contents/unifi-network"


def _parse_ver(v: str) -> tuple[int, ...]:
    try:
        return tuple(int(x) for x in v.strip().split("."))
    except (ValueError, AttributeError):
        return (0,)


def _ver_str(v: str) -> str:
    return f"v{v}"


def get_controller_version(client: Client) -> str | None:
    try:
        response = get_info.sync(client=client)
        if response:
            return getattr(response, "application_version", None)
        logger.error("Controller returned empty response for application info.")
        return None
    except UnexpectedStatus as e:
        if e.status_code == 401:
            logger.error("Controller returned 401 — check the API key for the active console profile.")
        elif e.status_code == 403:
            logger.error("Controller returned 403 — API key lacks permission to read application info.")
        else:
            logger.error(f"Controller returned unexpected status {e.status_code} for application info.")
        return None
    except httpx.HTTPError as e:
        logger.error(f"Network error retrieving controller version: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error retrieving controller version: {e}")
        return None


def fetch_latest_known_version() -> str | None:
    """Return the highest version found in beezly/unifi-apis, or None on failure."""
    try:
        with httpx.Client(timeout=10.0) as http:
            resp = http.get(
                _GITHUB_URL,
                headers={
                    "Accept": "application/vnd.github.v3+json",
                    # WHY: GitHub rate-limits anonymous requests per IP. A User-Agent
                    # identifying the tool distinguishes it from browser traffic.
                    "User-Agent": "unifi-director/2.0",
                },
            )
            resp.raise_for_status()

        versions: list[str] = [
            entry["name"][:-5]
            for entry in resp.json()
            if isinstance(entry, dict) and entry.get("name", "").endswith(".json")
        ]

        if not versions:
            logger.warning("No version files found in GitHub repo.")
            return None

        return max(versions, key=_parse_ver)

    except httpx.TimeoutException:
        logger.warning("Version check timed out (GitHub unreachable).")
        return None
    except httpx.HTTPStatusError as e:
        logger.warning(f"GitHub API returned {e.response.status_code} during version check.")
        return None
    except httpx.HTTPError as e:
        logger.warning(f"Network error during version check: {e}")
        return None
    except Exception as e:
        logger.warning(f"Unexpected error during version check: {e}")
        return None


def run_version_check(client: Client, as_json: bool = False) -> None:
    controller_ver = get_controller_version(client)
    latest_ver = fetch_latest_known_version()

    # Status is determined by comparing the built-in spec against the latest on
    # GitHub — not the controller version. The controller version is informational.
    update_available = None
    if latest_ver:
        sv = _parse_ver(SPEC_BUILT_ON)
        lv = _parse_ver(latest_ver)
        if sv < lv:
            update_available = True
        elif sv > lv:
            update_available = False  # ahead of repo
        else:
            update_available = False  # up to date

    name = REGISTRY.CONSOLE_NAME or "default"
    location = f"{name}  (via api.ui.com)" if REGISTRY.CONSOLE_ID else f"{name}  ({REGISTRY.HOST})"

    if as_json:
        print(json.dumps({
            "controller": name,
            "controller_host": REGISTRY.CONSOLE_ID or REGISTRY.HOST,
            "controller_version": controller_ver,
            "unifi_director_spec": SPEC_BUILT_ON,
            "latest_spec_available": latest_ver,
            "update_available": update_available,
        }, indent=2))
        return

    print(f"  Controller              : {location}")
    print(f"  Controller version      : {_ver_str(controller_ver) if controller_ver else 'Unknown (API error)'}")
    print(f"  unifi-director spec     : {_ver_str(SPEC_BUILT_ON)}")

    if latest_ver:
        print(f"  Latest spec available   : {_ver_str(latest_ver)}  (github.com/beezly/unifi-apis)")
        if update_available is True:
            print("  Status                  : Update available")
        elif _parse_ver(SPEC_BUILT_ON) > _parse_ver(latest_ver):
            print("  Status                  : Ahead of latest known spec")
        else:
            print("  Status                  : Up to date")
    else:
        print("  Latest spec available   : Unavailable (could not reach GitHub)")
