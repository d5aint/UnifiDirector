# UDM-Pro-Max — Full Setup & Configuration Guide

This document covers the complete setup of a UniFi Dream Machine Pro Max
(UDM-Pro-Max) from first power-on through a fully segmented, hardened network,
ending with integration into `unifi-director` for ongoing management.

> **Version note:** UI paths and option names are accurate for UniFi Network
> Application 8.x – 10.x running on UniFiOS 3.x. Ubiquiti updates the UI
> frequently — if a path differs slightly, check Settings or use the search bar
> in the UniFi Network UI.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [Hardware Overview](#2-hardware-overview)
3. [Physical Installation](#3-physical-installation)
4. [First Power-On & Initial Setup](#4-first-power-on--initial-setup)
5. [Network Design — VLAN Architecture](#5-network-design--vlan-architecture)
6. [Creating Networks & VLANs](#6-creating-networks--vlans)
7. [WiFi Configuration](#7-wifi-configuration)
8. [VPN Configuration](#8-vpn-configuration)
9. [Cyber Secure](#9-cyber-secure)
10. [Policy Engine](#10-policy-engine)
11. [Security Hardening](#11-security-hardening)
12. [UniFi Director Integration](#12-unifi-director-integration)
13. [Verification Checklist](#13-verification-checklist)

---

## 1. Before You Begin

### What you need

| Item | Notes |
|------|-------|
| UDM-Pro-Max | With power cables (included) |
| Active internet connection | ISP modem/ONT in bridge mode recommended |
| Cat6 or better Ethernet cables | For WAN and LAN connections |
| A computer or mobile device | For initial setup via browser or UniFi app |
| Ubiquiti account | Create free at [account.ui.com](https://account.ui.com) |
| 2× 3.5" SATA HDDs (optional) | For UniFi Protect local recording storage |
| SFP+ DAC or fiber module (optional) | If using the 10G SFP+ ports for uplinks |

### Decisions to make before starting

- **IP addressing scheme** — this guide uses `10.0.X.0/24` per VLAN (see Section 5)
- **Site name** — used in inventory.json and the cloud portal; choose something meaningful (e.g., `HQ`, `Branch-Office`, `City.ST-Location`)
- **Admin credentials** — use a strong, unique password; MFA will be enforced during setup
- **WiFi SSID names and passphrases** — one per segment (employee, IoT, guest)
- **ISP connection type** — DHCP, PPPoE, or static IP

---

## 2. Hardware Overview

### Front panel

| Component | Description |
|-----------|-------------|
| 1.7" LCD touchscreen | Live status: CPU, memory, WAN/LAN throughput, alerts |
| Status LED | Solid white = normal, blue = initializing, red = fault |
| USB-A port | Storage expansion or USB-to-Ethernet adapter |
| Power button | Short press = sleep display; hold 5s = graceful shutdown |

### Rear panel (left → right)

| Port | Label | Speed | Notes |
|------|-------|-------|-------|
| Console | CON | — | RJ45 serial (115200 baud); emergency access only |
| SFP+ × 2 | SFP1, SFP2 | 10G | Configurable as WAN or LAN uplink |
| RJ45 × 2 | WAN1, WAN2 | 2.5GbE | Default WAN ports |
| RJ45 × 8 | LAN1–LAN8 | 2.5GbE | Switching fabric; supports PoE pass-through on some ports |
| USB-A | — | USB 3.0 | Rear storage / adapter |
| PSU bay × 2 | — | — | Left bay = primary; right bay = optional redundant PSU |

### HDD bays

Located behind the front bezel. Supports 2× 3.5" SATA HDDs up to 20TB each for
UniFi Protect local NVR storage. HDDs are hot-swappable.

---

## 3. Physical Installation

### Rack mounting

1. Attach the included rack ears to both sides of the unit using the provided screws.
2. Slide into a 1U rack space. The UDM-Pro-Max is approximately 17" deep — ensure adequate clearance behind the unit for cable management.
3. Torque rack screws to finger-tight; over-tightening warps the chassis.

### Cable connections

Connect in this order to avoid configuration confusion:

```
ISP modem/ONT ──── WAN1 (RJ45) on UDM-Pro-Max
Your computer  ──── LAN1 (RJ45) on UDM-Pro-Max
Power          ──── PSU bay (left)
```

- If your ISP provides a 10G handoff (fiber ONT with SFP+), connect to SFP1 instead of WAN1 — the SFP+ ports can be configured as WAN in the setup wizard.
- Leave WAN2 unconnected until the primary WAN is confirmed working. It can be added later as a failover or load-balance uplink.

### HDD installation (optional — for UniFi Protect)

1. Press the front bezel release tab and swing the bezel open.
2. Slide HDDs into bays until they click into the SATA connector.
3. Close the bezel. HDDs are formatted automatically by Protect on first use.

### Power on

Connect power and wait approximately 90 seconds for the LCD to display the device IP address (`192.168.1.1` by default).

---

## 4. First Power-On & Initial Setup

### Access methods

**Option A — Web browser (recommended for initial setup):**

1. Ensure your computer has an IP address in the `192.168.1.0/24` range (it will via DHCP from the UDM).
2. Open a browser and navigate to `https://192.168.1.1`.
3. Accept the self-signed certificate warning.

**Option B — UniFi Network mobile app:**

1. Install the UniFi Network app (iOS or Android).
2. Ensure your phone is on the same network as the UDM.
3. Tap **+** → **Add Device** → follow the guided flow.

---

### Setup wizard

**Step 1 — Ubiquiti account**

- Log in with your Ubiquiti account or create one at [account.ui.com](https://account.ui.com).
- The UDM-Pro-Max requires a Ubiquiti account for initial setup.
- If the unit has no internet connection yet, use **Advanced Setup** (offline mode) — this skips cloud onboarding and lets you configure locally. You can link to the cloud later.

**Step 2 — Country & timezone**

- Set your country (affects WiFi regulatory domain and allowed channels).
- Set your timezone (affects log timestamps and scheduled tasks).

**Step 3 — WAN configuration**

| ISP type | Settings |
|----------|----------|
| DHCP (most common) | Select **DHCP** — no additional input needed |
| PPPoE (DSL/fiber) | Select **PPPoE** → enter ISP-provided username and password |
| Static IP | Select **Static** → enter IP, subnet, gateway, DNS provided by ISP |

- If your ISP requires a specific MAC address (MAC cloning), configure it under **WAN MAC Override** in the advanced settings — do this before saving if applicable.

**Step 4 — Site name**

- Enter a meaningful name (e.g., `HQ`, `Branch-Office`, `City.ST-Location`).
- This name appears in inventory.json and the cloud portal.

**Step 5 — Admin account**

- Create a local admin username and strong password.
- **Enable MFA immediately** — the wizard offers this step; do not skip it.

**Step 6 — Finish**

- The wizard applies settings and reboots the UDM (~60 seconds).
- After reboot, log back in at `https://192.168.1.1` or the IP shown on the LCD.

---

### Post-wizard baseline

Before configuring VLANs, confirm:

- WAN shows a public IP in **Dashboard → WAN**
- Internet connectivity test passes (ping 8.8.8.8)
- Firmware is current: **Settings → System → Updates** → apply any pending updates before continuing

---

## 5. Network Design — VLAN Architecture

### VLAN table

| VLAN | Name | Subnet | Gateway | Purpose |
|------|------|--------|---------|---------|
| 10 | Management | 10.0.10.0/24 | 10.0.10.1 | UDM management, network equipment |
| 20 | Servers | 10.0.20.0/24 | 10.0.20.1 | Internal servers, NAS, infrastructure |
| 30 | Employee-Wired | 10.0.30.0/24 | 10.0.30.1 | Wired workstations, docked laptops |
| 40 | Employee-WiFi | 10.0.40.0/24 | 10.0.40.1 | Wireless workstations, laptops |
| 50 | Printers | 10.0.50.0/24 | 10.0.50.1 | Printers, copiers, MFPs |
| 60 | IoT | 10.0.60.0/24 | 10.0.60.1 | Smart devices, sensors, cameras |
| 70 | DMZ | 10.0.70.0/24 | 10.0.70.1 | Public-facing servers |
| 80 | Guest | 10.0.80.0/24 | 10.0.80.1 | Visitor WiFi, temporary access |

### Traffic matrix

Defines what each segment can reach. ✅ = allowed, ❌ = blocked, ⚠️ = allowed on specific ports only.

| Source → Destination | Mgmt | Servers | Emp-Wired | Emp-WiFi | Printers | IoT | DMZ | Guest | WAN |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Management** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Servers** | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Employee-Wired** | ❌ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ | ❌ | ✅ |
| **Employee-WiFi** | ❌ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ | ❌ | ✅ |
| **Printers** | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| **IoT** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ |
| **DMZ** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| **Guest** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **WAN (inbound)** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | — |

> ⚠️ **Printers** — Employees can reach printers on TCP 9100 (raw print), 631 (IPP), 443/80 (web UI). Block all other ports.
> ⚠️ **WAN → DMZ** — Only published services (e.g., TCP 443 to a web server). All other inbound WAN traffic drops.

---

## 6. Creating Networks & VLANs

Navigate to **Settings → Networks → Create New Network** for each VLAN below.

### Common settings for all VLANs

| Setting | Value |
|---------|-------|
| Network Type | Standard |
| Auto-Scale Network | Off |
| IGMP Snooping | On (for networks with multicast, e.g., Printers, IoT) |
| Multicast DNS (mDNS) | On for Printers; Off for all others |
| DHCP Mode | Server |
| DHCP Range | `.100` – `.254` (reserve `.1`–`.99` for static assignments) |
| DHCP Lease Time | 24h for employee/server; 1h for guest |
| IPv6 | Disabled (unless your ISP provides IPv6) |

### VLAN 10 — Management

```
Name:        Management
VLAN ID:     10
Gateway IP:  10.0.10.1
Subnet:      10.0.10.0/24
DHCP Range:  10.0.10.100 – 10.0.10.254
```

- Assign the UDM-Pro-Max management interface to this VLAN after creation.
- Only network administrators should have devices on this VLAN.
- No WiFi SSID should be mapped to this VLAN.

### VLAN 20 — Servers

```
Name:        Servers
VLAN ID:     20
Gateway IP:  10.0.20.1
Subnet:      10.0.20.0/24
DHCP Range:  10.0.20.100 – 10.0.20.254
```

- Assign static IPs to servers in the `.10`–`.99` range via DHCP reservations.

### VLAN 30 — Employee-Wired

```
Name:        Employee-Wired
VLAN ID:     30
Gateway IP:  10.0.30.1
Subnet:      10.0.30.0/24
DHCP Range:  10.0.30.100 – 10.0.30.254
```

### VLAN 40 — Employee-WiFi

```
Name:        Employee-WiFi
VLAN ID:     40
Gateway IP:  10.0.40.1
Subnet:      10.0.40.0/24
DHCP Range:  10.0.40.100 – 10.0.40.254
```

### VLAN 50 — Printers

```
Name:        Printers
VLAN ID:     50
Gateway IP:  10.0.50.1
Subnet:      10.0.50.0/24
DHCP Range:  10.0.50.100 – 10.0.50.254
IGMP:        Enabled
mDNS:        Enabled
```

- Enable mDNS so that AirPrint and Bonjour discovery works across VLANs.
- Assign static IPs to all printers via DHCP reservation.

### VLAN 60 — IoT

```
Name:        IoT
VLAN ID:     60
Gateway IP:  10.0.60.1
Subnet:      10.0.60.0/24
DHCP Range:  10.0.60.100 – 10.0.60.254
```

- Enable Client Device Isolation to prevent IoT devices from communicating with each other.

### VLAN 70 — DMZ

```
Name:        DMZ
VLAN ID:     70
Gateway IP:  10.0.70.1
Subnet:      10.0.70.0/24
DHCP Range:  10.0.70.100 – 10.0.70.254
```

- Assign static IPs to all DMZ servers.
- No device in the DMZ should ever have a route to internal VLANs.

### VLAN 80 — Guest

```
Name:        Guest
VLAN ID:     80
Gateway IP:  10.0.80.1
Subnet:      10.0.80.0/24
DHCP Range:  10.0.80.100 – 10.0.80.254
DHCP Lease:  1h
```

- Enable **Client Device Isolation**.
- Enable **Network Isolation** (blocks inter-VLAN routing at the network level as a belt-and-suspenders measure alongside firewall rules).

---

## 7. WiFi Configuration

Navigate to **Settings → WiFi → Create New WiFi Network**.

### SSID design

| SSID | Band | Security | VLAN | Notes |
|------|------|----------|------|-------|
| `Corp-Staff` | 5 GHz (+ 6 GHz if supported) | WPA3-Personal or WPA3/WPA2 mixed | Employee-WiFi (40) | Employee wireless |
| `Corp-IoT` | 2.4 GHz | WPA2-Personal | IoT (60) | IoT devices; 2.4 GHz for compatibility |
| `Corp-Guest` | 5 GHz | WPA3-Personal | Guest (80) | Visitor access |

> **Do not create an SSID for Management, Servers, Printers, or DMZ.** Those segments are wired-only.

---

### Corp-Staff (Employee WiFi)

**Settings → WiFi → Create New WiFi Network**

```
Name (SSID):       Corp-Staff
Password:          [strong passphrase, minimum 16 characters]
Network:           Employee-WiFi (VLAN 40)
Security Protocol: WPA3 (or WPA3/WPA2 transitional for legacy device support)
Band:              Auto (allows 2.4 / 5 / 6 GHz)
```

**Advanced settings:**

| Setting | Value | Reason |
|---------|-------|--------|
| PMF (Protected Management Frames) | Required | Mandatory for WPA3; mitigates deauth attacks |
| Band Steering | Enabled | Pushes capable clients to 5/6 GHz |
| BSS Transition | Enabled | Enables 802.11v for roaming |
| Fast Roaming (802.11r) | Enabled | Reduces roam latency between APs |
| Client Device Isolation | Disabled | Employees should be able to communicate with each other |
| Proxy ARP | Enabled | Reduces broadcast traffic on wireless segments |
| UAPSD | Enabled | Power saving for mobile devices |
| Schedule | No restriction | Available 24/7 |

---

### Corp-IoT

```
Name (SSID):       Corp-IoT
Password:          [strong passphrase]
Network:           IoT (VLAN 60)
Security Protocol: WPA2-Personal
Band:              2.4 GHz only
```

**Advanced settings:**

| Setting | Value | Reason |
|---------|-------|--------|
| PMF | Disabled | Many IoT devices do not support PMF |
| Band Steering | Disabled | Fixed to 2.4 GHz for compatibility |
| Client Device Isolation | Enabled | IoT devices must not reach each other |
| SSID Broadcast | Enabled | Devices need to find the network |
| Maximum Association | Set a reasonable cap (e.g., 100) | Prevents runaway device adoption |

---

### Corp-Guest

```
Name (SSID):       Corp-Guest
Password:          [rotate regularly — consider hotspot vouchers]
Network:           Guest (VLAN 80)
Security Protocol: WPA3-Personal (or WPA2 for broad compatibility)
Band:              Auto
```

**Advanced settings:**

| Setting | Value | Reason |
|---------|-------|--------|
| Client Device Isolation | Enabled | Guests must not see each other |
| Network Isolation | Enabled | Belt-and-suspenders: blocks cross-VLAN routing |
| Hotspot Portal | Optional | Enable for voucher-based access control |
| Rate Limiting | Down: 25 Mbps / Up: 10 Mbps | Prevents guest bandwidth abuse |
| Schedule | Business hours or 24/7 as needed | |

---

## 8. VPN Configuration

The UDM-Pro-Max supports three VPN types. Choose based on use case.

### 8a. Remote Access VPN (WireGuard — recommended)

Used for employees working remotely who need access to internal resources.

Navigate to **Settings → VPN → VPN Server → Create VPN Server**

```
Type:              WireGuard
VPN Name:          Remote-Access
Interface:         WAN1 (or WAN2 for failover)
Tunnel IP:         10.0.200.1/24   (dedicated VPN pool, not overlapping any VLAN)
DNS:               10.0.10.1       (point to Management VLAN gateway for internal DNS)
Pre-Shared Key:    [auto-generated — save securely]
```

**Adding clients:**

1. **Settings → VPN → VPN Server → [Remote-Access] → Clients → Add Client**
2. Create one profile per user — never share profiles between users.
3. Download the `.conf` file or QR code and deliver securely to the user.
4. Revoke individual profiles if a device is lost or a user leaves.

**Firewall rule for VPN clients:**

Create a firewall rule (in Policy Engine → Policy Table) to restrict what VPN clients can reach:
- Allow VPN → Servers (VLAN 20): for internal resources
- Allow VPN → Management (VLAN 10): for IT admins only (create a separate VPN profile for admins)
- Block VPN → all other VLANs

---

### 8b. Site-to-Site VPN (IPsec)

Used to connect two physical office locations.

Navigate to **Settings → VPN → Site-to-Site VPN → Create**

```
Type:              IPsec
Name:              [Site-A to Site-B]
Pre-Shared Key:    [strong random string, minimum 32 characters]

Local:
  WAN IP:          [your WAN IP or DDNS hostname]
  Subnets:         10.0.0.0/8  (or specific VLANs you want to expose)

Remote:
  WAN IP:          [remote site WAN IP or DDNS hostname]
  Subnets:         [remote site subnet ranges]

IKE Version:       IKEv2
Encryption:        AES-256-GCM
DH Group:          20 (384-bit ECC)
```

> Use WireGuard site-to-site (Settings → VPN → Site-to-Site → WireGuard) if both sites run UniFi — it is simpler to configure and more performant than IPsec.

---

### 8c. Dynamic DNS (recommended for VPN reliability)

If your WAN IP changes, configure DDNS so remote VPN clients always find the UDM.

**Settings → Internet → [WAN1] → Advanced → Dynamic DNS**

```
Service:    [your DDNS provider — e.g., DynDNS, No-IP, Cloudflare]
Hostname:   vpn.yourdomain.com
Username:   [DDNS account username]
Password:   [DDNS account password]
```

---

## 9. Cyber Secure

Navigate to **Security** in the left navigation panel.

### 9a. Intrusion Detection & Prevention (IDS/IPS)

**Security → Threat Management → IDS/IPS**

| Setting | Recommended Value |
|---------|------------------|
| Mode | **Prevention** (IPS — actively blocks threats) |
| Interface | WAN1 (and WAN2 if configured) |
| Sensitivity | Balanced (raise to High after confirming no false positives) |
| Threat Categories | Enable all: Malware, Botnet, Exploit, Scan, Suspicious |

> Start in **Detection** mode for the first 48 hours to review alerts before switching to **Prevention** to avoid blocking legitimate traffic.

**Suppression rules:**

If IPS generates false positives for known-good traffic, add suppression rules:
**Threat Management → IDS/IPS → Suppression → Add Rule**

---

### 9b. Content Filtering

**Security → Threat Management → Content Filtering**

Configure per-network to match the trust level of each segment:

| Network | Preset | Additional blocks |
|---------|--------|-----------------|
| Employee-Wired | Work | Malware, Phishing |
| Employee-WiFi | Work | Malware, Phishing |
| IoT | Strict | All categories except device update services |
| Guest | Family | Malware, Adult, Gambling |
| Printers | None (or Strict) | Block all non-printing traffic at firewall instead |
| Servers | None | Managed via OS-level controls |

**Available filter categories:**

- Malware, Phishing, Botnet (enable on all networks)
- Adult Content, Gambling, Social Media, Streaming (per policy)
- Ad Networks (optional — can break some legitimate services)

---

### 9c. Traffic Logging

**Security → Traffic Logging**

| Setting | Value |
|---------|-------|
| Enable Traffic Logging | On |
| Log Level | Verbose (during initial deployment); Normal (ongoing) |
| Remote Syslog | On |
| Syslog Host | IP of your SIEM or syslog server |
| Syslog Port | 514 (UDP) or 6514 (TLS — preferred) |
| Protocol | TLS if your syslog server supports it |

**What gets logged:**

- Firewall allow/deny events
- IDS/IPS alerts and blocks
- Client connect/disconnect events
- Admin login events
- WAN state changes

> If you do not have a SIEM yet, enable logging to local storage and set up a log aggregator (e.g., Graylog, Loki, or Splunk) as a follow-on task. Do not skip enabling logging — you need the audit trail.

---

## 10. Policy Engine

The Policy Engine (Zone-Based Firewall) replaces the legacy LAN In/Out
rule model. It organizes traffic control into Zones, Objects, and Policies.

Navigate to **Security → Firewall & Security** (or **Policy Engine** depending on firmware version).

---

### 10a. Zones

Zones group networks by trust level. Create the following zones:

**Security → Firewall → Zones → Create Zone**

| Zone | Networks assigned | Trust level |
|------|------------------|-------------|
| Management | Management (VLAN 10) | Highest |
| Internal | Servers (20), Employee-Wired (30), Employee-WiFi (40) | High |
| Restricted | Printers (50), IoT (60) | Medium |
| DMZ | DMZ (70) | Low |
| Untrusted | Guest (80), VPN clients | Lowest (internal) |
| WAN | WAN1, WAN2 | External |

> UniFi pre-creates a **LAN** zone and a **WAN** zone. Rename **LAN** to **Internal** and reassign networks accordingly.

---

### 10b. Objects

Objects are reusable definitions for IPs, subnets, and port groups referenced in policies.

**Security → Firewall → Objects → Create Object**

#### IP Groups

| Name | Type | Value |
|------|------|-------|
| `RFC-1918-Private` | IP Group | 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 |
| `DNS-Servers` | IP Group | 10.0.10.1 (internal), 1.1.1.1, 8.8.8.8 |
| `NTP-Servers` | IP Group | 10.0.10.1 (if running NTP internally) |
| `Syslog-Server` | IP Group | [IP of your syslog/SIEM host] |
| `Print-Servers` | IP Group | [static IPs of all printers, e.g., 10.0.50.10–50.0.50.20] |
| `VPN-Pool` | IP Group | 10.0.200.0/24 |

#### Port Groups

| Name | Ports | Used for |
|------|-------|---------|
| `Print-Ports` | TCP 9100, 631, 443, 80 | Printing protocols |
| `DNS-Port` | UDP/TCP 53 | DNS queries |
| `NTP-Port` | UDP 123 | Time synchronization |
| `Web-Ports` | TCP 80, 443 | HTTP/HTTPS |
| `UDM-Mgmt-Ports` | TCP 443, 8443, 22 | UDM web UI and SSH |

---

### 10c. Policy Table

Policies are ordered rules evaluated top-to-bottom within each zone pair.
The implicit default at the bottom of every zone pair is **deny all**.

Navigate to **Security → Firewall → Policies → Create Policy**

#### Management zone (outbound — Management can reach everything)

| # | Name | Source | Destination | Action |
|---|------|--------|-------------|--------|
| 1 | Mgmt-Allow-All | Management | Any | Allow |

#### Internal → Servers

| # | Name | Source | Destination | Action |
|---|------|--------|-------------|--------|
| 1 | Internal-Allow-Servers | Internal | Servers | Allow |

#### Internal → Printers

| # | Name | Source | Destination | Ports | Action |
|---|------|--------|-------------|-------|--------|
| 1 | Internal-Allow-Print | Internal | `Print-Servers` | `Print-Ports` | Allow |
| 2 | Internal-Block-Printers | Internal | Restricted (Printers) | Any | Block |

#### Internal → WAN

| # | Name | Source | Destination | Action |
|---|------|--------|-------------|--------|
| 1 | Internal-Allow-WAN | Internal | WAN | Allow |

#### Restricted → WAN only (IoT and Printers)

| # | Name | Source | Destination | Action |
|---|------|--------|-------------|--------|
| 1 | Restricted-Allow-WAN | Restricted | WAN | Allow |
| 2 | Restricted-Block-Internal | Restricted | RFC-1918-Private | Block |

#### DMZ → WAN only

| # | Name | Source | Destination | Action |
|---|------|--------|-------------|--------|
| 1 | DMZ-Allow-WAN | DMZ | WAN | Allow |
| 2 | DMZ-Block-Internal | DMZ | RFC-1918-Private | Block |

#### Guest → WAN only

| # | Name | Source | Destination | Action |
|---|------|--------|-------------|--------|
| 1 | Guest-Allow-DNS | Untrusted | `DNS-Servers` | Allow (UDP/TCP 53) |
| 2 | Guest-Allow-WAN | Untrusted | WAN | Allow |
| 3 | Guest-Block-Internal | Untrusted | RFC-1918-Private | Block |

#### WAN → DMZ (published services only)

| # | Name | Source | Destination | Ports | Action |
|---|------|--------|-------------|-------|--------|
| 1 | WAN-Allow-DMZ-HTTPS | WAN | [DMZ web server IP] | TCP 443 | Allow |
| 2 | WAN-Block-All | WAN | RFC-1918-Private | Any | Block |

> Add WAN → DMZ rules only for services you actually publish externally. The default is block all inbound from WAN.

---

### 10d. Routing Table

For most deployments the routing table requires no manual entries — the UDM-Pro-Max handles all inter-VLAN routing automatically once networks are created.

Manual static routes are needed when:
- A downstream router exists on a VLAN (e.g., a server VLAN with its own router)
- Site-to-site VPN routes need to be explicitly advertised

**Security → Firewall → Routing → Static Routes → Add Route**

```
Example — Route to remote site over VPN:
  Destination:   10.1.0.0/16    (remote site subnets)
  Gateway:       [VPN tunnel interface IP]
  Distance:      1
  Name:          Site-B-VPN
```

---

## 11. Security Hardening

Apply these settings immediately after completing the network and policy configuration.

### Admin accounts

**Settings → Admins & Users**

- Enable MFA for every admin account (hardware key or authenticator app preferred over SMS).
- Remove any auto-created or default accounts.
- Create separate accounts per administrator — no shared credentials.
- Assign the minimum required role: **Read Only** for monitoring staff; **Network Admin** for network engineers; **Super Admin** only for primary administrator.

### Management access restriction

**Settings → System → Administration**

- Under **Access Control**, restrict the management UI to the Management VLAN (`10.0.10.0/24`) only.
- Disable access from Guest, IoT, and all untrusted VLANs.

### Device SSH

**Settings → System → Device Authentication**

- Change the default SSH username and password.
- Upload your SSH public key and disable password-based SSH authentication.
- Disable SSH entirely if it is not required for your environment.

### Firmware auto-update

**Settings → System → Updates**

- Enable **Auto Update** for the controller and managed devices — or set a maintenance window and commit to manual updates on a defined schedule.

### SSL certificate

**Settings → System → SSL Certificate**

- Replace the self-signed certificate with a valid certificate.
- If your UDM has a public FQDN, use Let's Encrypt (supported natively via UniFiOS or ACME scripts).
- If management-only (no public FQDN), use an internal CA certificate.

### Backup

**Settings → System → Backups**

- Enable **Auto Backup**.
- Set retention to at least 7 daily backups.
- If using UniFi Cloud, backups upload automatically; for self-hosted, configure an off-device backup destination.

### SNMP

**Settings → System → SNMP**

- **Disable SNMP** unless you are actively monitoring with an SNMP-capable NMS.
- If required: use SNMPv3 with `authPriv` security level (authentication + encryption). Never use SNMPv1/v2c community strings in production.

### Remote access

**Settings → System → Remote Access**

- If your team manages the device exclusively via VPN, disable UniFi Cloud remote access.
- If cloud access is required, ensure all accounts with remote access have MFA enforced.

---

## 12. UniFi Director Integration

### Generate an API key

The UniFi Director CLI uses the Integration API, which requires an API key.

1. Log in to the UniFi Network UI.
2. Navigate to **Settings → Control Plane → Integrations**.
3. Click **Create API Key**.
4. Name the key something identifiable (e.g., `unifi-director-prod`).
5. Set scope to **Read/Write** (required for write commands like ACL, DNS, device actions).
6. Copy the key immediately — it is shown only once.

> Store the key in `inventory.json` only. Never commit `inventory.json` to version control. It is gitignored by default in the unifi-director project.

### Find your Site ID

The Site ID is a UUID that identifies the default site on this controller.

**Option A — via unifi-director (once configured):**

```bash
unifi-director -c <profile-name> site list
```

The `id` column is the Site ID UUID.

**Option B — via the UniFi Network UI:**

1. Navigate to any network settings page.
2. The URL contains the site identifier, e.g.: `.../network/default/settings/...`
3. For the UUID, use the API directly: `https://<HOST>/proxy/network/integration/v1/sites`

### Add to inventory.json

Open `inventory.json` in your unifi-director project directory:

```json
{
  "cloud": {
    "host": "api.ui.com",
    "api_key": "<your-ui.com-cloud-api-key-if-applicable>"
  },
  "consoles": {
    "your-site-name": {
      "host": "10.0.10.1",
      "api_key": "<api-key-from-step-above>",
      "site_id": "<site-uuid-from-step-above>"
    }
  }
}
```

> Use the Management VLAN IP (`10.0.10.1`) as the host — not the original `192.168.1.1`. After VLAN configuration, the UDM management interface is accessible on the Management VLAN gateway.

### Verify the integration

```bash
cd /path/to/unifi-director
.venv/bin/unifi-director -c your-site-name inventory
.venv/bin/unifi-director -c your-site-name version
.venv/bin/unifi-director -c your-site-name audit --limit 5
```

### Run a baseline report

```bash
.venv/bin/unifi-director -c your-site-name report
```

Save the output file as your baseline configuration snapshot. Re-run after every
significant change as an audit trail.

---

## 13. Verification Checklist

Work through this checklist after completing setup to confirm the configuration is correct and complete.

### Connectivity

- [ ] WAN1 shows a public IP and passes internet connectivity
- [ ] All VLANs have DHCP serving addresses in the correct range
- [ ] Clients on Employee-Wired and Employee-WiFi can reach the internet
- [ ] Clients on Guest can reach the internet but cannot ping `10.0.0.0/8`
- [ ] IoT clients can reach the internet but cannot ping Employee or Server VLANs
- [ ] DMZ servers can reach the internet but cannot ping `10.0.0.0/8`
- [ ] VPN remote access connects and routes to Servers VLAN correctly
- [ ] Printers are reachable from Employee VLANs on print ports only

### Security

- [ ] MFA is enabled on all admin accounts
- [ ] Management UI is accessible only from Management VLAN
- [ ] IDS/IPS is in Prevention mode (after initial detection-only tuning period)
- [ ] Content filtering is applied to Employee and Guest networks
- [ ] Traffic logging is enabled and forwarding to syslog destination
- [ ] Auto-backup is enabled and a test restore has been performed
- [ ] Self-signed SSL certificate has been replaced with a valid certificate
- [ ] SNMP is disabled or configured as SNMPv3 only
- [ ] SSH is restricted to key-based authentication

### Policy Engine

- [ ] All zones are created and networks assigned correctly
- [ ] All inter-VLAN firewall policies match the traffic matrix in Section 5
- [ ] WAN inbound blocks all traffic except published DMZ services
- [ ] Guest and IoT VLANs cannot reach any RFC-1918 address except their own gateway

### UniFi Director

- [ ] `unifi-director inventory` lists the console correctly
- [ ] `unifi-director version` shows controller version without errors
- [ ] `unifi-director audit` completes without errors
- [ ] `unifi-director report` generates a complete baseline report with 0 section failures
- [ ] `inventory.json` is not committed to version control (confirm `.gitignore` is in place)
