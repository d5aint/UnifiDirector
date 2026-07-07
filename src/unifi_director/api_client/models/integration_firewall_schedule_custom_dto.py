from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_firewall_schedule_custom_dto_repeat_on_days_item import (
    IntegrationFirewallScheduleCustomDtoRepeatOnDaysItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_schedule_time import FirewallScheduleTime


T = TypeVar("T", bound="IntegrationFirewallScheduleCustomDto")


@_attrs_define
class IntegrationFirewallScheduleCustomDto:
    """
    Attributes:
        mode (str):
        repeat_on_days (list[IntegrationFirewallScheduleCustomDtoRepeatOnDaysItem]):
        start_date (datetime.date): Date in YYYY-MM-DD format. ISO 8601 compliant. Example: 2025-12-31.
        stop_date (datetime.date): Date in YYYY-MM-DD format. ISO 8601 compliant. Example: 2025-12-31.
        time_filter (FirewallScheduleTime | Unset): Defines the time range when the entity is active. If null, the
            entity is active all day.
    """

    mode: str
    repeat_on_days: list[IntegrationFirewallScheduleCustomDtoRepeatOnDaysItem]
    start_date: datetime.date
    stop_date: datetime.date
    time_filter: FirewallScheduleTime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        repeat_on_days = []
        for repeat_on_days_item_data in self.repeat_on_days:
            repeat_on_days_item = repeat_on_days_item_data.value
            repeat_on_days.append(repeat_on_days_item)

        start_date = self.start_date.isoformat()

        stop_date = self.stop_date.isoformat()

        time_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_filter, Unset):
            time_filter = self.time_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "repeatOnDays": repeat_on_days,
                "startDate": start_date,
                "stopDate": stop_date,
            }
        )
        if time_filter is not UNSET:
            field_dict["timeFilter"] = time_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_schedule_time import FirewallScheduleTime

        d = dict(src_dict)
        mode = d.pop("mode")

        repeat_on_days = []
        _repeat_on_days = d.pop("repeatOnDays")
        for repeat_on_days_item_data in _repeat_on_days:
            repeat_on_days_item = IntegrationFirewallScheduleCustomDtoRepeatOnDaysItem(repeat_on_days_item_data)

            repeat_on_days.append(repeat_on_days_item)

        start_date = datetime.date.fromisoformat(d.pop("startDate"))

        stop_date = datetime.date.fromisoformat(d.pop("stopDate"))

        _time_filter = d.pop("timeFilter", UNSET)
        time_filter: FirewallScheduleTime | Unset
        if isinstance(_time_filter, Unset):
            time_filter = UNSET
        else:
            time_filter = FirewallScheduleTime.from_dict(_time_filter)

        integration_firewall_schedule_custom_dto = cls(
            mode=mode,
            repeat_on_days=repeat_on_days,
            start_date=start_date,
            stop_date=stop_date,
            time_filter=time_filter,
        )

        integration_firewall_schedule_custom_dto.additional_properties = d
        return integration_firewall_schedule_custom_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
