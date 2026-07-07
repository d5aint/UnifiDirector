"""Tests for unifi_director.modules.version_manager."""

import json
from unittest.mock import MagicMock, patch

import pytest

from unifi_director.modules.version_manager import (
    SPEC_BUILT_ON,
    _parse_ver,
    fetch_latest_known_version,
    get_controller_version,
    run_version_check,
)


class TestParseVer:
    def test_three_part(self):
        assert _parse_ver("10.5.54") == (10, 5, 54)

    def test_two_part(self):
        assert _parse_ver("10.5") == (10, 5)

    def test_single_part(self):
        assert _parse_ver("10") == (10,)

    def test_leading_trailing_whitespace(self):
        assert _parse_ver("  10.5.54  ") == (10, 5, 54)

    def test_invalid_returns_zero_tuple(self):
        assert _parse_ver("not-a-version") == (0,)

    def test_empty_string_returns_zero_tuple(self):
        assert _parse_ver("") == (0,)

    def test_comparison_newer_patch(self):
        assert _parse_ver("10.5.55") > _parse_ver("10.5.54")

    def test_comparison_newer_minor(self):
        assert _parse_ver("10.6.0") > _parse_ver("10.5.99")

    def test_comparison_newer_major(self):
        assert _parse_ver("11.0.0") > _parse_ver("10.99.99")

    def test_comparison_equal(self):
        assert _parse_ver("10.5.54") == _parse_ver("10.5.54")

    def test_spec_built_on_is_parseable(self):
        parsed = _parse_ver(SPEC_BUILT_ON)
        assert len(parsed) >= 3
        assert all(isinstance(x, int) for x in parsed)


class TestGetControllerVersion:
    def test_returns_version_string(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.application_version = "10.5.54"

        with patch("unifi_director.modules.version_manager.get_info.sync", return_value=mock_response):
            result = get_controller_version(mock_client)

        assert result == "10.5.54"

    def test_returns_none_on_empty_response(self):
        mock_client = MagicMock()
        with patch("unifi_director.modules.version_manager.get_info.sync", return_value=None):
            result = get_controller_version(mock_client)
        assert result is None

    def test_returns_none_on_401(self):
        from unifi_director.api_client.errors import UnexpectedStatus
        mock_client = MagicMock()
        exc = UnexpectedStatus(status_code=401, content=b"")
        with patch("unifi_director.modules.version_manager.get_info.sync", side_effect=exc):
            result = get_controller_version(mock_client)
        assert result is None

    def test_returns_none_on_http_error(self):
        import httpx
        mock_client = MagicMock()
        with patch("unifi_director.modules.version_manager.get_info.sync",
                   side_effect=httpx.HTTPError("connection refused")):
            result = get_controller_version(mock_client)
        assert result is None

    def test_returns_none_on_unexpected_exception(self):
        mock_client = MagicMock()
        with patch("unifi_director.modules.version_manager.get_info.sync",
                   side_effect=Exception("boom")):
            result = get_controller_version(mock_client)
        assert result is None


class TestFetchLatestKnownVersion:
    def _mock_github_response(self, entries):
        mock_resp = MagicMock()
        mock_resp.json.return_value = entries
        mock_resp.raise_for_status = MagicMock()
        return mock_resp

    def test_returns_highest_version(self):
        entries = [
            {"name": "10.5.54.json"},
            {"name": "10.5.55.json"},
            {"name": "10.6.0.json"},
            {"name": "README.md"},
        ]
        mock_resp = self._mock_github_response(entries)

        with patch("unifi_director.modules.version_manager.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.return_value = mock_resp
            result = fetch_latest_known_version()

        assert result == "10.6.0"

    def test_returns_none_when_no_json_files(self):
        entries = [{"name": "README.md"}, {"name": "LICENSE"}]
        mock_resp = self._mock_github_response(entries)

        with patch("unifi_director.modules.version_manager.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.return_value = mock_resp
            result = fetch_latest_known_version()

        assert result is None

    def test_returns_none_on_timeout(self):
        import httpx
        with patch("unifi_director.modules.version_manager.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.side_effect = httpx.TimeoutException("timed out")
            result = fetch_latest_known_version()
        assert result is None

    def test_returns_none_on_http_status_error(self):
        import httpx
        mock_request = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 403
        with patch("unifi_director.modules.version_manager.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.side_effect = httpx.HTTPStatusError(
                "forbidden", request=mock_request, response=mock_response
            )
            result = fetch_latest_known_version()
        assert result is None

    def test_returns_none_on_unexpected_exception(self):
        with patch("unifi_director.modules.version_manager.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.side_effect = ValueError("bad json")
            result = fetch_latest_known_version()
        assert result is None

    def test_skips_non_dict_entries(self):
        entries = [{"name": "10.5.54.json"}, "not-a-dict", None]
        mock_resp = self._mock_github_response(entries)
        with patch("unifi_director.modules.version_manager.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.return_value = mock_resp
            result = fetch_latest_known_version()
        assert result == "10.5.54"


class TestRunVersionCheck:
    @patch("unifi_director.modules.version_manager.fetch_latest_known_version")
    @patch("unifi_director.modules.version_manager.get_controller_version")
    def test_json_output_update_available(self, mock_ctrl, mock_latest, capsys):
        mock_ctrl.return_value = "10.5.50"
        mock_latest.return_value = "10.6.0"

        run_version_check(MagicMock(), as_json=True)

        data = json.loads(capsys.readouterr().out)
        assert data["update_available"] is True
        assert data["controller_version"] == "10.5.50"
        assert data["unifi_director_spec"] == SPEC_BUILT_ON

    @patch("unifi_director.modules.version_manager.fetch_latest_known_version")
    @patch("unifi_director.modules.version_manager.get_controller_version")
    def test_json_output_up_to_date(self, mock_ctrl, mock_latest, capsys):
        mock_ctrl.return_value = "10.5.54"
        mock_latest.return_value = SPEC_BUILT_ON  # same version

        run_version_check(MagicMock(), as_json=True)

        data = json.loads(capsys.readouterr().out)
        assert data["update_available"] is False

    @patch("unifi_director.modules.version_manager.fetch_latest_known_version")
    @patch("unifi_director.modules.version_manager.get_controller_version")
    def test_json_output_no_github(self, mock_ctrl, mock_latest, capsys):
        mock_ctrl.return_value = "10.5.50"
        mock_latest.return_value = None

        run_version_check(MagicMock(), as_json=True)

        data = json.loads(capsys.readouterr().out)
        assert data["update_available"] is None
        assert data["latest_spec_available"] is None

    @patch("unifi_director.modules.version_manager.fetch_latest_known_version")
    @patch("unifi_director.modules.version_manager.get_controller_version")
    def test_human_output_shows_controller(self, mock_ctrl, mock_latest, capsys):
        mock_ctrl.return_value = "10.5.50"
        mock_latest.return_value = "10.6.0"

        run_version_check(MagicMock(), as_json=False)

        out = capsys.readouterr().out
        assert "10.5.50" in out
        assert "Update available" in out

    @patch("unifi_director.modules.version_manager.fetch_latest_known_version")
    @patch("unifi_director.modules.version_manager.get_controller_version")
    def test_human_output_unknown_controller(self, mock_ctrl, mock_latest, capsys):
        mock_ctrl.return_value = None
        mock_latest.return_value = "10.6.0"

        run_version_check(MagicMock(), as_json=False)

        out = capsys.readouterr().out
        assert "Unknown" in out

    @patch("unifi_director.modules.version_manager.fetch_latest_known_version")
    @patch("unifi_director.modules.version_manager.get_controller_version")
    def test_human_output_github_unreachable(self, mock_ctrl, mock_latest, capsys):
        mock_ctrl.return_value = "10.5.50"
        mock_latest.return_value = None

        run_version_check(MagicMock(), as_json=False)

        out = capsys.readouterr().out
        assert "Unavailable" in out

    @patch("unifi_director.modules.version_manager.fetch_latest_known_version")
    @patch("unifi_director.modules.version_manager.get_controller_version")
    def test_json_does_not_include_header_lines(self, mock_ctrl, mock_latest, capsys):
        mock_ctrl.return_value = "10.5.54"
        mock_latest.return_value = SPEC_BUILT_ON

        run_version_check(MagicMock(), as_json=True)

        out = capsys.readouterr().out
        # Must parse cleanly as JSON — no leading text
        data = json.loads(out)
        assert isinstance(data, dict)
