# UniFi Director — Reference Documentation

UniFi Director is a Python CLI for managing UniFi Network Applications via the
official Integration HTTP API. It targets Python 3.11–3.13 and runs headless on
a Raspberry Pi 5 or any Linux/macOS host.

---

## Table of Contents

1. [What it does](#what-it-does)
2. [Architecture](#architecture)
3. [Prerequisites](#prerequisites)
4. [Installation on Raspberry Pi 5](#installation-on-raspberry-pi-5)
5. [Configuration — inventory.json](#configuration--inventoryjson)
6. [Environment variables](#environment-variables)
7. [Global flags](#global-flags)
8. [Commands](#commands)
   - [report](#report), [version](#version), [inventory](#inventory), [cloud](#cloud), [audit](#audit), [site](#site)
   - [network](#network), [device](#device), [wifi](#wifi), [client](#client)
   - [firewall](#firewall), [acl](#acl), [dns](#dns), [traffic](#traffic), [resource](#resource)
   - [hotspot](#hotspot), [switching](#switching)
9. [Security notes](#security-notes)
10. [Troubleshooting](#troubleshooting)

---

## What it does

UniFi Director wraps the UniFi Network Application Integration API (introduced
in UniFi Network 8.x). It lets you read and manage networks, VLANs, firewall
zones, ACL rules, DNS policies, connected clients, adopted devices, Wi-Fi
broadcasts, traffic matching lists, and supporting resources from a terminal.

All network changes are real and take effect immediately. There is no dry-run
flag — treat write operations with care.

---

## Architecture

### Two routing modes

UniFi Director selects a routing mode automatically based on whether a
`console_id` is present for the active console profile:

| Mode | When | Base URL |
|------|------|----------|
| **Direct local** | `console_id` is absent | `https://<host>/proxy/network/integration` |
| **Cloud proxy** | `console_id` is present | `https://api.ui.com/v1/connector/consoles/<console_id>/proxy/network/integration` |

Direct local connects to the controller on your LAN. Cloud proxy routes through
Ubiquiti's `api.ui.com` relay — useful when the Pi cannot reach the controller
directly.

### Generated API client

The internal HTTP client was generated from the UniFi Network OpenAPI spec
version `10.5.54`. It is compatible with controllers running 8.x through 10.x.
The client uses `httpx` for transport and `attrs` for data models.

---

## Prerequisites

| Requirement | Notes |
|-------------|-------|
| Python 3.11, 3.12, or 3.13 | Debian Trixie ships 3.11 by default |
| Network access to the controller | Required for direct local mode |
| UniFi API key | Generated in the UniFi Network UI under **Settings → Control Plane → Integrations** |
| Site ID (UUID) | Found in the UniFi Network UI URL or via `unifi-director site list` |

---

## Installation on Raspberry Pi 5

### Step 1 — Copy the project to the Pi

From your workstation, transfer the project directory to the Pi. Replace the
path and user as appropriate:

```bash
rsync -av --exclude='.venv' --exclude='__pycache__' --exclude='inventory.json' \
    /path/to/UnifiDirector/ pi@<PI_IP>:/home/pi/unifi-director/
```

`inventory.json` is excluded intentionally — it contains credentials and should
never leave your local machine unencrypted. See [Configuration](#configuration--inventoryjson).

### Step 2 — Run setup.sh

SSH into the Pi and run the installer from the project directory:

```bash
ssh pi@<PI_IP>
cd /home/pi/unifi-director
chmod +x setup.sh
sudo ./setup.sh        # sudo creates /usr/local/bin/unifi-director system-wide
```

Without `sudo` the command is available via `.venv/bin/unifi-director` only.

### Step 3 — Configure inventory.json

The installer copies `inventory.json.example` to `inventory.json` if no
credentials file exists. Edit it:

```bash
nano /home/pi/unifi-director/inventory.json
```

See [Configuration](#configuration--inventoryjson) for the full format.

### Step 4 — Verify

```bash
unifi-director --help
unifi-director inventory
unifi-director audit --limit 5
```

### Updating

To push new code without re-installing:

```bash
# From workstation
rsync -av --exclude='.venv' --exclude='__pycache__' --exclude='inventory.json' \
    /path/to/UnifiDirector/ pi@<PI_IP>:/home/pi/unifi-director/

# No re-install needed — the editable install picks up src/ changes automatically.
```

If `pyproject.toml` dependencies changed, re-run `setup.sh`.

---

## Configuration — inventory.json

`inventory.json` lives in the directory you run `unifi-director` from (the
working directory). It is never committed to git.

### Full schema

```json
{
  "cloud": {
    "host": "api.ui.com",
    "api_key": "<your-ui.com-cloud-api-key>"
  },
  "consoles": {
    "<profile-name>": {
      "host": "<controller-hostname-or-ip>",
      "api_key": "<local-api-key>",
      "site_id": "<site-uuid>",
      "console_id": "<cloud-console-id>"
    }
  }
}
```

### Field reference

| Field | Required | Notes |
|-------|----------|-------|
| `cloud.host` | No | Defaults to `api.ui.com`. Override only if using a private relay. |
| `cloud.api_key` | Only for cloud proxy mode | Your Ubiquiti account API key. |
| `consoles.<name>.host` | Yes for direct local | IP or hostname of the controller. |
| `consoles.<name>.api_key` | Yes for direct local | Local integration API key. |
| `consoles.<name>.site_id` | Yes (always) | UUID of the target site. |
| `consoles.<name>.console_id` | Only for cloud proxy | Cloud Console ID from `api.ui.com`. |

### Console routing rules

- If `console_id` is **absent**: connects directly to `host` using `api_key`.
- If `console_id` is **present**: routes through `api.ui.com` using `cloud.api_key`. The `host` and `api_key` fields are ignored.

### Multiple console profiles

```json
{
  "cloud": { "api_key": "uicloud-key-here" },
  "consoles": {
    "default": {
      "host": "192.168.1.1",
      "api_key": "local-key-for-home",
      "site_id": "aaaaaaaa-0000-0000-0000-000000000001"
    },
    "office": {
      "console_id": "cloud-id-for-office-controller",
      "site_id": "bbbbbbbb-0000-0000-0000-000000000002"
    },
    "remote-site": {
      "host": "vpn-controller.example.com",
      "api_key": "remote-key",
      "site_id": "cccccccc-0000-0000-0000-000000000003"
    }
  }
}
```

Switch between profiles at runtime with `-c / --console`:

```bash
unifi-director -c office network list
unifi-director -c remote-site device list
```

If `-c` is omitted, the `default` profile is used.

### Finding your site_id

```bash
unifi-director site list
```

The UUID in the `id` column is your `site_id`.

---

## Environment variables

All fields in `inventory.json` can be overridden per-invocation with environment
variables. Variables take precedence over the file.

| Variable | Overrides |
|----------|-----------|
| `UNIFI_HOST` | `consoles.<name>.host` |
| `UNIFI_API_KEY` | `consoles.<name>.api_key` |
| `UNIFI_CLOUD_HOST` | `cloud.host` |
| `UNIFI_CLOUD_API_KEY` | `cloud.api_key` |
| `UNIFI_SITE_ID` | `consoles.<name>.site_id` |
| `UNIFI_VERIFY_SSL` | SSL verification (`true`/`1`/`yes` to enable) |
| `UNIFI_DEBUG` | Debug logging (`true`/`1`/`yes` to enable) |

SSL verification is **off by default** because local UniFi controllers use
self-signed certificates. Set `UNIFI_VERIFY_SSL=true` only if your controller
has a valid certificate chain.

---

## Global flags

These flags apply to every command and must appear before the subcommand:

```
-c, --console <name>   Target console profile from inventory.json (default: "default")
    --site <uuid>      Override the site UUID for this invocation only
    --json             Print raw JSON instead of formatted human-readable output
    --debug            Enable verbose HTTP logging (shows requests, headers, timing)
```

Examples:

```bash
unifi-director --debug network list
unifi-director --json device list | jq '.[].id'
unifi-director -c office --site <uuid> wifi list
```

---

## Commands

### `inventory`

List all console profiles configured in `inventory.json`. Does not connect to any controller.

```bash
unifi-director inventory
```

---

### `report`

Collects full site data across all API domains in a single pass and writes a
structured JSON file. Designed for offline analysis, security audits, and
AI-assisted review against frameworks like NIST CSF.

```bash
# Write to auto-named file in current directory
unifi-director report

# Write to a specific file
unifi-director report --out /path/to/output.json

# Print JSON to stdout (e.g. for piping)
unifi-director report --stdout

# Adjust collection limit (default: 500 per domain)
unifi-director report --limit 1000
```

**Output filename** (auto-named): `unifi-director-report-<console>-<YYYY-MM-DD_HH-MM-SS>.json`

**Report structure:**

```
meta                   — console, host, site_id, timestamps, spec versions
system_info            — UniFi Network Application info
sites                  — all sites on the console
networks               — all VLANs and networks
devices.adopted        — all adopted devices
devices.pending        — devices awaiting adoption
clients                — connected clients
wifi                   — all Wi-Fi broadcasts (SSIDs)
firewall.zones         — firewall zones
firewall.policies      — firewall policies (including system defaults)
acl_rules              — Access Control List rules
dns_policies           — local DNS overrides
traffic_lists          — traffic matching lists
resources.wans         — WAN interfaces
resources.vpn_tunnels  — site-to-site VPN tunnels
resources.vpn_servers  — VPN servers
resources.radius_profiles — RADIUS profiles
resources.device_tags  — device tags
resources.dpi_categories  — DPI application categories
resources.dpi_apps     — DPI applications
hotspot.vouchers       — Hotspot vouchers
switching.lags         — Link Aggregation Groups
switching.stacks       — switch stacks
switching.mc_lag_domains — MC-LAG domains
```

Each section includes a `count` field and an `error` field (null on success).
A failed section does not abort the report — the remaining sections continue.

The report also includes a `manual_checklist` array — 30 items across 9
categories covering settings that cannot be read from the API. Each item has:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier (e.g. `AC-01`) |
| `category` | Grouping (e.g. `Admin Access`, `Threat Management`) |
| `priority` | `High`, `Medium`, or `Low` |
| `check` | What to verify |
| `location` | Exact path in the UniFi Network UI |
| `nist_csf` | Relevant NIST CSF control reference |

**Checklist categories:**

| Category | Items | Focus |
|----------|-------|-------|
| Admin Access | 5 | MFA, account hygiene, role least-privilege, management access restrictions |
| Device Firmware | 3 | Per-device firmware currency, auto-update policy |
| Device Authentication | 2 | SSH hardening, default credentials |
| Threat Management | 4 | IDS/IPS, DNS filtering, DPI |
| Logging & Monitoring | 3 | Remote syslog, alerting, log retention |
| Backup & Recovery | 2 | Backup schedule, restore test |
| Switch Port Security | 4 | Unused ports, storm control, 802.1X, port isolation |
| Management Plane | 3 | Management VLAN isolation, SNMP, SSL certificate |
| Guest & IoT Networks | 4 | Client isolation, bandwidth limits, VLAN firewall rules |

---

### `version`

Show the UniFi Network Application version running on the active controller and
compare it against the latest known release in the
[beezly/unifi-apis](https://github.com/beezly/unifi-apis) spec repository.

```bash
unifi-director version
unifi-director -c office version
unifi-director --json version
```

Example output:

```
[VERSION CHECK]
  Controller version   : v10.4.57
  Latest known version : v10.5.56  (source: github.com/beezly/unifi-apis)
  Status               : Update available
```

If the Pi has no internet access, the latest known version line reads
`Unavailable (could not reach GitHub)` and the command exits cleanly.

---

### `cloud`

Manage Global Site Manager telemetry via `api.ui.com`. Requires `cloud.api_key`.

```bash
unifi-director cloud hosts                 # list all registered consoles
unifi-director cloud isp-metrics           # 24-hour ISP health (latency, packet loss, speed)
```

---

### `audit`

Read-only comprehensive snapshot of the entire site: system info, sites,
devices, WANs, RADIUS profiles, networks, and Wi-Fi.

```bash
unifi-director audit                       # standard audit, up to 100 items per section
unifi-director audit --limit 25            # cap items per section
unifi-director audit --clients 5           # include up to 5 connected clients
unifi-director audit --detailed            # include extended detail fields
unifi-director audit --all                 # include system-defined default firewall policies
```

---

### `site`

```bash
unifi-director site list                   # list all sites on the console
unifi-director site list --limit 10
```

---

### `network`

Manage networks and VLANs.

```bash
unifi-director network list
unifi-director network get <uuid>
unifi-director network refs <uuid>         # show what references this network

unifi-director network create '{"name":"Guest","management":"GATEWAY","enabled":true,"vlanId":30,"ipv4Configuration":{"hostIpAddress":"192.168.30.1","prefixLength":24,"dhcpConfiguration":{"mode":"SERVER","ipAddressRange":{"start":"192.168.30.2","stop":"192.168.30.254"},"leaseTimeSeconds":28800}}}'

unifi-director network update <uuid> '{"name":"Guest-Renamed","vlanId":30}'

unifi-director network delete <uuid>
unifi-director network delete <uuid> --force
```

When updating a network, omit read-only fields (`id`, `metadata`, `default`).

---

### `device`

Manage adopted UniFi devices (APs, switches, gateways).

```bash
unifi-director device list
unifi-director device pending              # devices awaiting adoption
unifi-director device get <uuid>
unifi-director device stats <uuid>         # latest telemetry statistics
unifi-director device adopt <mac>          # adopt a pending device
unifi-director device adopt <mac> --name "Upstairs AP"
unifi-director device action <uuid> RESTART
unifi-director device action <uuid> UPGRADE
unifi-director device port-action <uuid> 3 POWER_CYCLE   # PoE port cycle on switch
unifi-director device decommission <uuid>  # unadopt a device
```

---

### `wifi`

Manage Wi-Fi broadcasts (SSIDs).

```bash
unifi-director wifi list
unifi-director wifi get <uuid>
unifi-director wifi create '{"type":"STANDARD","name":"Guest","enabled":true,"securityConfiguration":{"type":"WPA2_PERSONAL","passphrase":"changeme"},"clientIsolationEnabled":true}'
unifi-director wifi update <uuid> '{"name":"Guest-Updated"}'
unifi-director wifi delete <uuid>
unifi-director wifi delete <uuid> --force
```

---

### `client`

Manage connected clients.

```bash
unifi-director client list
unifi-director client list --limit 200
unifi-director client get <mac-or-uuid>
unifi-director client action <mac-or-uuid> RECONNECT
unifi-director client action <mac-or-uuid> BLOCK
unifi-director client action <mac-or-uuid> UNBLOCK
unifi-director client action <mac-or-uuid> AUTHORIZE
unifi-director client action <mac-or-uuid> UNAUTHORIZE
```

---

### `firewall`

Manage Zone-Based Firewall. Requires ZBF to be enabled on the controller. Returns an
informational message (no crash) if ZBF is not configured.

```bash
# Zones
unifi-director firewall list-zones
unifi-director firewall get-zone <uuid>
unifi-director firewall create-zone "DMZ" '["<network-uuid-1>","<network-uuid-2>"]'
unifi-director firewall update-zone <uuid> "DMZ-Renamed" '["<network-uuid>"]'
unifi-director firewall delete-zone <uuid>

# Policies
unifi-director firewall list-policies
unifi-director firewall list-policies --all        # include system defaults
unifi-director firewall list-policies --limit 50
unifi-director firewall get-policy <uuid>
unifi-director firewall create-policy '<json>'
unifi-director firewall update-policy <uuid> '<json>'
unifi-director firewall delete-policy <uuid>
unifi-director firewall toggle-policy <uuid> enable
unifi-director firewall toggle-policy <uuid> disable

# Policy ordering (within a zone pair)
unifi-director firewall get-order <source-zone-uuid> <dest-zone-uuid>
unifi-director firewall set-order <source-zone-uuid> <dest-zone-uuid> '["uuid-1","uuid-2"]'
```

---

### `acl`

Manage Access Control List rules.

```bash
unifi-director acl list
unifi-director acl get <uuid>
unifi-director acl create '{"type":"IPV4","enabled":true,"name":"Block DNS","action":"BLOCK","protocolFilter":["UDP"],"destinationFilter":{"type":"PORTS","portFilter":[53]}}'
unifi-director acl update <uuid> '<json>'
unifi-director acl delete <uuid>
unifi-director acl get-order
unifi-director acl set-order '["uuid-1","uuid-2","uuid-3"]'
```

---

### `dns`

Manage DNS policies (local DNS overrides / A records).

```bash
unifi-director dns list
unifi-director dns get <uuid>
unifi-director dns create '{"type":"A_RECORD","enabled":true,"domain":"pihole.lan","ipv4Address":"192.168.1.10","ttlSeconds":3600}'
unifi-director dns update <uuid> '<json>'
unifi-director dns delete <uuid>
```

---

### `traffic`

Manage traffic matching lists (used by firewall policies).

```bash
unifi-director traffic list
unifi-director traffic get <uuid>
unifi-director traffic create '{"type":"IPV4_ADDRESSES","name":"Trusted Hosts","items":[{"type":"IPV4_ADDRESS","value":"192.168.1.50"}]}'
unifi-director traffic update <uuid> '<json>'
unifi-director traffic delete <uuid>
```

---

### `resource`

Read-only supporting resources. All subcommands accept `--limit <n>`.

```bash
unifi-director resource wans              # WAN interface definitions
unifi-director resource vpn-tunnels       # site-to-site VPN tunnels
unifi-director resource vpn-servers       # VPN server configs
unifi-director resource radius            # RADIUS profiles
unifi-director resource tags              # device tags
unifi-director resource dpi-categories    # DPI application categories
unifi-director resource dpi-apps          # DPI applications
unifi-director resource countries         # ISO country codes
```

---

### `hotspot`

Manage Hotspot vouchers for captive portal / guest network access.

```bash
# List vouchers
unifi-director hotspot list
unifi-director hotspot list --limit 50
unifi-director hotspot list --filter "Hotel Guest"

# Get a single voucher
unifi-director hotspot get <uuid>

# Create vouchers
unifi-director hotspot create --name "Hotel Guest" --minutes 1440
unifi-director hotspot create --name "Conference" --minutes 480 --count 20
unifi-director hotspot create --name "VIP" --minutes 2880 --count 5 \
    --guest-limit 1 --data-limit 2048 --rx-limit 10000 --tx-limit 5000

# Delete a single voucher
unifi-director hotspot delete <uuid>

# Bulk delete by filter (requires --filter to prevent accidental mass deletion)
unifi-director hotspot delete-all --filter "Hotel Guest"
```

**Create options:**

| Flag | Required | Description |
|------|----------|-------------|
| `--name` | Yes | Note/label applied to all generated vouchers |
| `--minutes` | Yes | Access duration in minutes (e.g. `1440` = 24 h) |
| `--count` | No | Number of vouchers to generate (default: 1) |
| `--guest-limit` | No | Max guests that may share one voucher |
| `--data-limit` | No | Data usage cap in megabytes |
| `--rx-limit` | No | Download rate limit in kbps |
| `--tx-limit` | No | Upload rate limit in kbps |

---

### `switching`

Read-only view of switching infrastructure — Link Aggregation Groups, switch
stacks, and Multi-Chassis LAG domains. These are typically only present on sites
with managed switches and stacking/LAG configured.

```bash
# Link Aggregation Groups
unifi-director switching lags
unifi-director switching lags --limit 50
unifi-director switching lag <uuid>

# Switch stacks
unifi-director switching stacks
unifi-director switching stack <uuid>

# Multi-Chassis LAG domains
unifi-director switching mclags
unifi-director switching mclag <uuid>
```

All list subcommands (`lags`, `stacks`, `mclags`) accept `--limit <n>`.
Returns `No <type> configured.` gracefully if none exist on the site.

---

## Security notes

**inventory.json contains your API keys — protect it.**

- It is listed in `.gitignore` and must never be committed to version control.
- The installer sets file permissions to `600` (owner read/write only).
- API keys are never printed or logged at any log level.
- If a key is compromised, rotate it immediately in the UniFi Network UI under
  **Settings → Control Plane → Integrations**.

**SSL verification**

Direct local mode disables SSL verification by default because controllers use
self-signed certificates. If your controller has a valid certificate (e.g.,
from Let's Encrypt), enable verification:

```bash
export UNIFI_VERIFY_SSL=true
unifi-director network list
```

**Destructive commands**

`network delete`, `wifi delete`, `device decommission`, `acl delete`,
`firewall delete-*`, `dns delete`, and `traffic delete` are permanent and
take effect immediately. Use `--json` with `list`/`get` to capture state
before making destructive changes.

---

## Troubleshooting

### `Initialization Failed: Missing HOST, API_KEY, or SITE_ID`

`inventory.json` is missing, empty, or the requested console profile does not
exist. Run `unifi-director inventory` to see what profiles are loaded, then
check the file path and profile name.

### `Console 'X' not found. Available: [...]`

The profile name passed to `-c` does not match any key in `inventory.json`.
Profile names are case-sensitive.

### `Invalid JSON in inventory.json`

The file has a syntax error. Validate with:

```bash
python3 -m json.tool inventory.json
```

### HTTP 401 Unauthorized

The API key is wrong or has been revoked. Regenerate it in the UniFi Network UI
and update `inventory.json`.

### HTTP 400 on `firewall list-zones`

Zone-Based Firewall is not enabled on the controller. This is expected and
handled gracefully — the command prints an informational message and exits
cleanly.

### SSL errors on direct local mode

The controller's self-signed cert is being rejected. Confirm SSL verification is
off (it defaults to off; check that `UNIFI_VERIFY_SSL` is not set to `true`).

### `command not found: unifi-director`

The system symlink was not created. Either re-run `sudo ./setup.sh` or activate
the venv:

```bash
source /home/pi/unifi-director/.venv/bin/activate
unifi-director --help
```

### Verbose HTTP debugging

```bash
unifi-director --debug network list
```

This prints exact request URLs, headers (with truncated API keys), timing, and
response status codes.
