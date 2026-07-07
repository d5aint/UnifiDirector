"""HTTP client factory — single shared instances for local and cloud routes."""

__version__ = "1.0.0"

import logging
import warnings

import httpx

from .api_client.client import Client
from .registry import REGISTRY

request_logger = logging.getLogger("UnifiHTTP")


def _log_request(request: httpx.Request) -> None:
    request_logger.debug(f"Request: {request.method} {request.url}")


def get_shared_client() -> Client:
    """Return a configured Client for the active console (local or cloud proxy).

    WHY: A single shared httpx connection pool is reused across all CLI command
    paths, preventing connection exhaustion on heavily paginated commands like audit.
    """
    if not REGISTRY.VERIFY_SSL:
        # WHY: Local UniFi controllers use self-signed certs; suppress urllib3
        # warnings that would pollute CLI output when SSL verification is disabled.
        warnings.filterwarnings("ignore", message="Unverified HTTPS request")

    if REGISTRY.CONSOLE_ID:
        # WHY: Cloud Proxy route avoids opening firewall ports to the controller;
        # all traffic tunnels through api.ui.com using the console's cloud ID.
        base_url = f"https://api.ui.com/v1/connector/consoles/{REGISTRY.CONSOLE_ID}/proxy/network/integration"
        api_key = REGISTRY.CLOUD_API_KEY
    else:
        base_url = f"https://{REGISTRY.HOST}/proxy/network/integration"
        api_key = REGISTRY.API_KEY

    return Client(
        base_url=base_url,
        headers={"X-API-KEY": api_key, "Accept": "application/json"},
        verify_ssl=REGISTRY.VERIFY_SSL,
        raise_on_unexpected_status=True,
        httpx_args={"event_hooks": {"request": [_log_request]}},
    )


def get_cloud_client() -> httpx.Client:
    """Return a raw httpx Client for the Global UniFi Cloud Site Manager API."""
    return httpx.Client(
        base_url=f"https://{REGISTRY.CLOUD_HOST}",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-API-Key": REGISTRY.CLOUD_API_KEY,
        },
        timeout=10.0,
        event_hooks={"request": [_log_request]},
    )
