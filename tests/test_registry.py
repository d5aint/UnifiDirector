"""Tests for unifi_director.registry._initialize_registry."""

import json
import sys
from unittest.mock import patch

import pytest


def _init(**env):
    """Call _initialize_registry with env vars patched."""
    from unifi_director.registry import _initialize_registry
    with patch.dict("os.environ", env, clear=False):
        return _initialize_registry()


class TestBypassMode:
    def test_help_flag_returns_null_registry(self):
        with patch.object(sys, "argv", ["unifi-director", "--help"]):
            reg = _init()
        assert reg.HOST == ""
        assert reg.API_KEY == ""
        assert str(reg.SITE_ID) == "00000000-0000-0000-0000-000000000000"
        assert reg.CONSOLE_ID is None
        assert reg.CONSOLE_NAME is None

    def test_short_help_flag(self):
        with patch.object(sys, "argv", ["unifi-director", "-h"]):
            reg = _init()
        assert reg.HOST == ""

    def test_single_argv_returns_null_registry(self):
        with patch.object(sys, "argv", ["unifi-director"]):
            reg = _init()
        assert reg.HOST == ""
        assert reg.VERIFY_SSL is False
        assert reg.DEBUG is False


class TestEnvVarMode:
    """No inventory.json, no --console — loads entirely from environment."""

    _SITE = "12345678-1234-5678-1234-567812345678"

    def test_loads_from_env_vars(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "version"]):
            reg = _init(
                UNIFI_HOST="10.0.0.1",
                UNIFI_API_KEY="test-key",
                UNIFI_SITE_ID=self._SITE,
            )
        assert reg.HOST == "10.0.0.1"
        assert str(reg.SITE_ID) == self._SITE
        assert reg.CONSOLE_ID is None
        assert reg.CONSOLE_NAME is None

    def test_debug_env_var(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "version"]):
            reg = _init(
                UNIFI_HOST="10.0.0.1",
                UNIFI_API_KEY="test-key",
                UNIFI_SITE_ID=self._SITE,
                UNIFI_DEBUG="true",
            )
        assert reg.DEBUG is True

    def test_debug_cli_flag(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "--debug", "version"]):
            reg = _init(
                UNIFI_HOST="10.0.0.1",
                UNIFI_API_KEY="test-key",
                UNIFI_SITE_ID=self._SITE,
            )
        assert reg.DEBUG is True

    def test_verify_ssl_env_var(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "version"]):
            reg = _init(
                UNIFI_HOST="10.0.0.1",
                UNIFI_API_KEY="test-key",
                UNIFI_SITE_ID=self._SITE,
                UNIFI_VERIFY_SSL="true",
            )
        assert reg.VERIFY_SSL is True

    def test_missing_host_exits(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "version"]), \
             patch.dict("os.environ", {"UNIFI_HOST": "", "UNIFI_API_KEY": "key", "UNIFI_SITE_ID": self._SITE}, clear=False):
            from unifi_director.registry import _initialize_registry
            with pytest.raises(SystemExit) as exc:
                _initialize_registry()
        assert exc.value.code == 1

    def test_missing_site_id_exits(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "version"]), \
             patch.dict("os.environ", {"UNIFI_HOST": "10.0.0.1", "UNIFI_API_KEY": "key", "UNIFI_SITE_ID": ""}, clear=False):
            from unifi_director.registry import _initialize_registry
            with pytest.raises(SystemExit) as exc:
                _initialize_registry()
        assert exc.value.code == 1

    def test_invalid_site_uuid_exits(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "version"]):
            from unifi_director.registry import _initialize_registry
            with pytest.raises(SystemExit) as exc:
                with patch.dict("os.environ", {
                    "UNIFI_HOST": "10.0.0.1",
                    "UNIFI_API_KEY": "key",
                    "UNIFI_SITE_ID": "not-a-uuid",
                }, clear=False):
                    _initialize_registry()
        assert exc.value.code == 1


class TestInventoryMode:
    _SITE = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"

    def _write_inventory(self, tmp_path, consoles=None):
        data = {
            "cloud": {"host": "api.ui.com", "api_key": "cloud-key"},
            "consoles": consoles or {
                "home": {
                    "host": "192.168.1.1",
                    "api_key": "local-key",
                    "site_id": self._SITE,
                }
            },
        }
        (tmp_path / "inventory.json").write_text(json.dumps(data))

    def test_loads_named_console_long_flag(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        self._write_inventory(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "--console", "home", "version"]):
            from unifi_director.registry import _initialize_registry
            reg = _initialize_registry()
        assert reg.HOST == "192.168.1.1"
        assert str(reg.SITE_ID) == self._SITE
        assert reg.CONSOLE_NAME == "home"
        assert reg.CLOUD_HOST == "api.ui.com"

    def test_loads_named_console_equals_syntax(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        self._write_inventory(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "--console=home", "version"]):
            from unifi_director.registry import _initialize_registry
            reg = _initialize_registry()
        assert reg.CONSOLE_NAME == "home"

    def test_loads_named_console_short_flag(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        self._write_inventory(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "-c", "home", "version"]):
            from unifi_director.registry import _initialize_registry
            reg = _initialize_registry()
        assert reg.CONSOLE_NAME == "home"

    def test_console_id_populated(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        self._write_inventory(tmp_path, consoles={
            "hq": {
                "host": "10.0.0.1",
                "api_key": "key",
                "site_id": self._SITE,
                "console_id": "console-xyz",
            }
        })
        with patch.object(sys, "argv", ["unifi-director", "--console", "hq", "version"]):
            from unifi_director.registry import _initialize_registry
            reg = _initialize_registry()
        assert reg.CONSOLE_ID == "console-xyz"

    def test_unknown_console_exits(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        self._write_inventory(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "--console", "office", "version"]):
            from unifi_director.registry import _initialize_registry
            with pytest.raises(SystemExit) as exc:
                _initialize_registry()
        assert exc.value.code == 1

    def test_missing_inventory_with_console_arg_exits(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)  # empty — no inventory.json
        with patch.object(sys, "argv", ["unifi-director", "--console", "home", "version"]):
            from unifi_director.registry import _initialize_registry
            with pytest.raises(SystemExit) as exc:
                _initialize_registry()
        assert exc.value.code == 1

    def test_invalid_json_exits(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        (tmp_path / "inventory.json").write_text("{not valid json")
        with patch.object(sys, "argv", ["unifi-director", "--console", "home", "version"]):
            from unifi_director.registry import _initialize_registry
            with pytest.raises(SystemExit) as exc:
                _initialize_registry()
        assert exc.value.code == 1

    def test_env_var_overrides_inventory_host(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        self._write_inventory(tmp_path)
        with patch.object(sys, "argv", ["unifi-director", "--console", "home", "version"]), \
             patch.dict("os.environ", {"UNIFI_HOST": "10.99.99.99"}, clear=False):
            from unifi_director.registry import _initialize_registry
            reg = _initialize_registry()
        assert reg.HOST == "10.99.99.99"
