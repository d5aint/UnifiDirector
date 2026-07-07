from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FirewallScheduleTime")


@_attrs_define
class FirewallScheduleTime:
    """Defines the time range when the entity is active. If null, the entity is active all day.

    Attributes:
        start_time (str): Time in HH:MM format. Uses 24-hour clock system. ISO 8601 compliant. Example: 21:37.
        stop_time (str): Time in HH:MM format. Uses 24-hour clock system. ISO 8601 compliant. Example: 21:37.
    """

    start_time: str
    stop_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        stop_time = self.stop_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startTime": start_time,
                "stopTime": stop_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("startTime")

        stop_time = d.pop("stopTime")

        firewall_schedule_time = cls(
            start_time=start_time,
            stop_time=stop_time,
        )

        firewall_schedule_time.additional_properties = d
        return firewall_schedule_time

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
