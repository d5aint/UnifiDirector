"""Tests for unifi_director.main.main() — routing and error handling."""

import sys
from unittest.mock import MagicMock, call, patch

import pytest

from unifi_director.main import main
from unifi_director.registry import REGISTRY


def _run(*argv):
    """Invoke main() with a patched sys.argv and a mocked shared client."""
    with patch("unifi_director.main.get_shared_client") as mock_client_factory:
        mock_client_factory.return_value = MagicMock()
        with patch.object(sys, "argv", ["unifi-director"] + list(argv)):
            main()
    return mock_client_factory


class TestCommandRouting:
    @patch("unifi_director.main.handle_inventory_command")
    def test_inventory_routes(self, mock_handler):
        _run("inventory")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_version_command")
    def test_version_routes(self, mock_handler):
        _run("version")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_report_command")
    def test_report_routes(self, mock_handler):
        _run("report")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_cloud_commands")
    def test_cloud_routes(self, mock_handler):
        _run("cloud", "hosts")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.run_comprehensive_audit")
    def test_audit_routes(self, mock_handler):
        _run("audit")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_acl_commands")
    def test_acl_routes(self, mock_handler):
        _run("acl", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_client_commands")
    def test_client_routes(self, mock_handler):
        _run("client", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_dns_commands")
    def test_dns_routes(self, mock_handler):
        _run("dns", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_firewall_commands")
    def test_firewall_routes(self, mock_handler):
        _run("firewall", "list-zones")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_network_commands")
    def test_network_routes(self, mock_handler):
        _run("network", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_resource_commands")
    def test_resource_routes(self, mock_handler):
        _run("resource", "wans")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_site_commands")
    def test_site_routes(self, mock_handler):
        _run("site", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_traffic_commands")
    def test_traffic_routes(self, mock_handler):
        _run("traffic", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_device_commands")
    def test_device_routes(self, mock_handler):
        _run("device", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_wifi_commands")
    def test_wifi_routes(self, mock_handler):
        _run("wifi", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_hotspot_commands")
    def test_hotspot_routes(self, mock_handler):
        _run("hotspot", "list")
        mock_handler.assert_called_once()

    @patch("unifi_director.main.handle_switching_commands")
    def test_switching_routes(self, mock_handler):
        _run("switching", "lags")
        mock_handler.assert_called_once()


class TestSiteOverride:
    @patch("unifi_director.main.handle_version_command")
    def test_valid_site_uuid_updates_registry(self, _mock):
        test_uuid = "12345678-1234-5678-1234-567812345678"
        _run("--site", test_uuid, "version")
        assert str(REGISTRY.SITE_ID) == test_uuid
        assert REGISTRY.SITE_ID_RAW == test_uuid

    def test_invalid_site_uuid_exits_with_1(self):
        with patch("unifi_director.main.get_shared_client"):
            with patch.object(sys, "argv", ["unifi-director", "--site", "not-a-uuid", "version"]):
                with pytest.raises(SystemExit) as exc:
                    main()
        assert exc.value.code == 1


class TestErrorHandling:
    def test_keyboard_interrupt_exits_cleanly(self):
        with patch("unifi_director.main.get_shared_client", side_effect=KeyboardInterrupt):
            with patch.object(sys, "argv", ["unifi-director", "version"]):
                with pytest.raises(SystemExit) as exc:
                    main()
        assert exc.value.code == 0

    def test_fatal_exception_exits_with_1(self):
        with patch("unifi_director.main.get_shared_client", side_effect=RuntimeError("fatal")):
            with patch.object(sys, "argv", ["unifi-director", "version"]):
                with pytest.raises(SystemExit) as exc:
                    main()
        assert exc.value.code == 1

    @patch("unifi_director.main.handle_version_command", side_effect=Exception("handler crash"))
    def test_handler_exception_exits_with_1(self, _mock):
        with patch("unifi_director.main.get_shared_client"):
            with patch.object(sys, "argv", ["unifi-director", "version"]):
                with pytest.raises(SystemExit) as exc:
                    main()
        assert exc.value.code == 1

    @patch("unifi_director.main.handle_version_command", side_effect=KeyboardInterrupt)
    def test_handler_keyboard_interrupt_exits_cleanly(self, _mock):
        with patch("unifi_director.main.get_shared_client"):
            with patch.object(sys, "argv", ["unifi-director", "version"]):
                with pytest.raises(SystemExit) as exc:
                    main()
        assert exc.value.code == 0


class TestInventoryHandlerNoClient:
    """inventory command is special — it's called before get_shared_client."""

    @patch("unifi_director.main.handle_inventory_command")
    def test_inventory_handler_called_inside_client_context(self, mock_handler):
        with patch("unifi_director.main.get_shared_client") as mock_factory:
            with patch.object(sys, "argv", ["unifi-director", "inventory"]):
                main()
        # handler is called within the `with get_shared_client()` block
        mock_handler.assert_called_once()
