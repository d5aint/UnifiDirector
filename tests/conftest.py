"""
conftest.py — runs before any test module is imported.

WHY: unifi_director.registry executes _initialize_registry() at module scope.
Setting sys.argv = ['test'] (length 1) triggers the help-bypass path, which
returns a null GlobalRegistry without reading inventory.json or env vars.
This must happen here, before pytest imports any test file.
"""

import sys

sys.argv = ["test"]

import pytest
from uuid import UUID

from unifi_director.registry import REGISTRY


@pytest.fixture(autouse=True)
def _restore_registry():
    """Snapshot and restore all REGISTRY fields after each test."""
    snapshot = {
        "HOST": REGISTRY.HOST,
        "API_KEY": REGISTRY.API_KEY,
        "CLOUD_HOST": REGISTRY.CLOUD_HOST,
        "CLOUD_API_KEY": REGISTRY.CLOUD_API_KEY,
        "SITE_ID": REGISTRY.SITE_ID,
        "SITE_ID_RAW": REGISTRY.SITE_ID_RAW,
        "CONSOLE_ID": REGISTRY.CONSOLE_ID,
        "CONSOLE_NAME": REGISTRY.CONSOLE_NAME,
        "VERIFY_SSL": REGISTRY.VERIFY_SSL,
        "DEBUG": REGISTRY.DEBUG,
    }
    yield
    for field, value in snapshot.items():
        setattr(REGISTRY, field, value)
