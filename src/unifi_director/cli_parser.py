"""CLI Parser Definitions — all argparse subcommand definitions."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="UniFi Director CLI",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-c", "--console", help="Target a specific console profile from inventory.json")
    parser.add_argument("--site", help="Override the default Site ID (UUID) for this execution")
    parser.add_argument("--json", action="store_true", help="Output pure JSON for scripting/saving instead of human-readable text")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging and print exact HTTP requests")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available director commands")
    subparsers.add_parser("inventory", help="List all locally configured consoles from inventory.json")
    subparsers.add_parser("version", help="Show controller version and check for available updates")

    report_parser = subparsers.add_parser("report", help="Collect full site data across all domains into a single JSON file.")
    report_parser.add_argument("--out", metavar="FILE", help="Output file path (default: auto-named in current directory).")
    report_parser.add_argument("--limit", type=int, default=500, help="Max items per collection (default: 500).")
    report_parser.add_argument("--stdout", action="store_true", help="Print JSON to stdout instead of writing a file.")

    # --- Cloud / Telemetry ---
    cloud_parser = subparsers.add_parser("cloud", help="Manage Global Site Manager telemetry (api.ui.com)")
    cloud_subs = cloud_parser.add_subparsers(dest="cloud_command", required=True)
    cloud_subs.add_parser("hosts", help="List all global UniFi OS Consoles and their statuses")
    cloud_subs.add_parser("isp-metrics", help="Fetch 24-hour ISP health metrics (latency, packet loss, speed)")

    # --- Audit ---
    adt_parser = subparsers.add_parser("audit", help="Run the read-only comprehensive site audit")
    adt_parser.add_argument("--all", action="store_true", help="Include system-defined default firewall policies in the output.")
    adt_parser.add_argument("--detailed", action="store_true", help="Include details in the output.")
    adt_parser.add_argument("--limit", type=int, default=100, help="Maximum number to fetch.")
    adt_parser.add_argument("--clients", type=int, default=2, help="Maximum number of clients to fetch.")

    # --- ACL ---
    acl_parser = subparsers.add_parser("acl", help="Manage Access Control List (ACL) rules", formatter_class=argparse.RawTextHelpFormatter)
    acl_subs = acl_parser.add_subparsers(dest="acl_command", required=True)

    list_a_p = acl_subs.add_parser("list", help="Retrieve a list of all ACL rules on a site.")
    list_a_p.add_argument("--limit", type=int, default=50, help="Maximum number of rules to fetch.")

    acl_subs.add_parser("get", help="Retrieve details for a specific ACL Rule.").add_argument("id", help="The UUID of the ACL rule.")

    acl_payload_help = (
        "A valid JSON string mapping to the ACL rule schema.\n\n"
        "Schema Reference:\n"
        "  {\n"
        "    \"type\": \"<IPV4|MAC>\",\n"
        "    \"enabled\": <true|false>,\n"
        "    \"name\": \"<string>\",\n"
        "    \"description\": \"<string>\",\n"
        "    \"action\": \"<ALLOW|BLOCK>\",\n"
        "    \"enforcingDeviceFilter\": {\n"
        "      \"type\": \"DEVICES\",\n"
        "      \"deviceIds\": [\"<UUID>\"]\n"
        "    },\n"
        "    \"sourceFilter\": {\n"
        "      \"type\": \"<IP_ADDRESSES_OR_SUBNETS|NETWORKS|PORTS>\",\n"
        "      \"ipAddressesOrSubnets\": [\"<IP/CIDR>\"],\n"
        "      \"portFilter\": [<integer>]\n"
        "    },\n"
        "    \"destinationFilter\": {\n"
        "      \"type\": \"<IP_ADDRESSES_OR_SUBNETS|NETWORKS|PORTS>\",\n"
        "      \"ipAddressesOrSubnets\": [\"<IP/CIDR>\"],\n"
        "      \"portFilter\": [<integer>]\n"
        "    },\n"
        "    \"protocolFilter\": [\"<TCP|UDP>\"]\n"
        "  }\n\n"
        "Example:\n"
        "  '{\"type\": \"IPV4\", \"enabled\": true, \"name\": \"Block DNS\", \"action\": \"BLOCK\","
        " \"protocolFilter\": [\"UDP\"], \"destinationFilter\": {\"type\": \"PORTS\", \"portFilter\": [53]}}'\n"
    )
    create_a_p = acl_subs.add_parser("create", help="Create a new ACL rule on a site.", formatter_class=argparse.RawTextHelpFormatter)
    create_a_p.add_argument("payload", help=acl_payload_help)

    update_a_p = acl_subs.add_parser("update", help="Update an existing ACL rule on a site.", formatter_class=argparse.RawTextHelpFormatter)
    update_a_p.add_argument("id", help="The UUID of the ACL rule to update.")
    update_a_p.add_argument("payload", help=acl_payload_help)

    acl_subs.add_parser("delete", help="Delete an existing ACL rule on a site.").add_argument("id", help="The UUID of the ACL rule to delete.")
    acl_subs.add_parser("get-order", help="Retrieve ACL rule ordering on a site.")

    set_order_p = acl_subs.add_parser("set-order", help="Reorder ACL rules on a site.", formatter_class=argparse.RawTextHelpFormatter)
    set_order_p.add_argument("payload", help="A valid JSON array of UUIDs.\nExample:\n  '[\"uuid-1\", \"uuid-2\"]'\n")

    # --- Client ---
    client_parser = subparsers.add_parser("client", help="Manage connected clients.")
    client_subs = client_parser.add_subparsers(dest="client_command", required=True)

    list_c_p = client_subs.add_parser("list", help="Retrieve a list of all connected clients on a site.")
    list_c_p.add_argument("--limit", type=int, default=100, help="Maximum number of clients to fetch per page.")

    client_subs.add_parser("get", help="Retrieve detailed information about a specific connected client.").add_argument("id", help="The MAC address or UUID of the client.")

    action_c_p = client_subs.add_parser("action", help="Perform an action on a specific connected client.")
    action_c_p.add_argument("id", help="The MAC address or UUID of the client.")
    action_c_p.add_argument("action", choices=["RECONNECT", "BLOCK", "UNBLOCK", "AUTHORIZE", "UNAUTHORIZE"], help="The action to perform.")

    # --- DNS ---
    dns_parser = subparsers.add_parser("dns", help="Manage DNS policies", formatter_class=argparse.RawTextHelpFormatter)
    dns_subs = dns_parser.add_subparsers(dest="dns_command", required=True)

    list_d_p = dns_subs.add_parser("list", help="Retrieve a list of all DNS policies on a site.")
    list_d_p.add_argument("--limit", type=int, default=50, help="Maximum number of policies to fetch.")

    dns_subs.add_parser("get", help="Retrieve details for a specific DNS policy.").add_argument("id", help="The UUID of the DNS policy.")

    dns_payload_help = (
        "A valid JSON string mapping to DNS schema.\n\n"
        "Schema Reference:\n"
        "  {\n"
        "    \"type\": \"<A_RECORD>\",\n"
        "    \"enabled\": <true|false>,\n"
        "    \"domain\": \"<string>\",\n"
        "    \"ipv4Address\": \"<IP>\",\n"
        "    \"ttlSeconds\": <integer>\n"
        "  }\n\n"
        "Example (A Record):\n"
        "  '{\"type\": \"A_RECORD\", \"enabled\": true, \"domain\": \"example.com\","
        " \"ipv4Address\": \"192.168.1.10\", \"ttlSeconds\": 3600}'\n"
    )
    create_d_p = dns_subs.add_parser("create", help="Create a new DNS policy on a site.", formatter_class=argparse.RawTextHelpFormatter)
    create_d_p.add_argument("payload", help=dns_payload_help)

    update_d_p = dns_subs.add_parser("update", help="Update an existing DNS policy on a site.", formatter_class=argparse.RawTextHelpFormatter)
    update_d_p.add_argument("id", help="The UUID of the DNS policy to update.")
    update_d_p.add_argument("payload", help=dns_payload_help)

    dns_subs.add_parser("delete", help="Delete an existing DNS policy on a site.").add_argument("id", help="The UUID of the DNS policy to delete.")

    # --- Firewall ---
    fw_parser = subparsers.add_parser("firewall", help="Manage firewall zones and policies.", formatter_class=argparse.RawTextHelpFormatter)
    fw_subs = fw_parser.add_subparsers(dest="firewall_command", required=True)

    fw_subs.add_parser("list-zones", help="Retrieve a list of all firewall zones on a site.")
    fw_subs.add_parser("get-zone", help="Get firewall zone details on a site.").add_argument("id", help="The UUID of the firewall zone")

    create_z_p = fw_subs.add_parser("create-zone", help="Create a new firewall zone on a site.", formatter_class=argparse.RawTextHelpFormatter)
    create_z_p.add_argument("name", help="The name of the new zone")
    create_z_p.add_argument("network_ids", help="A JSON array string of network UUIDs.\nExample:\n  '[\"uuid-1\", \"uuid-2\"]'\n")

    update_zone_p = fw_subs.add_parser("update-zone", help="Update a firewall zone on a site.", formatter_class=argparse.RawTextHelpFormatter)
    update_zone_p.add_argument("id", help="The UUID of the firewall zone")
    update_zone_p.add_argument("name", help="The new name of the zone")
    update_zone_p.add_argument("network_ids", help="A JSON array string of network UUIDs.\nExample:\n  '[\"uuid-1\", \"uuid-2\"]'\n")

    fw_subs.add_parser("delete-zone", help="Delete a firewall zone from a site.").add_argument("id", help="The UUID of the firewall zone.")

    list_fw_p = fw_subs.add_parser("list-policies", help="Retrieve a list of firewall policies on a site.")
    list_fw_p.add_argument("--limit", type=int, default=200, help="Maximum number of policies to fetch.")
    list_fw_p.add_argument("--all", action="store_true", help="Include system-defined default policies in the output.")

    fw_subs.add_parser("get-policy", help="Retrieve details for a specific firewall policy.").add_argument("id", help="The UUID of the firewall policy.")

    fw_payload_help = (
        "A valid JSON string mapping to the firewall policy schema.\n\n"
        "Schema Reference:\n"
        "  {\n"
        "    \"enabled\": <true|false>,\n"
        "    \"name\": \"<string>\",\n"
        "    \"description\": \"<string>\",\n"
        "    \"action\": {\"type\": \"<ALLOW|BLOCK|REJECT>\", \"allowReturnTraffic\": <true|false>},\n"
        "    \"source\": {\"zoneId\": \"<UUID>\", \"trafficFilter\": {\"type\": \"<PORT|NETWORK|...>\"}},\n"
        "    \"destination\": {\"zoneId\": \"<UUID>\", \"trafficFilter\": {\"type\": \"<PORT|NETWORK|...>\"}},\n"
        "    \"ipProtocolScope\": {\"ipVersion\": \"<IPV4|IPV6|IPV4_AND_IPV6>\"},\n"
        "    \"loggingEnabled\": <true|false>\n"
        "  }\n\n"
        "Example:\n"
        "  '{}'\n"
    )
    create_policy_p = fw_subs.add_parser("create-policy", help="Create a new firewall policy on a site.", formatter_class=argparse.RawTextHelpFormatter)
    create_policy_p.add_argument("payload", help=fw_payload_help)

    update_policy_p = fw_subs.add_parser("update-policy", help="Update an existing firewall policy on a site.", formatter_class=argparse.RawTextHelpFormatter)
    update_policy_p.add_argument("id", help="The UUID of the firewall policy.")
    update_policy_p.add_argument("payload", help=fw_payload_help)

    fw_subs.add_parser("delete-policy", help="Delete an existing firewall policy on a site.").add_argument("id", help="The UUID of the firewall policy.")

    toggle_fw_p = fw_subs.add_parser("toggle-policy", help="Enable or disable a specific firewall policy.")
    toggle_fw_p.add_argument("id", help="The UUID of the firewall policy.")
    toggle_fw_p.add_argument("state", choices=["enable", "disable"], help="Target state for the policy.")

    get_order_fw = fw_subs.add_parser("get-order", help="Retrieve user-defined firewall policy ordering for a source/destination zone pair.")
    get_order_fw.add_argument("source_zone", help="The UUID of the source firewall zone.")
    get_order_fw.add_argument("dest_zone", help="The UUID of the destination firewall zone.")

    set_order_fw = fw_subs.add_parser("set-order", help="Reorder firewall policies for a source/destination zone pair.", formatter_class=argparse.RawTextHelpFormatter)
    set_order_fw.add_argument("source_zone", help="The UUID of the source firewall zone.")
    set_order_fw.add_argument("dest_zone", help="The UUID of the destination firewall zone.")
    set_order_fw.add_argument("payload", help="A JSON array string of ordered firewall policy UUIDs.\nExample:\n  '[\"uuid-1\", \"uuid-2\"]'\n")

    # --- Network ---
    net_parser = subparsers.add_parser("network", help="Manage networks and VLANs", formatter_class=argparse.RawTextHelpFormatter)
    net_subs = net_parser.add_subparsers(dest="net_command", required=True)

    list_n_p = net_subs.add_parser("list", help="Retrieve a list of all Networks and VLANs on a site.")
    list_n_p.add_argument("--limit", type=int, default=50, help="Maximum number of networks to fetch")

    net_subs.add_parser("get", help="Retrieve detailed information about a specific network.").add_argument("id", help="The UUID of the network")
    net_subs.add_parser("refs", help="Retrieve references to a specific network.").add_argument("id", help="The UUID of the network")

    network_payload_help = (
        "A valid JSON string mapping to the network schema.\n"
        "IMPORTANT: When updating, strip read-only fields like 'id', 'metadata', and 'default'.\n\n"
        "Example (Gateway Managed Network):\n"
        "  '{\n"
        "    \"name\": \"Guest\",\n"
        "    \"management\": \"GATEWAY\",\n"
        "    \"enabled\": true,\n"
        "    \"vlanId\": 30,\n"
        "    \"isolationEnabled\": true,\n"
        "    \"ipv4Configuration\": {\n"
        "      \"hostIpAddress\": \"192.168.30.1\",\n"
        "      \"prefixLength\": 24,\n"
        "      \"dhcpConfiguration\": {\n"
        "        \"mode\": \"SERVER\",\n"
        "        \"ipAddressRange\": {\"start\": \"192.168.30.2\", \"stop\": \"192.168.30.254\"},\n"
        "        \"leaseTimeSeconds\": 28800\n"
        "      }\n"
        "    }\n"
        "  }'\n"
    )
    create_p = net_subs.add_parser("create", help="Create a new network on a site.", formatter_class=argparse.RawTextHelpFormatter)
    create_p.add_argument("payload", help=network_payload_help)

    update_p = net_subs.add_parser("update", help="Update an existing network on a site.", formatter_class=argparse.RawTextHelpFormatter)
    update_p.add_argument("id", help="The UUID of the network to update")
    update_p.add_argument("payload", help=network_payload_help)

    delete_p = net_subs.add_parser("delete", help="Delete an existing network on a site.")
    delete_p.add_argument("id", help="The UUID of the network to delete")
    delete_p.add_argument("--force", action="store_true", help="Force deletion of the network")

    # --- Resource ---
    res_parser = subparsers.add_parser("resource", help="Manage supporting network resources (VPN, DPI, WAN, etc.)")
    res_subs = res_parser.add_subparsers(dest="resource_command", required=True)

    for cmd, hlp in [
        ("wans", "Returns available WAN interface definitions for a given site."),
        ("vpn-tunnels", "List Site-To-Site VPN Tunnels."),
        ("vpn-servers", "List VPN Servers."),
        ("radius", "List Radius Profiles."),
        ("tags", "List Device Tags."),
        ("dpi-categories", "List DPI Application Categories."),
        ("dpi-apps", "List DPI Applications."),
        ("countries", "Returns ISO-standard country codes and names."),
    ]:
        res_subs.add_parser(cmd, help=hlp).add_argument("--limit", type=int, default=50, help="Maximum to fetch")

    # --- Site ---
    site_parser = subparsers.add_parser("site", help="List sites", formatter_class=argparse.RawTextHelpFormatter)
    site_subs = site_parser.add_subparsers(dest="site_command", required=True)
    list_s_p = site_subs.add_parser("list", help="List sites")
    list_s_p.add_argument("--limit", type=int, default=50, help="Maximum number of sites to fetch")

    # --- Traffic ---
    traffic_parser = subparsers.add_parser("traffic", help="Manage traffic matching lists", formatter_class=argparse.RawTextHelpFormatter)
    traffic_subs = traffic_parser.add_subparsers(dest="traffic_command", required=True)

    list_t_p = traffic_subs.add_parser("list", help="Retrieve all traffic matching lists on a site.")
    list_t_p.add_argument("--limit", type=int, default=50, help="Maximum number of lists to fetch.")

    traffic_subs.add_parser("get", help="Retrieve details for a specific traffic matching list.").add_argument("id", help="The UUID of the traffic matching list.")

    traffic_payload_help = (
        "A valid JSON string mapping to the traffic matching list schema.\n\n"
        "Schema Reference:\n"
        "  {\n"
        "    \"type\": \"<PORTS|IPV4_ADDRESSES|IPV6_ADDRESSES>\",\n"
        "    \"name\": \"<string>\",\n"
        "    \"items\": [\n"
        "      {\"type\": \"<PORT_NUMBER|PORT_NUMBER_RANGE|IPV4_ADDRESS>\", \"value\": \"<string>\"}\n"
        "    ]\n"
        "  }\n\n"
        "Example:\n"
        "  '{\"type\": \"IP_ADDRESS\", \"name\": \"Blocklist\","
        " \"items\": [{\"type\": \"IPV4_ADDRESS\", \"value\": \"1.1.1.1\"}]}'\n"
    )
    create_t_p = traffic_subs.add_parser("create", help="Create Traffic Matching List.", formatter_class=argparse.RawTextHelpFormatter)
    create_t_p.add_argument("payload", help=traffic_payload_help)

    update_t_p = traffic_subs.add_parser("update", help="Update Traffic Matching List.", formatter_class=argparse.RawTextHelpFormatter)
    update_t_p.add_argument("id", help="The UUID of the traffic matching list to update.")
    update_t_p.add_argument("payload", help=traffic_payload_help)

    traffic_subs.add_parser("delete", help="Delete Traffic Matching List.").add_argument("id", help="The UUID of the traffic matching list to delete.")

    # --- Device ---
    device_parser = subparsers.add_parser("device", help="Manage UniFi devices (APs, Switches, Gateways).")
    device_subs = device_parser.add_subparsers(dest="device_command", required=True)

    device_subs.add_parser("pending", help="Retrieve devices pending adoption.")

    list_dev_p = device_subs.add_parser("list", help="Retrieve a list of all adopted devices on a site.")
    list_dev_p.add_argument("--limit", type=int, default=25, help="Maximum number of devices to fetch")

    device_subs.add_parser("get", help="Retrieve detailed information about a specific adopted device.").add_argument("id", help="The UUID of the device.")
    device_subs.add_parser("stats", help="Get latest statistics for a device.").add_argument("id", help="The UUID of the device.")
    device_subs.add_parser("decommission", help="Removes (unadopts) an adopted device from the site.").add_argument("id", help="The UUID of the device.")

    adopt_p = device_subs.add_parser("adopt", help="Adopt a device to a site.")
    adopt_p.add_argument("mac", help="MAC address of the device to adopt.")
    adopt_p.add_argument("--name", help="Optional name to assign to the device.")

    action_p = device_subs.add_parser("action", help="Perform an action on a specific adopted device (e.g., RESTART, UPGRADE).")
    action_p.add_argument("id", help="The UUID of the device.")
    action_p.add_argument("action", help="The action string to execute.")

    port_action_p = device_subs.add_parser("port-action", help="Perform an action on a specific device port (e.g., POWER_CYCLE).")
    port_action_p.add_argument("id", help="The UUID of the device (switch).")
    port_action_p.add_argument("port_idx", type=int, help="The index of the port (usually 1-based).")
    port_action_p.add_argument("action", help="The action string to execute.")

    # --- WiFi ---
    wifi_parser = subparsers.add_parser("wifi", help="Manage Wi-Fi broadcasts (SSIDs)", formatter_class=argparse.RawTextHelpFormatter)
    wifi_subs = wifi_parser.add_subparsers(dest="wifi_command", required=True)

    list_w_p = wifi_subs.add_parser("list", help="List Wi-Fi broadcasts")
    list_w_p.add_argument("--limit", type=int, default=50, help="Maximum number of broadcasts to fetch")

    wifi_subs.add_parser("get", help="Fetch details for a specific Wi-Fi broadcast").add_argument("id", help="The UUID of the Wi-Fi broadcast")

    wifi_payload_help = (
        "A valid JSON string mapping to Wi-Fi schema.\n\n"
        "Example:\n"
        "  '{\"type\": \"STANDARD\", \"name\": \"Guest WiFi\", \"enabled\": true,"
        " \"securityConfiguration\": {\"type\": \"WPA2_PERSONAL\", \"passphrase\": \"secret123\"},"
        " \"clientIsolationEnabled\": true}'\n"
    )
    create_w_p = wifi_subs.add_parser("create", help="Create a new Wifi Broadcast.", formatter_class=argparse.RawTextHelpFormatter)
    create_w_p.add_argument("payload", help=wifi_payload_help)

    update_w_p = wifi_subs.add_parser("update", help="Update an existing Wifi Broadcast.", formatter_class=argparse.RawTextHelpFormatter)
    update_w_p.add_argument("id", help="The UUID of the Wi-Fi broadcast to update.")
    update_w_p.add_argument("payload", help=wifi_payload_help)

    delete_w_p = wifi_subs.add_parser("delete", help="Delete an existing Wifi Broadcast.")
    delete_w_p.add_argument("id", help="The UUID of the Wi-Fi broadcast to delete.")
    delete_w_p.add_argument("--force", action="store_true", help="Force deletion of the broadcast.")

    # --- Hotspot ---
    hotspot_parser = subparsers.add_parser("hotspot", help="Manage Hotspot vouchers.")
    hotspot_subs = hotspot_parser.add_subparsers(dest="hotspot_command", required=True)

    list_h_p = hotspot_subs.add_parser("list", help="List Hotspot vouchers.")
    list_h_p.add_argument("--limit", type=int, default=100, help="Maximum number of vouchers to fetch.")
    list_h_p.add_argument("--filter", dest="filter_", help="Filter string (e.g. by voucher name/note).")

    hotspot_subs.add_parser("get", help="Get details for a specific voucher.").add_argument(
        "id", help="UUID of the voucher."
    )

    create_h_p = hotspot_subs.add_parser("create", help="Create one or more Hotspot vouchers.")
    create_h_p.add_argument("--name", required=True, help="Note/label applied to all generated vouchers.")
    create_h_p.add_argument("--minutes", type=int, required=True, help="Access duration in minutes (e.g. 1440 = 24h).")
    create_h_p.add_argument("--count", type=int, default=1, help="Number of vouchers to generate (default: 1).")
    create_h_p.add_argument("--guest-limit", type=int, help="Max guests that may share one voucher.")
    create_h_p.add_argument("--data-limit", type=int, help="Data usage cap in megabytes.")
    create_h_p.add_argument("--rx-limit", type=int, help="Download rate limit in kbps.")
    create_h_p.add_argument("--tx-limit", type=int, help="Upload rate limit in kbps.")

    hotspot_subs.add_parser("delete", help="Delete a single voucher by UUID.").add_argument(
        "id", help="UUID of the voucher to delete."
    )

    delete_all_h_p = hotspot_subs.add_parser("delete-all", help="Bulk-delete vouchers matching a filter string.")
    delete_all_h_p.add_argument("--filter", dest="filter_", required=True, help="Filter string to match vouchers.")

    # --- Switching ---
    switching_parser = subparsers.add_parser("switching", help="View switching infrastructure (LAGs, stacks, MC-LAG).")
    switching_subs = switching_parser.add_subparsers(dest="switching_command", required=True)

    for cmd, hlp in [
        ("lags", "List Link Aggregation Groups (LAGs)."),
        ("stacks", "List switch stacks."),
        ("mclags", "List Multi-Chassis LAG domains."),
    ]:
        switching_subs.add_parser(cmd, help=hlp).add_argument(
            "--limit", type=int, default=25, help="Maximum number to fetch."
        )

    switching_subs.add_parser("lag", help="Get details for a specific LAG.").add_argument(
        "id", help="UUID of the LAG."
    )
    switching_subs.add_parser("stack", help="Get details for a specific switch stack.").add_argument(
        "id", help="UUID of the switch stack."
    )
    switching_subs.add_parser("mclag", help="Get details for a specific MC-LAG domain.").add_argument(
        "id", help="UUID of the MC-LAG domain."
    )

    return parser
