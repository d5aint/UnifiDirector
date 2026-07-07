"""Tests for unifi_director.cli_handlers output-formatting helpers."""

from unittest.mock import MagicMock

from unifi_director.cli_handlers import (
    _format_key,
    _format_value,
    format_human_readable,
    pretty_print_json,
    display_output,
)


class TestPrettyPrintJson:
    def test_none_returns_not_found(self):
        assert "Not Found" in pretty_print_json(None)

    def test_empty_string_returns_not_found(self):
        assert "Not Found" in pretty_print_json("")

    def test_dict_is_json(self):
        result = pretty_print_json({"key": "value"})
        assert '"key": "value"' in result

    def test_list_is_json(self):
        result = pretty_print_json([1, 2, 3])
        assert "1" in result

    def test_obj_with_to_dict(self):
        obj = MagicMock()
        obj.to_dict.return_value = {"x": 42}
        result = pretty_print_json(obj)
        assert '"x": 42' in result

    def test_plain_string(self):
        result = pretty_print_json("hello")
        assert result == "hello"


class TestFormatKey:
    def test_underscores_to_spaces(self):
        assert _format_key("first_name") == "First Name"

    def test_single_word(self):
        assert _format_key("host") == "Host"

    def test_camel_case_split(self):
        result = _format_key("rxBytes")
        assert " " in result

    def test_already_spaced(self):
        result = _format_key("site id")
        assert result == "Site Id"


class TestFormatValue:
    def test_none_returns_na(self):
        assert _format_value("any", None) == "N/A"

    def test_empty_string_returns_na(self):
        assert _format_value("any", "") == "N/A"

    def test_uptime_days(self):
        # 1 day + 2 hours + 3 min + 4 sec
        seconds = 86400 + 7200 + 180 + 4
        result = _format_value("uptime_seconds", seconds)
        assert "1d" in result
        assert "2h" in result

    def test_uptime_minutes_only(self):
        result = _format_value("uptime", 90)
        assert "1m" in result
        assert "30s" in result

    def test_uptime_zero(self):
        result = _format_value("uptime", 0)
        assert "0s" in result

    def test_bps_gbps(self):
        result = _format_value("rx_bps", 2_500_000_000)
        assert "Gbps" in result
        assert "2.50" in result

    def test_bps_mbps(self):
        result = _format_value("tx_bps", 100_000_000)
        assert "Mbps" in result
        assert "100.00" in result

    def test_bps_kbps(self):
        result = _format_value("rx_bps", 5_000)
        assert "Kbps" in result

    def test_bps_plain(self):
        result = _format_value("rx_bps", 500)
        assert "500 bps" == result

    def test_percentage(self):
        result = _format_value("cpu_utilization", 42)
        assert "42%" in result

    def test_pct_key(self):
        result = _format_value("load_pct", 75)
        assert "75%" in result

    def test_plain_string_passthrough(self):
        result = _format_value("hostname", "my-switch")
        assert result == "my-switch"

    def test_bool_passthrough(self):
        result = _format_value("enabled", True)
        assert result == "True"

    def test_timestamp_format(self):
        result = _format_value("updated_at", "2024-01-15T10:30:00Z")
        # ISO separator T is replaced with a space; trailing Z becomes " UTC"
        assert "2024-01-15 10:30:00 UTC" == result


class TestFormatHumanReadable:
    def test_none_returns_not_found(self):
        result = format_human_readable(None)
        assert "Not Found" in result

    def test_dict_with_simple_values(self):
        result = format_human_readable({"host": "10.0.0.1"})
        assert "10.0.0.1" in result
        assert "Host" in result

    def test_dict_skips_none_values(self):
        result = format_human_readable({"host": "10.0.0.1", "empty": None})
        assert "empty" not in result.lower()

    def test_dict_skips_empty_list(self):
        result = format_human_readable({"items": [], "name": "x"})
        assert "items" not in result.lower()

    def test_list_of_strings(self):
        result = format_human_readable(["a", "b", "c"])
        assert "- a" in result
        assert "- b" in result

    def test_nested_dict(self):
        result = format_human_readable({"config": {"key": "val"}})
        assert "val" in result

    def test_obj_with_to_dict(self):
        obj = MagicMock()
        obj.to_dict.return_value = {"status": "active"}
        result = format_human_readable(obj)
        assert "active" in result


class TestDisplayOutput:
    def test_json_flag_prints_json(self, capsys):
        args = MagicMock()
        args.json = True
        display_output(args, "Test", {"key": "val"})
        out = capsys.readouterr().out
        assert '"key": "val"' in out

    def test_no_json_flag_prints_human(self, capsys):
        args = MagicMock()
        args.json = False
        display_output(args, "My Title", {"host": "10.0.0.1"})
        out = capsys.readouterr().out
        assert "My Title" in out
        assert "10.0.0.1" in out
