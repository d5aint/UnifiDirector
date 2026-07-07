# UniFi Director

> Production-grade Python CLI for managing UniFi Network Applications via the official HTTP API.

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Platform: UniFi](https://img.shields.io/badge/platform-UniFi%20Network-0559C9.svg)](https://ui.com/)

---

## Overview

UniFi Director is a structured, auditable CLI tool for managing UniFi Network Applications at scale. It wraps the official UniFi HTTP API in a typed Python client and exposes a consistent command interface for network operations, device management, firewall policy, and cloud connectivity — with full support for multi-site environments.

---

## Key Features

- **Full API coverage** — networks, WiFi, clients, devices, firewall, ACLs, DNS, traffic rules, and more
- **Multi-site support** — operate across multiple UniFi sites from a single inventory file
- **Cloud integration** — ISP metrics, cloud key management, and remote site access
- **Typed API client** — auto-generated from the official OpenAPI spec; sync and async variants for every endpoint
- **Audit command** — snapshot current controller state for change tracking and compliance review
- **Zero secrets in code** — all credentials stored in a local `inventory.json`, never hardcoded

---

## Quick Start

```bash
# Clone
git clone https://github.com/d5aint/UnifiDirector.git
cd UnifiDirector

# Install
chmod +x setup.sh && ./setup.sh

# Configure
cp inventory.json.example inventory.json
# Edit inventory.json with your controller host and API key

# Run
unifi-director audit
unifi-director network list
unifi-director device list
```

---

## Commands

| Group | Description |
|---|---|
| `inventory` | View and validate the loaded inventory |
| `cloud` | Cloud key status, ISP metrics, remote access |
| `audit` | Snapshot controller state |
| `site` | Site listing and info |
| `network` | Network CRUD operations |
| `wifi` | WiFi broadcast management |
| `client` | Connected client lookup |
| `device` | Device listing and stats |
| `firewall` | Firewall zones and policies |
| `acl` | ACL rule management |
| `dns` | DNS record management |
| `traffic` | Traffic matching rules |
| `resource` | System resource usage |

Run `unifi-director --help` or `unifi-director <command> --help` for full usage.

---

## API Client

The bundled `api_client` package provides direct access to the UniFi Network API.

### Basic usage

```python
from unifi_director.api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://<controller-host>", token="<api-key>")
```

Every endpoint module exposes four functions:

| Function | Description |
|----------|-------------|
| `sync` | Blocking — returns parsed data or `None` on failure |
| `sync_detailed` | Blocking — always returns a `Response`, with `parsed` set on success |
| `asyncio` | Same as `sync` but async |
| `asyncio_detailed` | Same as `sync_detailed` but async |

```python
from unifi_director.api_client.api.networks import get_networks
from unifi_director.api_client.types import Response

with client as c:
    networks = get_networks.sync(client=c)
    # or with full response metadata:
    response: Response = get_networks.sync_detailed(client=c)
```

### SSL / certificate verification

```python
# Custom certificate bundle (recommended for internal controllers)
client = AuthenticatedClient(
    base_url="https://internal-controller.local",
    token="<api-key>",
    verify_ssl="/path/to/certificate_bundle.pem",
)

# Disable verification — only for isolated test environments
client = AuthenticatedClient(
    base_url="https://internal-controller.local",
    token="<api-key>",
    verify_ssl=False,
)
```

### Advanced httpx customisation

```python
from unifi_director.api_client import Client

def log_request(request):
    print(f"{request.method} {request.url}")

def log_response(response):
    print(f"{response.status_code} {response.request.url}")

client = Client(
    base_url="https://<controller-host>",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or replace the underlying httpx client directly (resets base_url — re-set it)
import httpx
client.set_httpx_client(httpx.Client(base_url="https://<controller-host>"))
```

---

## Documentation

Full technical documentation — architecture, module reference, registry configuration, and API client details — is in [DOCS.md](DOCS.md).

---

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
