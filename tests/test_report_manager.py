"""Tests for unifi_director.modules.report_manager."""

import re

import pytest

from unifi_director.modules.report_manager import (
    MANUAL_CHECKLIST,
    _collect,
    _to_dict,
    default_filename,
)


class TestToDictHelper:
    def test_none_returns_none(self):
        assert _to_dict(None) is None

    def test_obj_with_to_dict(self):
        class Obj:
            def to_dict(self):
                return {"x": 1}
        assert _to_dict(Obj()) == {"x": 1}

    def test_list_recursive(self):
        class Obj:
            def to_dict(self):
                return {"y": 2}
        result = _to_dict([Obj(), None])
        assert result == [{"y": 2}, None]

    def test_plain_value_passthrough(self):
        assert _to_dict(42) == 42
        assert _to_dict("hello") == "hello"


class TestCollect:
    def test_successful_list(self):
        result = _collect("test", lambda: [1, 2, 3])
        assert result == {"data": [1, 2, 3], "count": 3, "error": None}

    def test_empty_list(self):
        result = _collect("test", lambda: [])
        assert result == {"data": [], "count": 0, "error": None}

    def test_exception_isolation(self):
        def boom():
            raise RuntimeError("API unavailable")

        result = _collect("networks", boom)
        assert result["data"] is None
        assert result["count"] is None
        assert "API unavailable" in result["error"]

    def test_exception_does_not_raise(self):
        # _collect must never propagate — the whole point is failure isolation
        result = _collect("x", lambda: (_ for _ in ()).throw(Exception("crash")))
        assert result["error"] is not None

    def test_items_with_to_dict(self):
        class Obj:
            def to_dict(self):
                return {"key": "val"}

        result = _collect("items", lambda: [Obj()])
        assert result["data"] == [{"key": "val"}]
        assert result["count"] == 1

    def test_returns_non_list_iterable(self):
        # generators are valid — they'll be consumed into a list
        result = _collect("gen", lambda: (x for x in range(3)))
        assert result["count"] == 3

    def test_non_iterable_result(self):
        # a plain dict is not consumed as a list — count is None
        result = _collect("dict", lambda: {"k": "v"})
        assert result["data"] == {"k": "v"}
        assert result["count"] is None


class TestDefaultFilename:
    def test_filename_starts_with_prefix(self):
        name = default_filename("home")
        assert name.startswith("unifi-director-report-home-")

    def test_filename_ends_with_json(self):
        assert default_filename("home").endswith(".json")

    def test_spaces_replaced_with_underscores(self):
        name = default_filename("My Console")
        assert " " not in name
        assert "My_Console" in name

    def test_slashes_replaced_with_dashes(self):
        name = default_filename("site/primary")
        assert "/" not in name
        assert "site-primary" in name

    def test_timestamp_format(self):
        name = default_filename("home")
        # Expect YYYY-MM-DD_HH-MM-SS segment
        assert re.search(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}", name)


class TestManualChecklist:
    EXPECTED_COUNT = 30

    def test_correct_item_count(self):
        assert len(MANUAL_CHECKLIST) == self.EXPECTED_COUNT

    def test_all_items_have_required_fields(self):
        for item in MANUAL_CHECKLIST:
            assert "id" in item, f"Missing 'id' in {item}"
            assert "category" in item, f"Missing 'category' in {item}"
            assert "priority" in item, f"Missing 'priority' in {item}"
            assert "check" in item, f"Missing 'check' in {item}"
            assert "location" in item, f"Missing 'location' in {item}"
            assert "nist_csf" in item, f"Missing 'nist_csf' in {item}"

    def test_all_priorities_are_valid(self):
        valid = {"High", "Medium", "Low"}
        for item in MANUAL_CHECKLIST:
            assert item["priority"] in valid, f"Invalid priority '{item['priority']}' on {item['id']}"

    def test_ids_are_unique(self):
        ids = [item["id"] for item in MANUAL_CHECKLIST]
        assert len(ids) == len(set(ids)), "Duplicate IDs found in MANUAL_CHECKLIST"

    def test_expected_categories_present(self):
        categories = {item["category"] for item in MANUAL_CHECKLIST}
        assert "Admin Access" in categories
        assert "Threat Management" in categories
        assert "Logging & Monitoring" in categories
        assert "Guest & IoT Networks" in categories

    def test_high_priority_items_exist(self):
        high = [i for i in MANUAL_CHECKLIST if i["priority"] == "High"]
        assert len(high) >= 5

    def test_nist_csf_format(self):
        # All NIST CSF references should follow the XX.YY-N pattern
        for item in MANUAL_CHECKLIST:
            ref = item["nist_csf"]
            assert re.match(r"[A-Z]{2}\.[A-Z]{2}-\d+", ref), \
                f"Unexpected NIST CSF format '{ref}' on {item['id']}"
