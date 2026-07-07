"""UniFi Global Configuration Registry — validated singleton loaded at startup."""

__version__ = "1.0.0"

import json
import logging
import os
import sys
from dataclasses import dataclass
from uuid import UUID


@dataclass
class GlobalRegistry:
    """Validated, read-only global configuration for the current CLI invocation."""
    HOST: str
    API_KEY: str
    CLOUD_HOST: str
    CLOUD_API_KEY: str
    SITE_ID: UUID
    SITE_ID_RAW: str
    CONSOLE_ID: str | None
    CONSOLE_NAME: str | None
    VERIFY_SSL: bool
    DEBUG: bool


def _initialize_registry() -> GlobalRegistry:
    # WHY: Return a no-op registry for --help/-h so argparse can print usage without
    # requiring credentials to be present. All real commands still go through full
    # validation below.
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) == 1:
        _null_uuid = UUID("00000000-0000-0000-0000-000000000000")
        return GlobalRegistry(
            HOST="", API_KEY="", CLOUD_HOST="", CLOUD_API_KEY="",
            SITE_ID=_null_uuid, SITE_ID_RAW="", CONSOLE_ID=None, CONSOLE_NAME=None,
            VERIFY_SSL=False, DEBUG=False,
        )

    cli_debug = "--debug" in sys.argv
    debug_mode = cli_debug or os.getenv("UNIFI_DEBUG", "False").lower() in ("true", "1", "yes")
    # WHY: SSL verification is off by default because local UniFi controllers use
    # self-signed certificates. Opt-in via env var for production deployments.
    verify_ssl = os.getenv("UNIFI_VERIFY_SSL", "False").lower() in ("true", "1", "yes")

    log_level = logging.DEBUG if debug_mode else logging.INFO
    logging.basicConfig(level=log_level, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    if not debug_mode:
        # WHY: httpx and httpcore are very chatty at INFO; suppress to WARNING so
        # normal CLI output stays readable without --debug.
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("httpcore").setLevel(logging.WARNING)

    logger = logging.getLogger("UnifiRegistry")

    console_name: str | None = None
    for i, arg in enumerate(sys.argv):
        if arg in ("-c", "--console") and i + 1 < len(sys.argv):
            console_name = sys.argv[i + 1]
            break
        elif arg.startswith("--console="):
            console_name = arg.split("=", 1)[1]
            break

    # WHY: inventory.json is resolved relative to CWD so the tool can be invoked
    # from any directory and still find the credentials file the operator placed there.
    inventory_path = "inventory.json"

    if not console_name and not os.path.exists(inventory_path):
        host = os.getenv("UNIFI_HOST")
        api_key = os.getenv("UNIFI_API_KEY")
        cloud_host = os.getenv("UNIFI_CLOUD_HOST")
        cloud_api_key = os.getenv("UNIFI_CLOUD_API_KEY")
        site_id_raw = os.getenv("UNIFI_SITE_ID")
        console_id = None
    else:
        console_name = console_name or "default"
        if not os.path.exists(inventory_path):
            logger.critical(f"Requested console '{console_name}' but {inventory_path} is missing.")
            sys.exit(1)

        try:
            with open(inventory_path) as f:
                inventory = json.load(f)
        except json.JSONDecodeError as e:
            logger.critical(f"Invalid JSON in {inventory_path}: {e}")
            sys.exit(1)

        cloud_config = inventory.get("cloud", {})
        cloud_host = os.getenv("UNIFI_CLOUD_HOST") or cloud_config.get("host", "api.ui.com")
        cloud_api_key = os.getenv("UNIFI_CLOUD_API_KEY") or cloud_config.get("api_key")

        consoles = inventory.get("consoles", {})
        if console_name not in consoles:
            logger.critical(f"Console '{console_name}' not found. Available: {list(consoles.keys())}")
            sys.exit(1)

        target = consoles[console_name]
        host = os.getenv("UNIFI_HOST") or target.get("host")
        api_key = os.getenv("UNIFI_API_KEY") or target.get("api_key")
        site_id_raw = os.getenv("UNIFI_SITE_ID") or target.get("site_id")
        console_id = target.get("console_id")

    # WHY: Fail fast at startup rather than letting commands fail mid-execution
    # with cryptic HTTP errors when credentials are incomplete.
    if not site_id_raw or (not console_id and not all([host, api_key])):
        logger.critical("Initialization Failed: Missing HOST, API_KEY, or SITE_ID for active context.")
        sys.exit(1)

    try:
        site_id = UUID(site_id_raw)
    except ValueError:
        logger.critical(f"Initialization Failed: SITE_ID must be a valid UUID. Received: {site_id_raw}")
        sys.exit(1)

    return GlobalRegistry(
        HOST=host or "",
        API_KEY=api_key or "",
        CLOUD_HOST=cloud_host or "",
        CLOUD_API_KEY=cloud_api_key or "",
        SITE_ID=site_id,
        SITE_ID_RAW=site_id_raw,
        CONSOLE_ID=console_id,
        CONSOLE_NAME=console_name,
        VERIFY_SSL=verify_ssl,
        DEBUG=debug_mode,
    )


REGISTRY = _initialize_registry()
