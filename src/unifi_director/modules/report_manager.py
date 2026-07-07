"""Full-site report collector — aggregates all API domains into a single JSON document."""

__version__ = "1.0.0"

import datetime
import json
import logging
import sys
from typing import Any

from ..api_client.client import Client
from ..registry import REGISTRY
from .version_manager import SPEC_BUILT_ON, get_controller_version, fetch_latest_known_version

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Manual checklist — items that cannot be assessed from the API
# ---------------------------------------------------------------------------

MANUAL_CHECKLIST = [
    # --- Admin Access ---
    {
        "id": "AC-01",
        "category": "Admin Access",
        "priority": "High",
        "check": "Enable Multi-Factor Authentication (MFA) for every admin account.",
        "location": "Settings → Admins & Users → [each user] → Security",
        "nist_csf": "PR.AC-1",
    },
    {
        "id": "AC-02",
        "category": "Admin Access",
        "priority": "High",
        "check": "Remove or disable any shared or unused admin accounts.",
        "location": "Settings → Admins & Users",
        "nist_csf": "PR.AC-1",
    },
    {
        "id": "AC-03",
        "category": "Admin Access",
        "priority": "High",
        "check": "Assign least-privilege roles — avoid granting Super Admin unless required.",
        "location": "Settings → Admins & Users → [each user] → Role",
        "nist_csf": "PR.AC-4",
    },
    {
        "id": "AC-04",
        "category": "Admin Access",
        "priority": "Medium",
        "check": "Restrict UI access to a management VLAN or specific source IP ranges only.",
        "location": "Settings → System → Administration → Access Control",
        "nist_csf": "PR.AC-5",
    },
    {
        "id": "AC-05",
        "category": "Admin Access",
        "priority": "Medium",
        "check": "Disable or restrict UniFi Cloud remote access — use VPN for remote management instead.",
        "location": "Settings → System → Remote Access",
        "nist_csf": "PR.AC-3",
    },

    # --- Device Firmware ---
    {
        "id": "DP-01",
        "category": "Device Firmware",
        "priority": "High",
        "check": "Verify all adopted devices (APs, switches, gateways) are running current firmware.",
        "location": "UniFi Devices → [each device] → Settings → Firmware",
        "nist_csf": "PR.IP-12",
    },
    {
        "id": "DP-02",
        "category": "Device Firmware",
        "priority": "Medium",
        "check": "Enable automatic firmware updates or document a recurring manual update schedule.",
        "location": "Settings → System → Updates",
        "nist_csf": "PR.IP-12",
    },
    {
        "id": "DP-03",
        "category": "Device Firmware",
        "priority": "High",
        "check": "Verify the UniFi Network Application (controller) itself is up to date.",
        "location": "Settings → System → Updates (or use 'unifi-director version')",
        "nist_csf": "PR.IP-12",
    },

    # --- Device Authentication ---
    {
        "id": "DA-01",
        "category": "Device Authentication",
        "priority": "High",
        "check": "Change default SSH device credentials and disable SSH on devices that do not require it.",
        "location": "Settings → System → Device Authentication",
        "nist_csf": "PR.AC-1",
    },
    {
        "id": "DA-02",
        "category": "Device Authentication",
        "priority": "Medium",
        "check": "If SSH is required, configure key-based authentication and disable password login.",
        "location": "Settings → System → Device Authentication → SSH Keys",
        "nist_csf": "PR.AC-1",
    },

    # --- Threat Management ---
    {
        "id": "TM-01",
        "category": "Threat Management",
        "priority": "High",
        "check": "Enable Intrusion Detection/Prevention (IDS/IPS) on all WAN interfaces if licensed.",
        "location": "Security → Threat Management → IDS/IPS",
        "nist_csf": "DE.CM-1",
    },
    {
        "id": "TM-02",
        "category": "Threat Management",
        "priority": "High",
        "check": "Enable DNS filtering / content filtering, especially on guest and IoT networks.",
        "location": "Security → Threat Management → Content Filtering",
        "nist_csf": "PR.PT-3",
    },
    {
        "id": "TM-03",
        "category": "Threat Management",
        "priority": "Medium",
        "check": "Review Threat Management dashboard for any active or historical alerts.",
        "location": "Security → Threat Management → Overview",
        "nist_csf": "DE.CM-1",
    },
    {
        "id": "TM-04",
        "category": "Threat Management",
        "priority": "Medium",
        "check": "Enable DPI (Deep Packet Inspection) to gain visibility into application traffic.",
        "location": "Settings → Site → Services → Deep Packet Inspection",
        "nist_csf": "DE.CM-1",
    },

    # --- Logging & Monitoring ---
    {
        "id": "LM-01",
        "category": "Logging & Monitoring",
        "priority": "High",
        "check": "Configure remote syslog to a SIEM or central log server.",
        "location": "Settings → System → Logging → Remote Syslog",
        "nist_csf": "DE.CM-7",
    },
    {
        "id": "LM-02",
        "category": "Logging & Monitoring",
        "priority": "Medium",
        "check": "Enable email or webhook alerts for critical events (admin login, device offline, WAN failover).",
        "location": "Settings → Notifications",
        "nist_csf": "DE.AE-5",
    },
    {
        "id": "LM-03",
        "category": "Logging & Monitoring",
        "priority": "Medium",
        "check": "Verify that firewall and IDS logs are being captured and retained for at least 90 days.",
        "location": "Settings → System → Logging",
        "nist_csf": "PR.PT-1",
    },

    # --- Backup & Recovery ---
    {
        "id": "BR-01",
        "category": "Backup & Recovery",
        "priority": "High",
        "check": "Enable automatic backups and verify backup files are stored off-device.",
        "location": "Settings → System → Backups",
        "nist_csf": "RC.RP-1",
    },
    {
        "id": "BR-02",
        "category": "Backup & Recovery",
        "priority": "Medium",
        "check": "Test the restore process at least once to confirm backups are valid.",
        "location": "Settings → System → Backups → Restore",
        "nist_csf": "RC.RP-1",
    },

    # --- Switch Port Security ---
    {
        "id": "SP-01",
        "category": "Switch Port Security",
        "priority": "Medium",
        "check": "Disable unused switch ports.",
        "location": "UniFi Devices → [switch] → Ports → [unused port] → Disabled",
        "nist_csf": "PR.AC-5",
    },
    {
        "id": "SP-02",
        "category": "Switch Port Security",
        "priority": "Medium",
        "check": "Enable storm control on access-layer switch ports to prevent broadcast storms.",
        "location": "UniFi Devices → [switch] → Ports → [port] → Storm Control",
        "nist_csf": "PR.PT-4",
    },
    {
        "id": "SP-03",
        "category": "Switch Port Security",
        "priority": "Medium",
        "check": "Apply 802.1X port-based authentication on wired access ports where applicable.",
        "location": "Settings → Profiles → Switch Ports → 802.1X Control",
        "nist_csf": "PR.AC-1",
    },
    {
        "id": "SP-04",
        "category": "Switch Port Security",
        "priority": "Low",
        "check": "Enable port isolation on switch ports serving guest or IoT devices.",
        "location": "UniFi Devices → [switch] → Ports → [port] → Port Isolation",
        "nist_csf": "PR.AC-5",
    },

    # --- Management Plane ---
    {
        "id": "MP-01",
        "category": "Management Plane",
        "priority": "High",
        "check": "Ensure the UniFi controller is on a dedicated management VLAN, not accessible from guest or IoT VLANs.",
        "location": "Verify via firewall rules — management VLAN should block inbound from untrusted VLANs.",
        "nist_csf": "PR.AC-5",
    },
    {
        "id": "MP-02",
        "category": "Management Plane",
        "priority": "Medium",
        "check": "Disable SNMP if not actively used. If required, use SNMPv3 with auth and encryption.",
        "location": "Settings → System → SNMP",
        "nist_csf": "PR.PT-3",
    },
    {
        "id": "MP-03",
        "category": "Management Plane",
        "priority": "Medium",
        "check": "Replace the self-signed SSL certificate with a valid certificate (e.g., Let's Encrypt).",
        "location": "Settings → System → SSL Certificate",
        "nist_csf": "PR.DS-2",
    },

    # --- Guest & IoT Networks ---
    {
        "id": "GI-01",
        "category": "Guest & IoT Networks",
        "priority": "High",
        "check": "Confirm client isolation is enabled on all guest SSIDs.",
        "location": "Settings → WiFi → [guest SSID] → Advanced → Client Device Isolation",
        "nist_csf": "PR.AC-5",
    },
    {
        "id": "GI-02",
        "category": "Guest & IoT Networks",
        "priority": "Medium",
        "check": "Apply bandwidth limits on guest networks to prevent abuse.",
        "location": "Settings → WiFi → [guest SSID] → Advanced → Rate Limiting",
        "nist_csf": "PR.PT-4",
    },
    {
        "id": "GI-03",
        "category": "Guest & IoT Networks",
        "priority": "High",
        "check": "Verify IoT devices are on a dedicated VLAN with firewall rules blocking access to LAN and management.",
        "location": "Settings → Networks → [IoT VLAN] + Security → Firewall",
        "nist_csf": "PR.AC-5",
    },
    {
        "id": "GI-04",
        "category": "Guest & IoT Networks",
        "priority": "Medium",
        "check": "Block guest and IoT VLANs from reaching the UniFi controller management port (TCP 443/8443).",
        "location": "Security → Firewall → LAN In rules",
        "nist_csf": "PR.AC-5",
    },
]

# WHY: Limit for paginated collections in report mode is higher than individual
# commands so the report captures the full site state, not a truncated sample.
_DEFAULT_LIMIT = 500


def _to_dict(obj: Any) -> Any:
    if obj is None:
        return None
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    if isinstance(obj, list):
        return [_to_dict(i) for i in obj]
    return obj


def _collect(label: str, fn, *args, **kwargs) -> dict:
    """Run a collection function, return {data, error} dict. Never raises."""
    try:
        result = fn(*args, **kwargs)
        items = list(result) if hasattr(result, "__iter__") and not isinstance(result, (dict, str)) else result
        return {"data": _to_dict(items), "count": len(items) if isinstance(items, list) else None, "error": None}
    except Exception as e:
        logger.warning(f"Report section '{label}' failed: {e}")
        return {"data": None, "count": None, "error": str(e)}


def build_report(client: Client, limit: int = _DEFAULT_LIMIT) -> dict:
    from .system_info_manager import UnifiInfoManager
    from .site_manager import UnifiSiteManager
    from .network_manager import UnifiNetworkManager
    from .device_manager import UnifiDeviceManager
    from .client_manager import UnifiClientManager
    from .wifi_manager import UnifiWifiManager
    from .firewall_manager import UnifiFirewallManager
    from .acl_manager import UnifiAclManager
    from .dns_manager import UnifiDnsManager
    from .traffic_matching_manager import UnifiTrafficMatchingManager
    from .resource_manager import UnifiResourceManager
    from .hotspot_manager import UnifiHotspotManager
    from .switching_manager import UnifiSwitchingManager

    site_id = REGISTRY.SITE_ID

    info_mgr     = UnifiInfoManager(client=client)
    site_mgr     = UnifiSiteManager(client=client)
    net_mgr      = UnifiNetworkManager(client=client, site_id=site_id)
    dev_mgr      = UnifiDeviceManager(client=client, site_id=site_id)
    client_mgr   = UnifiClientManager(client=client, site_id=site_id)
    wifi_mgr     = UnifiWifiManager(client=client, site_id=site_id)
    fw_mgr       = UnifiFirewallManager(client=client, site_id=site_id)
    acl_mgr      = UnifiAclManager(client=client, site_id=site_id)
    dns_mgr      = UnifiDnsManager(client=client, site_id=site_id)
    traffic_mgr  = UnifiTrafficMatchingManager(client=client, site_id=site_id)
    res_mgr      = UnifiResourceManager(client=client, site_id=site_id)
    hotspot_mgr  = UnifiHotspotManager(client=client)
    switch_mgr   = UnifiSwitchingManager(client=client)

    def _p(label: str) -> None:
        print(f"  Collecting {label}...", file=sys.stderr)

    _p("system info")
    system_info = _collect("system_info", info_mgr.get_system_info)
    _p("sites")
    sites = _collect("sites", lambda: list(site_mgr.iter_sites(limit=limit)))
    _p("networks")
    networks = _collect("networks", lambda: list(net_mgr.iter_networks(limit=limit)))
    _p("devices")
    devices = _collect("devices", lambda: list(dev_mgr.iter_adopted(limit=limit)))
    _p("pending devices")
    pending = _collect("pending_devices", dev_mgr.list_pending)
    _p("clients")
    clients = _collect("clients", lambda: list(client_mgr.iter_clients(limit=limit)))
    _p("WiFi broadcasts")
    wifi = _collect("wifi", lambda: list(wifi_mgr.iter_broadcasts(limit=limit)))
    _p("firewall zones")
    fw_zones = _collect("firewall_zones", lambda: fw_mgr.list_zones(limit=limit, exclude_system=False))
    _p("firewall policies")
    fw_policies = _collect("firewall_policies", lambda: fw_mgr.list_policies(limit=limit, exclude_system=False))
    _p("ACL rules")
    acl_rules = _collect("acl_rules", lambda: list(acl_mgr.iter_rules(limit=limit)))
    _p("DNS policies")
    dns = _collect("dns_policies", lambda: list(dns_mgr.list_policies(limit=limit)))
    _p("traffic lists")
    traffic = _collect("traffic_lists", lambda: list(traffic_mgr.iter_matching_lists(limit=limit)))
    _p("WANs")
    wans = _collect("wans", res_mgr.list_wans)
    _p("VPN tunnels")
    vpn_t = _collect("vpn_tunnels", lambda: list(res_mgr.iter_vpn_tunnels(limit=limit)))
    _p("VPN servers")
    vpn_s = _collect("vpn_servers", lambda: list(res_mgr.iter_vpn_servers(limit=limit)))
    _p("RADIUS profiles")
    radius = _collect("radius", lambda: list(res_mgr.iter_radius_profiles(limit=limit)))
    _p("device tags")
    tags = _collect("tags", lambda: list(res_mgr.iter_device_tags(limit=limit)))
    _p("DPI categories")
    dpi_cats = _collect("dpi_categories", res_mgr.list_dpi_categories)
    _p("DPI apps")
    dpi_apps = _collect("dpi_apps", lambda: list(res_mgr.iter_dpi_apps(limit=limit)))
    _p("hotspot vouchers")
    vouchers = _collect("vouchers", lambda: hotspot_mgr.list_vouchers(limit=limit))
    _p("LAGs")
    lags = _collect("lags", lambda: switch_mgr.list_lags(limit=limit))
    _p("switch stacks")
    stacks = _collect("stacks", lambda: switch_mgr.list_stacks(limit=limit))
    _p("MC-LAG domains")
    mclags = _collect("mclags", lambda: switch_mgr.list_mc_lag_domains(limit=limit))
    _p("controller version")
    ctrl_ver = get_controller_version(client)
    _p("latest spec")
    latest = fetch_latest_known_version()

    return {
        "meta": {
            "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
            "console": REGISTRY.CONSOLE_NAME or "default",
            "host": REGISTRY.CONSOLE_ID or REGISTRY.HOST,
            "site_id": REGISTRY.SITE_ID_RAW,
            "controller_version": ctrl_ver,
            "unifi_director_spec": SPEC_BUILT_ON,
            "latest_spec_available": latest,
        },
        "system_info": system_info,
        "sites": sites,
        "networks": networks,
        "devices": {
            "adopted": devices,
            "pending": pending,
        },
        "clients": clients,
        "wifi": wifi,
        "firewall": {
            "zones": fw_zones,
            "policies": fw_policies,
        },
        "acl_rules": acl_rules,
        "dns_policies": dns,
        "traffic_lists": traffic,
        "resources": {
            "wans": wans,
            "vpn_tunnels": vpn_t,
            "vpn_servers": vpn_s,
            "radius_profiles": radius,
            "device_tags": tags,
            "dpi_categories": dpi_cats,
            "dpi_apps": dpi_apps,
        },
        "hotspot": {
            "vouchers": vouchers,
        },
        "switching": {
            "lags": lags,
            "stacks": stacks,
            "mc_lag_domains": mclags,
        },
        "manual_checklist": MANUAL_CHECKLIST,
    }


def default_filename(console_name: str) -> str:
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_name = console_name.replace(" ", "_").replace("/", "-")
    return f"unifi-director-report-{safe_name}-{ts}.json"
