"""CLI Execution Handlers — maps parsed arguments to manager modules."""

__version__ = "1.0.0"

import itertools
import json
import logging
import re
from typing import Any

from .api_client.client import Client
from .registry import REGISTRY
from .modules.system_info_manager import UnifiInfoManager
from .modules.cloud_manager import UnifiCloudManager
from .modules.acl_manager import UnifiAclManager
from .modules.client_manager import UnifiClientManager
from .modules.dns_manager import UnifiDnsManager
from .modules.firewall_manager import UnifiFirewallManager
from .modules.network_manager import UnifiNetworkManager
from .modules.resource_manager import UnifiResourceManager
from .modules.site_manager import UnifiSiteManager
from .modules.traffic_matching_manager import UnifiTrafficMatchingManager
from .modules.device_manager import UnifiDeviceManager
from .modules.wifi_manager import UnifiWifiManager

logger = logging.getLogger("OpsDirectorHandlers")


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def pretty_print_json(obj: Any) -> str:
    if not obj:
        return "Not Found / Operation Failed"
    if hasattr(obj, "to_dict"):
        return json.dumps(obj.to_dict(), indent=2)
    if isinstance(obj, (dict, list)):
        return json.dumps(obj, indent=2)
    return str(obj)


def _format_key(key: str) -> str:
    s = key.replace("_", " ")
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[a-zA-Z])(?=[0-9])", " ", s)
    return s.title()


def _format_value(key: str, value: Any) -> str:
    if value is None or value == "":
        return "N/A"
    key_lower = key.lower()

    if "uptime" in key_lower and isinstance(value, (int, float)):
        m, s = divmod(int(value), 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        parts = []
        if d > 0:
            parts.append(f"{d}d")
        if h > 0:
            parts.append(f"{h}h")
        if m > 0:
            parts.append(f"{m}m")
        if s > 0 or not parts:
            parts.append(f"{s}s")
        return " ".join(parts)

    if ("pct" in key_lower or "utilization" in key_lower or "percentage" in key_lower) and isinstance(value, (int, float)):
        return f"{value}%"

    if "bps" in key_lower and isinstance(value, (int, float)):
        if value >= 1_000_000_000:
            return f"{value / 1_000_000_000:.2f} Gbps"
        elif value >= 1_000_000:
            return f"{value / 1_000_000:.2f} Mbps"
        elif value >= 1_000:
            return f"{value / 1_000:.2f} Kbps"
        return f"{value} bps"

    if isinstance(value, str) and "T" in value and value.endswith("Z"):
        return value.replace("T", " ").replace("Z", " UTC")

    return str(value)


def format_human_readable(obj: Any, indent: int = 0) -> str:
    if obj is None or obj == "":
        return "Not Found / Operation Failed"
    if hasattr(obj, "to_dict"):
        obj = obj.to_dict()
    if not isinstance(obj, (dict, list)):
        return str(obj)

    lines = []
    spacing = " " * indent
    if isinstance(obj, dict):
        for k, v in obj.items():
            if v is None or v == [] or v == {}:
                continue
            clean_key = _format_key(k)
            if isinstance(v, (dict, list)) and v:
                lines.append(f"{spacing}{clean_key}:")
                lines.append(format_human_readable(v, indent + 2))
            else:
                formatted_val = _format_value(k, v)
                target_width = max(32 - indent, len(clean_key))
                lines.append(f"{spacing}{clean_key:<{target_width}}: {formatted_val}")
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)) and item:
                lines.append(f"{spacing}-")
                lines.append(format_human_readable(item, indent + 2))
            else:
                lines.append(f"{spacing}- {item}")
    return "\n".join(lines)


def display_output(args: Any, title: str, data: Any) -> None:
    if getattr(args, "json", False):
        print(pretty_print_json(data))
    else:
        print(f"[{title}]\n{format_human_readable(data)}")


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------

def handle_inventory_command() -> None:
    import os

    inventory_path = "inventory.json"
    if not os.path.exists(inventory_path):
        print("No inventory.json found.")
        return
    try:
        with open(inventory_path, "r") as f:
            inventory = json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {inventory_path}: {e}")
        return

    consoles = inventory.get("consoles", {})
    if not consoles:
        print("No consoles found in inventory.json.")
        return

    print("\n[CONFIGURED CONSOLES]")
    for console_name, details in consoles.items():
        host = details.get("host", "N/A")
        print(f"  - {console_name:<32} | Host: {host}")
    print()


def handle_report_command(args: Any, shared_client: Client) -> None:
    import sys
    from .modules.report_manager import build_report, default_filename
    from .registry import REGISTRY

    console = REGISTRY.CONSOLE_NAME or "default"
    limit = getattr(args, "limit", 500)
    to_stdout = getattr(args, "stdout", False)
    out_path = getattr(args, "out", None)

    print(f"\nBuilding report for '{console}' (limit: {limit} per collection)...", file=sys.stderr)
    print("", file=sys.stderr)

    report = build_report(shared_client, limit=limit)

    payload = json.dumps(report, indent=2, default=str)

    if to_stdout:
        print(payload)
    else:
        path = out_path or default_filename(console)
        with open(path, "w", encoding="utf-8") as f:
            f.write(payload)
        sections_ok  = sum(1 for v in _iter_sections(report) if v.get("error") is None)
        sections_err = sum(1 for v in _iter_sections(report) if v.get("error") is not None)
        print("", file=sys.stderr)
        print(f"Report written to: {path}", file=sys.stderr)
        print(f"Sections: {sections_ok} OK, {sections_err} failed", file=sys.stderr)
        print(f"\nReport written to: {path}\n")


def _iter_sections(report: dict):
    """Yield all leaf section dicts that have an 'error' key."""
    for v in report.values():
        if isinstance(v, dict):
            if "error" in v:
                yield v
            else:
                yield from _iter_sections(v)


def handle_version_command(args: Any, shared_client: Client) -> None:
    from .modules.version_manager import run_version_check
    as_json = getattr(args, "json", False)
    if not as_json:
        print("\n[VERSION CHECK]")
    run_version_check(shared_client, as_json=as_json)
    if not as_json:
        print()


def handle_cloud_commands(args: Any) -> None:
    try:
        with UnifiCloudManager() as cloud_mgr:
            if args.cloud_command == "hosts":
                logger.debug("Executing GET for Cloud Consoles")
                hosts = cloud_mgr.get_cloud_hosts()
                print("\n[UNIFI CLOUD CONSOLES]")
                for h in hosts:
                    host_id = h.get("id", "N/A")
                    ip_addr = h.get("ipAddress", "N/A")
                    owner = h.get("owner", "false")
                    user_data = h.get("userData", {})
                    reported_state = h.get("reportedState", {})
                    hardware = reported_state.get("hardware", {})
                    print(f"  - {reported_state.get('name', 'N/A'):<32} (ID: {host_id})")
                    print(f"    * State:     {reported_state.get('state', 'UNKNOWN')}")
                    print(f"    * Model:     {hardware.get('shortname', 'UNKNOWN')}")
                    print(f"    * Serial:    {hardware.get('serialno', 'UNKNOWN')}")
                    print(f"    * UUID:      {hardware.get('uuid', 'UNKNOWN')}")
                    print(f"    * Version:   {reported_state.get('version', 'N/A')}")
                    print(f"    * Hostname:  {reported_state.get('hostname', 'N/A')}")
                    print(f"    * IPv4:      {ip_addr}")
                    print(f"    * Owner:     {owner}")
                    print(f"    * Role:      {user_data.get('role', 'UNKNOWN')}\n")
                print(f"\nTotal Consoles: {len(hosts)}\n")

            elif args.cloud_command == "isp-metrics":
                logger.debug(f"Executing GET for ISP Metrics (Site: {REGISTRY.SITE_ID})")
                metrics = cloud_mgr.get_isp_metrics(site_id=str(REGISTRY.SITE_ID))
                display_output(args, "ISP HEALTH METRICS (Last 24h)", metrics)

    except Exception as e:
        logger.error(f"Fatal: Cloud command execution failed: {e}", exc_info=True)


def run_comprehensive_audit(args: Any, shared_client: Client) -> None:
    print("=" * 80)
    print(f"INITIATING UNIFI AUDIT FOR HOST: {REGISTRY.HOST}")
    print("=" * 80)
    print()
    detailed = getattr(args, "detailed", False)
    limit = getattr(args, "limit", 10)
    client_limit = getattr(args, "clients", 2)

    try:
        # System Info
        print("=" * 28)
        print("  SYSTEM INFO")
        print("=" * 28)
        info_mgr = UnifiInfoManager(client=shared_client)
        sys_info = info_mgr.get_system_info()
        if sys_info:
            print(f"  - Version: {getattr(sys_info, 'application_version', 'Unknown')}")
        print()

        # Sites
        print("=" * 28)
        print("  SITES")
        print("=" * 28)
        site_mgr = UnifiSiteManager(client=shared_client)
        for site in site_mgr.iter_sites(limit=limit):
            print(f"  - {site.name:<32} | ID: {site.id}")
        print()

        # Devices
        print("=" * 28)
        print("  ADOPTED HARDWARE")
        print("=" * 28)
        device_mgr = UnifiDeviceManager(client=shared_client, site_id=REGISTRY.SITE_ID)
        for dev in device_mgr.iter_adopted(limit=limit):
            name = dev.name or "Unnamed"
            if detailed:
                display_output(args, f"DEVICE DETAIL ({dev.model})", device_mgr.get_device_details(dev.id))
                print("\n" + "=" * 70 + "\n")
            else:
                print(f"  - {name:<32} | Model: {dev.model:<28} | State: {dev.state:<8} | ID: {dev.id}")
                print()

        # Resources
        res_mgr = UnifiResourceManager(client=shared_client, site_id=REGISTRY.SITE_ID)

        print("=" * 28)
        print("  WAN INTERFACES")
        print("=" * 28)
        for w in res_mgr.list_wans():
            print(f"  - {getattr(w, 'name', 'Unknown WAN'):<32} | ID: {getattr(w, 'id', 'N/A')}")
        print()

        print("=" * 28)
        print("  SITE-TO-SITE TUNNELS")
        print("=" * 28)
        for v in res_mgr.iter_vpn_tunnels(limit=limit):
            print(f"  - {getattr(v, 'name', str(v)):<32} | Type: {getattr(v, 'type', 'N/A'):<10} | ID: {getattr(v, 'id', 'N/A')}")
        print()

        print("=" * 28)
        print("  RADIUS PROFILES")
        print("=" * 28)
        for r in res_mgr.iter_radius_profiles(limit=limit):
            print(f"  - {getattr(r, 'name', str(r)):<32} | ID: {getattr(r, 'id', 'N/A')}")
        print()

        # DNS
        print("=" * 28)
        print("  DNS POLICIES")
        print("=" * 28)
        dns_mgr = UnifiDnsManager(client=shared_client, site_id=REGISTRY.SITE_ID)
        for p in dns_mgr.list_policies(limit=limit):
            if detailed:
                display_output(args, f"DNS POLICY DETAIL ({p.domain})", dns_mgr.get_policy(p.id))
                print("\n" + "=" * 70 + "\n")
            else:
                print(f"  - {p.domain:<32} | Enabled: {str(p.enabled):<5} | ID: {p.id}")
                print()

        # Networks
        print("=" * 28)
        print("  NETWORKS & VLANs")
        print("=" * 28)
        net_mgr = UnifiNetworkManager(client=shared_client, site_id=REGISTRY.SITE_ID)
        for net in net_mgr.iter_networks(limit=limit):
            net_display = f"[{net.vlan_id}] {net.name}"
            if detailed:
                display_output(args, f"NETWORK DETAIL ({net_display})", net_mgr.get_network(net.id))
                print("\n" + "=" * 70 + "\n")
            else:
                print(f"  - {net_display:<32} | Mgmt: {net.management:<8} | ID: {net.id}")
                print()

        # WiFi
        print("=" * 28)
        print("  WI-FI SSIDs")
        print("=" * 28)
        wifi_mgr = UnifiWifiManager(client=shared_client, site_id=REGISTRY.SITE_ID)
        for ssid in wifi_mgr.iter_broadcasts(limit=limit):
            state = "Enabled" if ssid.enabled else "Disabled"
            if detailed:
                display_output(args, f"WI-FI BROADCAST DETAIL ({ssid.name})", wifi_mgr.get_broadcast(ssid.id))
                print("\n" + "=" * 70 + "\n")
            else:
                print(f"  - {ssid.name:<32} | State: {state:<8} | ID: {ssid.id}")
                print()

        # ACLs
        print("=" * 28)
        print("  ACLs")
        print("=" * 28)
        acl_mgr = UnifiAclManager(client=shared_client, site_id=REGISTRY.SITE_ID)
        for r in acl_mgr.iter_rules(limit=limit):
            print(f"  - {r.name:<32} | Action: {getattr(r, 'action', 'N/A'):<8} | ID: {r.id}")
        print()

        # Firewall
        fw_mgr = UnifiFirewallManager(client=shared_client, site_id=REGISTRY.SITE_ID)
        exclude_sys = not getattr(args, "all", False)

        print("=" * 28)
        print("  FIREWALL ZONES")
        print("=" * 28)
        for z in fw_mgr.list_zones(limit=limit, exclude_system=exclude_sys):
            name = getattr(z, "name", "Unknown Zone")
            origin = getattr(getattr(z, "metadata", None), "origin", "UNKNOWN").upper()
            id_str = "" if "SYSTEM" in origin else f" | ID: {getattr(z, 'id', 'N/A')}"
            print(f"  - {name:<32} | Origin: {origin:<14}{id_str}")
        print()

        print("=" * 28)
        print("  FIREWALL POLICIES")
        print("=" * 28)
        for fw in fw_mgr.list_policies(limit=limit, exclude_system=exclude_sys):
            fw_name = getattr(fw, "name", "Unnamed")
            action = getattr(getattr(fw, "action", None), "type_", "UNKNOWN")
            state = "Enabled" if getattr(fw, "enabled", False) else "Disabled"
            origin = getattr(getattr(fw, "metadata", None), "origin", "UNKNOWN").upper()
            id_str = "" if "SYSTEM" in origin else f" | ID: {getattr(fw, 'id', 'N/A')}"
            print(f"  - {fw_name:<32} | Action: {action:<8} | State: {state:<8} | Origin: {origin:<14}{id_str}")
        print()

        # Clients
        print("=" * 28)
        print(f"  ACTIVE CLIENTS (Limit: {client_limit})")
        print("=" * 28)
        client_mgr = UnifiClientManager(client=shared_client, site_id=REGISTRY.SITE_ID)
        for c in itertools.islice(client_mgr.iter_clients(limit=client_limit), client_limit):
            name = getattr(c, "name", None) or "Unknown Device"
            ip_attr = getattr(c, "ip_address", "N/A")
            ip = ip_attr if isinstance(ip_attr, str) else "N/A"
            if detailed:
                display_output(args, f"CLIENT DETAIL ({name})", client_mgr.get_client(c.id))
                print("\n" + "=" * 70 + "\n")
            else:
                print(f"  - {name:<32} | IP: {ip:<16} | MAC/ID: {c.id}")
        print()

        print("=" * 80)
        print("COMPREHENSIVE AUDIT COMPLETE")
        print("=" * 80)
        print()

    except Exception as e:
        logger.error(f"Audit terminated prematurely: {e}", exc_info=True)
    finally:
        logger.debug("Releasing resources and terminating director.")


def handle_acl_commands(args: Any, shared_client: Client) -> None:
    acl_mgr = UnifiAclManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.acl_command == "list":
            print("\n[ACL RULES]")
            count = 0
            for r in acl_mgr.iter_rules(limit=args.limit):
                print(f"  - {r.name:<32} | ID: {r.id} | Action: {getattr(r, 'action', 'N/A')}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.acl_command == "get":
            display_output(args, "ACL RULE DETAILS", acl_mgr.get_rule(args.id))

        elif args.acl_command == "create":
            display_output(args, "CREATE SUCCESS", acl_mgr.create_rule(json.loads(args.payload)))

        elif args.acl_command == "update":
            display_output(args, "UPDATE SUCCESS", acl_mgr.update_rule(args.id, json.loads(args.payload)))

        elif args.acl_command == "delete":
            print(f"\n[DELETE RESULT] Success: {acl_mgr.delete_rule(args.id)}\n")

        elif args.acl_command == "get-order":
            print(f"\n[ACL RULE ORDER]\n{json.dumps([str(i) for i in acl_mgr.get_order()], indent=2)}\n")

        elif args.acl_command == "set-order":
            print(f"\n[SET-ORDER RESULT] Success: {acl_mgr.set_order(json.loads(args.payload))}\n")

    except json.JSONDecodeError as e:
        logger.error(f"Fatal: Invalid JSON payload: {e}")
    except Exception as e:
        logger.error(f"Fatal: ACL command failed: {e}", exc_info=True)


def handle_client_commands(args: Any, shared_client: Client) -> None:
    client_mgr = UnifiClientManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.client_command == "list":
            print("\n[ACTIVE CLIENTS]")
            count = 0
            for c in client_mgr.iter_clients(limit=args.limit):
                name = getattr(c, "name", None) or "Unknown Device"
                ip_attr = getattr(c, "ip_address", "N/A")
                ip = ip_attr if isinstance(ip_attr, str) else "N/A"
                print(f"  - {name:<32} | IP: {ip:<16} | MAC/ID: {c.id}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.client_command == "get":
            display_output(args, "CLIENT DETAILS", client_mgr.get_client(args.id))

        elif args.client_command == "action":
            print(f"\n[ACTION RESULT] Success: {client_mgr.trigger_action(args.id, args.action)}\n")

    except Exception as e:
        logger.error(f"Fatal: Client command failed: {e}", exc_info=True)


def handle_dns_commands(args: Any, shared_client: Client) -> None:
    dns_mgr = UnifiDnsManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.dns_command == "list":
            print("\n[DNS POLICIES]")
            count = 0
            for p in dns_mgr.list_policies(limit=args.limit):
                print(f"  - {getattr(p, 'domain', 'Unknown Domain'):<32} | ID: {p.id} | Enabled: {p.enabled}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.dns_command == "get":
            display_output(args, "DNS POLICY DETAILS", dns_mgr.get_policy(args.id))

        elif args.dns_command == "create":
            display_output(args, "CREATE SUCCESS", dns_mgr.create_policy(json.loads(args.payload)))

        elif args.dns_command == "update":
            display_output(args, "UPDATE SUCCESS", dns_mgr.update_policy(args.id, json.loads(args.payload)))

        elif args.dns_command == "delete":
            print(f"\n[DELETE RESULT] Success: {dns_mgr.delete_policy(args.id)}\n")

    except json.JSONDecodeError as e:
        logger.error(f"Fatal: Invalid JSON payload: {e}")
    except Exception as e:
        logger.error(f"Fatal: DNS command failed: {e}", exc_info=True)


def handle_firewall_commands(args: Any, shared_client: Client) -> None:
    fw_mgr = UnifiFirewallManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.firewall_command == "list-zones":
            zones = fw_mgr.list_zones()
            print("\n[FIREWALL ZONES]")
            for z in zones:
                print(f"  - {getattr(z, 'name', 'Unknown Zone'):<32} | ID: {getattr(z, 'id', 'N/A')}")
            print(f"\nTotal retrieved: {len(zones)}")

        elif args.firewall_command == "get-zone":
            display_output(args, "FIREWALL ZONE DETAILS", fw_mgr.get_zone(args.id))

        elif args.firewall_command == "create-zone":
            result = fw_mgr.create_zone(args.name, json.loads(args.network_ids))
            print(f"\n[CREATE ZONE SUCCESS]\n{pretty_print_json(result)}\n")

        elif args.firewall_command == "update-zone":
            display_output(args, "UPDATE ZONE SUCCESS", fw_mgr.update_zone(args.id, args.name, json.loads(args.network_ids)))

        elif args.firewall_command == "delete-zone":
            print(f"\n[DELETE ZONE RESULT] Success: {fw_mgr.delete_zone(args.id)}\n")

        elif args.firewall_command == "list-policies":
            exclude_sys = not getattr(args, "all", False)
            policies = fw_mgr.list_policies(limit=args.limit, exclude_system=exclude_sys)
            print("\n[FIREWALL POLICIES]")
            for p in policies:
                p_name = getattr(p, "name", "Unnamed")  # FIX: archive used undefined `name` variable here
                action = getattr(getattr(p, "action", None), "type_", "UNKNOWN")
                state = "Enabled" if getattr(p, "enabled", False) else "Disabled"
                origin = getattr(getattr(p, "metadata", None), "origin", "UNKNOWN")
                id_str = "" if "SYSTEM" in origin else f" | ID: {getattr(p, 'id', 'N/A')}"
                print(f"  - {p_name:<30} | Action: {action:<8} | State: {state:<8} | Origin: {origin:<16}{id_str}")
            print(f"\nTotal retrieved: {len(policies)}")

        elif args.firewall_command == "get-policy":
            display_output(args, "FIREWALL POLICY DETAILS", fw_mgr.get_policy(args.id))

        elif args.firewall_command == "create-policy":
            display_output(args, "CREATE POLICY SUCCESS", fw_mgr.create_policy(json.loads(args.payload)))

        elif args.firewall_command == "update-policy":
            display_output(args, "UPDATE POLICY SUCCESS", fw_mgr.update_policy(args.id, json.loads(args.payload)))

        elif args.firewall_command == "delete-policy":
            print(f"\n[DELETE POLICY RESULT] Success: {fw_mgr.delete_policy(args.id)}\n")

        elif args.firewall_command == "toggle-policy":
            success = fw_mgr.toggle_policy(args.id, enabled=(args.state.lower() == "enable"))
            print(f"\n[TOGGLE POLICY RESULT] Success: {success}\n")

        elif args.firewall_command == "get-order":
            result = fw_mgr.get_current_order(args.source_zone, args.dest_zone)
            print(f"\n[FIREWALL RULE ORDER]\n{json.dumps(result, indent=2)}\n")

        elif args.firewall_command == "set-order":
            success = fw_mgr.set_rule_order(args.source_zone, args.dest_zone, json.loads(args.payload))
            print(f"\n[SET-ORDER RESULT] Success: {success}\n")

    except json.JSONDecodeError as e:
        logger.error(f"Fatal: Invalid JSON payload: {e}")
    except Exception as e:
        logger.error(f"Fatal: Firewall command failed: {e}", exc_info=True)


def handle_network_commands(args: Any, shared_client: Client) -> None:
    net_mgr = UnifiNetworkManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.net_command == "list":
            print("\n[NETWORKS & VLANs]")
            count = 0
            for net in net_mgr.iter_networks(limit=args.limit):
                print(f"  - [{net.vlan_id}] {net.name} (Mgmt: {net.management}) | ID: {net.id}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.net_command == "get":
            display_output(args, "NETWORK DETAILS", net_mgr.get_network(args.id))

        elif args.net_command == "refs":
            display_output(args, "NETWORK REFERENCES", net_mgr.get_references(args.id))

        elif args.net_command == "create":
            display_output(args, "CREATE SUCCESS", net_mgr.create_network(json.loads(args.payload)))

        elif args.net_command == "update":
            display_output(args, "UPDATE SUCCESS", net_mgr.update_network(args.id, json.loads(args.payload)))

        elif args.net_command == "delete":
            print(f"\n[DELETE RESULT] Success: {net_mgr.delete_network(args.id, force=args.force)}\n")

    except json.JSONDecodeError as e:
        logger.error(f"Fatal: Invalid JSON payload: {e}")
    except Exception as e:
        logger.error(f"Fatal: Network command failed: {e}", exc_info=True)


def handle_resource_commands(args: Any, shared_client: Client) -> None:
    res_mgr = UnifiResourceManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.resource_command == "countries":
            print("\n[COUNTRIES]")
            count = 0
            for c in res_mgr.list_countries(limit=args.limit):
                if count >= args.limit:
                    break
                print(f"  - {getattr(c, 'name', str(c))}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.resource_command == "wans":
            wans = res_mgr.list_wans(limit=args.limit)
            print("\n[WAN INTERFACES]")
            for w in wans:
                print(f"  - {getattr(w, 'name', 'Unknown WAN')} | ID: {getattr(w, 'id', 'N/A')}")
            print(f"\nTotal retrieved: {len(wans)}")

        elif args.resource_command == "tags":
            print("\n[DEVICE TAGS]")
            count = 0
            for t in res_mgr.iter_device_tags(limit=args.limit):
                if count >= args.limit:
                    break
                print(f"  - {getattr(t, 'name', str(t))} | ID: {getattr(t, 'id', 'N/A')}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.resource_command == "dpi-apps":
            print("\n[DPI APPLICATIONS]")
            count = 0
            for a in res_mgr.iter_dpi_apps(limit=args.limit):
                if count >= args.limit:
                    break
                print(f"  - {getattr(a, 'name', str(a))} | ID: {getattr(a, 'id', 'N/A')}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.resource_command == "dpi-categories":
            cats = res_mgr.list_dpi_categories()
            print("\n[DPI CATEGORIES]")
            for c in cats:
                print(f"  - {getattr(c, 'name', str(c))} | ID: {getattr(c, 'id', 'N/A')}")
            print(f"\nTotal retrieved: {len(cats)}")

        elif args.resource_command == "radius":
            print("\n[RADIUS PROFILES]")
            count = 0
            for r in res_mgr.iter_radius_profiles(limit=args.limit):
                if count >= args.limit:
                    break
                print(f"  - {getattr(r, 'name', str(r))} | ID: {getattr(r, 'id', 'N/A')}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.resource_command == "vpn-tunnels":
            print("\n[SITE-TO-SITE VPN TUNNELS]")
            count = 0
            for v in res_mgr.iter_vpn_tunnels(limit=args.limit):
                if count >= args.limit:
                    break
                print(f"  - {getattr(v, 'name', str(v))} | Type: {getattr(v, 'type', 'N/A')} | ID: {getattr(v, 'id', 'N/A')}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.resource_command == "vpn-servers":
            print("\n[VPN SERVERS]")
            count = 0
            for v in res_mgr.iter_vpn_servers(limit=args.limit):
                if count >= args.limit:
                    break
                print(f"  - {getattr(v, 'name', str(v))} | Protocol: {getattr(v, 'protocol', 'N/A')} | ID: {getattr(v, 'id', 'N/A')}")
                count += 1
            print(f"\nTotal retrieved: {count}")

    except Exception as e:
        logger.error(f"Fatal: Resource command failed: {e}", exc_info=True)


def handle_site_commands(args: Any, shared_client: Client) -> None:
    site_mgr = UnifiSiteManager(client=shared_client)
    try:
        if args.site_command == "list":
            print("\n[SITES]")
            for site in site_mgr.iter_sites(limit=args.limit):
                print(f"  - {site.name} (ID: {site.id})")
            print()
    except Exception as e:
        logger.error(f"Fatal: Site command failed: {e}", exc_info=True)


def handle_traffic_commands(args: Any, shared_client: Client) -> None:
    traffic_mgr = UnifiTrafficMatchingManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.traffic_command == "list":
            print("\n[TRAFFIC MATCHING LISTS]")
            count = 0
            for t in traffic_mgr.iter_matching_lists(limit=args.limit):
                print(f"  - {t.name} | ID: {t.id}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.traffic_command == "get":
            display_output(args, "TRAFFIC MATCHING LIST DETAILS", traffic_mgr.get_list(args.id))

        elif args.traffic_command == "create":
            display_output(args, "CREATE SUCCESS", traffic_mgr.create_list(json.loads(args.payload)))

        elif args.traffic_command == "update":
            display_output(args, "UPDATE SUCCESS", traffic_mgr.update_list(args.id, json.loads(args.payload)))

        elif args.traffic_command == "delete":
            print(f"\n[DELETE RESULT] Success: {traffic_mgr.delete_list(args.id)}\n")

    except json.JSONDecodeError as e:
        logger.error(f"Fatal: Invalid JSON payload: {e}")
    except Exception as e:
        logger.error(f"Fatal: Traffic command failed: {e}", exc_info=True)


def handle_device_commands(args: Any, shared_client: Client) -> None:
    device_mgr = UnifiDeviceManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.device_command == "pending":
            results = device_mgr.list_pending()
            print("\n[PENDING ADOPTION]")
            for dev in results:
                print(f"  - Model: {dev.model:<28} | {dev.mac}")
            print(f"\nTotal pending: {len(results)}\n")

        elif args.device_command == "list":
            print("\n[ADOPTED HARDWARE]")
            count = 0
            for dev in device_mgr.iter_adopted(limit=args.limit):
                name = dev.name or "Unnamed"
                print(f"  - {name:<32} | Model: {dev.model:<28} | State: {dev.state:<10} | ID: {dev.id}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.device_command == "get":
            display_output(args, "DEVICE DETAILS", device_mgr.get_device_details(args.id))

        elif args.device_command == "stats":
            display_output(args, "DEVICE STATS", device_mgr.get_stats(args.id))

        elif args.device_command == "adopt":
            print(f"\n[ADOPT RESULT] Success: {device_mgr.adopt(args.mac, args.name)}\n")

        elif args.device_command == "decommission":
            print(f"\n[DECOMMISSION RESULT] Success: {device_mgr.decommission(args.id)}\n")

        elif args.device_command == "action":
            print(f"\n[ACTION RESULT] Success: {device_mgr.device_action(args.id, args.action)}\n")

        elif args.device_command == "port-action":
            print(f"\n[PORT ACTION RESULT] Success: {device_mgr.port_action(args.id, args.port_idx, args.action)}\n")

    except Exception as e:
        logger.error(f"Fatal: Device command failed: {e}", exc_info=True)


def handle_wifi_commands(args: Any, shared_client: Client) -> None:
    wifi_mgr = UnifiWifiManager(client=shared_client, site_id=REGISTRY.SITE_ID)
    try:
        if args.wifi_command == "list":
            print("\n[WI-FI BROADCASTS]")
            count = 0
            for w in wifi_mgr.iter_broadcasts(limit=args.limit):
                state = "Enabled" if w.enabled else "Disabled"
                print(f"  - {w.name} | ID: {w.id} | State: {state}")
                count += 1
            print(f"\nTotal retrieved: {count}")

        elif args.wifi_command == "get":
            display_output(args, "WI-FI BROADCAST DETAILS", wifi_mgr.get_broadcast(args.id))

        elif args.wifi_command == "create":
            display_output(args, "CREATE SUCCESS", wifi_mgr.provision_broadcast(json.loads(args.payload)))

        elif args.wifi_command == "update":
            display_output(args, "UPDATE SUCCESS", wifi_mgr.update_broadcast(args.id, json.loads(args.payload)))

        elif args.wifi_command == "delete":
            print(f"\n[DELETE RESULT] Success: {wifi_mgr.delete_broadcast(args.id, force=args.force)}\n")

    except json.JSONDecodeError as e:
        logger.error(f"Fatal: Invalid JSON payload: {e}")
    except Exception as e:
        logger.error(f"Fatal: Wi-Fi command failed: {e}", exc_info=True)


def handle_hotspot_commands(args: Any, shared_client: Client) -> None:
    from .modules.hotspot_manager import UnifiHotspotManager
    from uuid import UUID
    mgr = UnifiHotspotManager(client=shared_client)
    try:
        if args.hotspot_command == "list":
            print("\n[HOTSPOT VOUCHERS]")
            vouchers = mgr.list_vouchers(limit=args.limit, filter_=getattr(args, "filter_", None))
            if not vouchers:
                print("  No vouchers found.")
            for v in vouchers:
                status = "Expired" if v.expired else "Active"
                guests = getattr(v, "authorized_guest_count", 0)
                print(f"  - {v.name} | Code: {v.code} | {status} | Guests: {guests} | ID: {v.id}")
            print(f"\nTotal retrieved: {len(vouchers)}")

        elif args.hotspot_command == "get":
            display_output(args, "VOUCHER DETAILS", mgr.get_voucher(UUID(args.id)))

        elif args.hotspot_command == "create":
            result = mgr.create_vouchers(
                name=args.name,
                time_limit_minutes=args.minutes,
                count=args.count,
                authorized_guest_limit=args.guest_limit,
                data_usage_limit_mbytes=args.data_limit,
                rx_rate_limit_kbps=args.rx_limit,
                tx_rate_limit_kbps=args.tx_limit,
            )
            if result:
                created = getattr(result, "created_voucher_ids", [])
                print(f"\n[CREATE SUCCESS] {len(created)} voucher(s) created.")
                for vid in created:
                    print(f"  ID: {vid}")
                print()
            else:
                print("\n[CREATE FAILED]\n")

        elif args.hotspot_command == "delete":
            # WHY: Deletion is logged at WARNING so single-voucher deletes are
            # visible in normal (non-debug) log output without requiring --debug.
            logger.warning(f"Deleting voucher {args.id}")
            result = mgr.delete_voucher(UUID(args.id))
            deleted = getattr(result, "deleted_count", "unknown") if result else 0
            print(f"\n[DELETE RESULT] Deleted: {deleted}\n")

        elif args.hotspot_command == "delete-all":
            # WHY: Bulk delete is logged at WARNING — mass deletion is irreversible.
            logger.warning(f"Bulk-deleting vouchers with filter: {args.filter_}")
            result = mgr.delete_vouchers(filter_=args.filter_)
            deleted = getattr(result, "deleted_count", "unknown") if result else 0
            print(f"\n[BULK DELETE RESULT] Deleted: {deleted}\n")

    except Exception as e:
        logger.error(f"Fatal: Hotspot command failed: {e}", exc_info=True)


def handle_switching_commands(args: Any, shared_client: Client) -> None:
    from .modules.switching_manager import UnifiSwitchingManager
    from uuid import UUID
    mgr = UnifiSwitchingManager(client=shared_client)
    try:
        if args.switching_command == "lags":
            print("\n[LINK AGGREGATION GROUPS]")
            items = mgr.list_lags(limit=args.limit)
            if not items:
                print("  No LAGs configured.")
            for item in items:
                members = len(getattr(item, "members", []))
                print(f"  - Type: {getattr(item, 'type_', 'N/A')} | Members: {members} | ID: {item.id}")
            print(f"\nTotal retrieved: {len(items)}")

        elif args.switching_command == "lag":
            display_output(args, "LAG DETAILS", mgr.get_lag(UUID(args.id)))

        elif args.switching_command == "stacks":
            print("\n[SWITCH STACKS]")
            items = mgr.list_stacks(limit=args.limit)
            if not items:
                print("  No switch stacks configured.")
            for item in items:
                members = len(getattr(item, "members", []))
                print(f"  - {item.name} | Members: {members} | ID: {item.id}")
            print(f"\nTotal retrieved: {len(items)}")

        elif args.switching_command == "stack":
            display_output(args, "SWITCH STACK DETAILS", mgr.get_stack(UUID(args.id)))

        elif args.switching_command == "mclags":
            print("\n[MC-LAG DOMAINS]")
            items = mgr.list_mc_lag_domains(limit=args.limit)
            if not items:
                print("  No MC-LAG domains configured.")
            for item in items:
                peers = len(getattr(item, "peers", []))
                print(f"  - {item.name} | Peers: {peers} | ID: {item.id}")
            print(f"\nTotal retrieved: {len(items)}")

        elif args.switching_command == "mclag":
            display_output(args, "MC-LAG DOMAIN DETAILS", mgr.get_mc_lag_domain(UUID(args.id)))

    except Exception as e:
        logger.error(f"Fatal: Switching command failed: {e}", exc_info=True)
