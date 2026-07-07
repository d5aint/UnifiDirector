"""Tests for unifi_director.cli_parser.build_parser."""

import pytest

from unifi_director.cli_parser import build_parser


def _parse(*argv):
    return build_parser().parse_args(list(argv))


class TestGlobalFlags:
    def test_debug_flag(self):
        args = _parse("--debug", "version")
        assert args.debug is True

    def test_json_flag(self):
        args = _parse("--json", "version")
        assert args.json is True

    def test_site_override(self):
        uid = "12345678-0000-0000-0000-000000000000"
        args = _parse("--site", uid, "version")
        assert args.site == uid

    def test_console_flag(self):
        args = _parse("--console", "home", "version")
        assert args.console == "home"

    def test_no_command_exits(self):
        with pytest.raises(SystemExit):
            _parse()


class TestSimpleSubcommands:
    def test_inventory(self):
        args = _parse("inventory")
        assert args.command == "inventory"

    def test_version(self):
        args = _parse("version")
        assert args.command == "version"

    def test_audit_defaults(self):
        args = _parse("audit")
        assert args.command == "audit"
        assert args.limit == 100
        assert args.clients == 2
        assert args.all is False
        assert args.detailed is False

    def test_audit_all_flag(self):
        args = _parse("audit", "--all")
        assert args.all is True


class TestReportCommand:
    def test_report_defaults(self):
        args = _parse("report")
        assert args.command == "report"
        assert args.limit == 500
        assert args.stdout is False
        assert args.out is None

    def test_report_out_path(self):
        args = _parse("report", "--out", "my-report.json")
        assert args.out == "my-report.json"

    def test_report_stdout(self):
        args = _parse("report", "--stdout")
        assert args.stdout is True

    def test_report_limit(self):
        args = _parse("report", "--limit", "100")
        assert args.limit == 100


class TestCloudCommands:
    def test_cloud_hosts(self):
        args = _parse("cloud", "hosts")
        assert args.command == "cloud"
        assert args.cloud_command == "hosts"

    def test_cloud_isp_metrics(self):
        args = _parse("cloud", "isp-metrics")
        assert args.cloud_command == "isp-metrics"

    def test_cloud_missing_subcommand_exits(self):
        with pytest.raises(SystemExit):
            _parse("cloud")


class TestAclCommands:
    def test_acl_list_defaults(self):
        args = _parse("acl", "list")
        assert args.command == "acl"
        assert args.acl_command == "list"
        assert args.limit == 50

    def test_acl_list_custom_limit(self):
        args = _parse("acl", "list", "--limit", "10")
        assert args.limit == 10

    def test_acl_get(self):
        args = _parse("acl", "get", "some-uuid")
        assert args.acl_command == "get"
        assert args.id == "some-uuid"

    def test_acl_create(self):
        payload = '{"name": "test"}'
        args = _parse("acl", "create", payload)
        assert args.acl_command == "create"
        assert args.payload == payload

    def test_acl_update(self):
        args = _parse("acl", "update", "some-uuid", '{"name":"x"}')
        assert args.acl_command == "update"
        assert args.id == "some-uuid"

    def test_acl_delete(self):
        args = _parse("acl", "delete", "some-uuid")
        assert args.acl_command == "delete"

    def test_acl_get_order(self):
        args = _parse("acl", "get-order")
        assert args.acl_command == "get-order"

    def test_acl_set_order(self):
        args = _parse("acl", "set-order", '["uuid-1","uuid-2"]')
        assert args.acl_command == "set-order"


class TestNetworkCommands:
    def test_network_list(self):
        args = _parse("network", "list")
        assert args.command == "network"
        assert args.net_command == "list"
        assert args.limit == 50

    def test_network_get(self):
        args = _parse("network", "get", "net-uuid")
        assert args.net_command == "get"
        assert args.id == "net-uuid"

    def test_network_delete_force(self):
        args = _parse("network", "delete", "net-uuid", "--force")
        assert args.force is True


class TestDeviceCommands:
    def test_device_list_defaults(self):
        args = _parse("device", "list")
        assert args.command == "device"
        assert args.limit == 25

    def test_device_adopt(self):
        args = _parse("device", "adopt", "aa:bb:cc:dd:ee:ff", "--name", "Switch-1")
        assert args.mac == "aa:bb:cc:dd:ee:ff"
        assert args.name == "Switch-1"

    def test_device_action(self):
        args = _parse("device", "action", "dev-uuid", "RESTART")
        assert args.action == "RESTART"

    def test_device_port_action(self):
        args = _parse("device", "port-action", "dev-uuid", "1", "POWER_CYCLE")
        assert args.port_idx == 1


class TestClientCommands:
    def test_client_action_choices(self):
        for choice in ["RECONNECT", "BLOCK", "UNBLOCK", "AUTHORIZE", "UNAUTHORIZE"]:
            args = _parse("client", "action", "mac-or-uuid", choice)
            assert args.action == choice

    def test_client_action_invalid_choice_exits(self):
        with pytest.raises(SystemExit):
            _parse("client", "action", "mac", "INVALID")


class TestHotspotCommands:
    def test_hotspot_create_required_args(self):
        args = _parse("hotspot", "create", "--name", "Event", "--minutes", "120")
        assert args.name == "Event"
        assert args.minutes == 120
        assert args.count == 1

    def test_hotspot_create_optional_args(self):
        args = _parse("hotspot", "create", "--name", "VIP", "--minutes", "60",
                      "--count", "5", "--data-limit", "1024")
        assert args.count == 5
        assert args.data_limit == 1024

    def test_hotspot_create_missing_name_exits(self):
        with pytest.raises(SystemExit):
            _parse("hotspot", "create", "--minutes", "60")


class TestFirewallCommands:
    def test_firewall_list_policies_defaults(self):
        args = _parse("firewall", "list-policies")
        assert args.limit == 200
        assert args.all is False

    def test_firewall_toggle_policy(self):
        args = _parse("firewall", "toggle-policy", "fw-uuid", "enable")
        assert args.state == "enable"

    def test_firewall_toggle_invalid_state_exits(self):
        with pytest.raises(SystemExit):
            _parse("firewall", "toggle-policy", "fw-uuid", "maybe")

    def test_firewall_get_order(self):
        args = _parse("firewall", "get-order", "src-zone", "dst-zone")
        assert args.source_zone == "src-zone"
        assert args.dest_zone == "dst-zone"


class TestSwitchingCommands:
    def test_switching_lags(self):
        args = _parse("switching", "lags")
        assert args.command == "switching"
        assert args.switching_command == "lags"
        assert args.limit == 25

    def test_switching_stacks(self):
        args = _parse("switching", "stacks")
        assert args.switching_command == "stacks"

    def test_switching_mclags(self):
        args = _parse("switching", "mclags")
        assert args.switching_command == "mclags"

    def test_switching_lag_get(self):
        args = _parse("switching", "lag", "lag-uuid")
        assert args.switching_command == "lag"
        assert args.id == "lag-uuid"


class TestResourceCommands:
    def test_resource_wans(self):
        args = _parse("resource", "wans")
        assert args.command == "resource"
        assert args.resource_command == "wans"
        assert args.limit == 50

    def test_resource_vpn_tunnels(self):
        args = _parse("resource", "vpn-tunnels")
        assert args.resource_command == "vpn-tunnels"

    def test_resource_dpi_apps(self):
        args = _parse("resource", "dpi-apps")
        assert args.resource_command == "dpi-apps"
