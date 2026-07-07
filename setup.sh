#!/usr/bin/env bash
# UniFi Director — Raspberry Pi 5 installer (Debian Trixie, ARMv8)
#
# Usage:
#   chmod +x setup.sh
#   ./setup.sh            # installs without system-wide symlink
#   sudo ./setup.sh       # also creates /usr/local/bin/unifi-director

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_LINK="/usr/local/bin/unifi-director"

echo "=== UniFi Director Setup ==="
echo "Project dir: ${SCRIPT_DIR}"
echo ""

# --- uv ---
if ! command -v uv &>/dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "uv: $(uv --version)"
fi

# --- Install package ---
# WHY: uv reads requires-python from pyproject.toml and enforces it automatically.
# Editable install means updated source files take effect without re-running setup.sh.
echo "Installing unifi-director..."
cd "$SCRIPT_DIR"
uv sync
echo "Package installed."

# --- System-wide symlink ---
# WHY: The entry point lives in .venv/bin/ which is not on PATH by default.
# A symlink at /usr/local/bin makes the command available in any shell session
# without sourcing the venv or modifying .bashrc.
sudo ln -sf "${SCRIPT_DIR}/.venv/bin/unifi-director" "$INSTALL_LINK"
echo "Symlink created: ${INSTALL_LINK}"

# --- inventory.json ---
INVENTORY="${SCRIPT_DIR}/inventory.json"
EXAMPLE="${SCRIPT_DIR}/inventory.json.example"

echo ""
if [ ! -f "$INVENTORY" ]; then
    if [ -f "$EXAMPLE" ]; then
        cp "$EXAMPLE" "$INVENTORY"
        chmod 600 "$INVENTORY"
        echo "Created inventory.json from example template."
        echo "IMPORTANT: Edit ${INVENTORY} with your controller credentials before running."
        echo "See DOCS.md for the full configuration reference."
    else
        echo "WARNING: inventory.json not found and no example template present."
        echo "Create inventory.json manually. See DOCS.md for the required format."
    fi
else
    echo "inventory.json: found (not modified)."
fi

# --- Smoke test ---
echo ""
echo "Verifying install..."
uv run unifi-director --help

echo ""
echo "=== Setup complete ==="
if [ "$(id -u)" -eq 0 ]; then
    echo "Run from any directory: unifi-director <command>"
else
    echo "Run: uv run unifi-director <command>"
    echo "Dev tools: uv sync --group dev"
fi
