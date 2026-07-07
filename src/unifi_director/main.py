"""UniFi Director — CLI entry point."""

__version__ = "1.0.0"

import logging
import sys
from uuid import UUID

from .registry import REGISTRY
from .cli_parser import build_parser
from .cli_handlers import (
    handle_inventory_command,
    handle_report_command,
    handle_version_command,
    handle_cloud_commands,
    run_comprehensive_audit,
    handle_acl_commands,
    handle_client_commands,
    handle_dns_commands,
    handle_firewall_commands,
    handle_hotspot_commands,
    handle_network_commands,
    handle_resource_commands,
    handle_site_commands,
    handle_switching_commands,
    handle_traffic_commands,
    handle_device_commands,
    handle_wifi_commands,
)
from .client_factory import get_shared_client

logger = logging.getLogger("OpsDirector")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if getattr(args, "site", None):
        try:
            # WHY: Allow per-invocation site override without editing inventory.json,
            # useful when targeting a secondary site on the same console.
            REGISTRY.SITE_ID = UUID(args.site)
            REGISTRY.SITE_ID_RAW = args.site
            logger.debug(f"Overrode default Site ID. Now targeting: {REGISTRY.SITE_ID}")
        except ValueError:
            logger.error(f"Invalid UUID format provided for --site: {args.site}")
            sys.exit(1)

    try:
        with get_shared_client() as shared_client:
            if args.command == "inventory":
                handle_inventory_command()
            elif args.command == "report":
                handle_report_command(args, shared_client)
            elif args.command == "version":
                handle_version_command(args, shared_client)
            elif args.command == "cloud":
                handle_cloud_commands(args)
            elif args.command == "audit":
                run_comprehensive_audit(args, shared_client)
            elif args.command == "acl":
                handle_acl_commands(args, shared_client)
            elif args.command == "client":
                handle_client_commands(args, shared_client)
            elif args.command == "dns":
                handle_dns_commands(args, shared_client)
            elif args.command == "firewall":
                handle_firewall_commands(args, shared_client)
            elif args.command == "network":
                handle_network_commands(args, shared_client)
            elif args.command == "resource":
                handle_resource_commands(args, shared_client)
            elif args.command == "site":
                handle_site_commands(args, shared_client)
            elif args.command == "traffic":
                handle_traffic_commands(args, shared_client)
            elif args.command == "device":
                handle_device_commands(args, shared_client)
            elif args.command == "wifi":
                handle_wifi_commands(args, shared_client)
            elif args.command == "hotspot":
                handle_hotspot_commands(args, shared_client)
            elif args.command == "switching":
                handle_switching_commands(args, shared_client)
    except KeyboardInterrupt:
        print("\nExecution cancelled by user.")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Fatal orchestration failure: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
