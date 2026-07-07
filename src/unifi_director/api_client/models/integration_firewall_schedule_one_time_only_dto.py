from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.firewall_schedule_time import FirewallScheduleTime


T = TypeVar("T", bound="IntegrationFirewallScheduleOneTimeOnlyDto")


@_attrs_define
class IntegrationFirewallScheduleOneTimeOnlyDto:
    """
    Attributes:
        mode (str):
        time_filter (FirewallScheduleTime): Defines the time range when the entity is active. If null, the entity is
            active all day.
        date (datetime.date): Date in YYYY-MM-DD format. ISO 8601 compliant. Example: 2025-12-31.
    """

    mode: str
    time_filter: FirewallScheduleTime
    date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        time_filter = self.time_filter.to_dict()

        date = self.date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "timeFilter": time_filter,
                "date": date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_schedule_time import FirewallScheduleTime

        d = dict(src_dict)
        mode = d.pop("mode")

        time_filter = FirewallScheduleTime.from_dict(d.pop("timeFilter"))

        date = datetime.date.fromisoformat(d.pop("date"))

        integration_firewall_schedule_one_time_only_dto = cls(
            mode=mode,
            time_filter=time_filter,
            date=date,
        )

        integration_firewall_schedule_one_time_only_dto.additional_properties = d
        return integration_firewall_schedule_one_time_only_dto

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
