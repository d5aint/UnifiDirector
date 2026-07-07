from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blackout_schedule_configuration_per_day_day import BlackoutScheduleConfigurationPerDayDay

T = TypeVar("T", bound="BlackoutScheduleConfigurationPerDay")


@_attrs_define
class BlackoutScheduleConfigurationPerDay:
    """
    Attributes:
        type_ (str):
        day (BlackoutScheduleConfigurationPerDayDay):
    """

    type_: str
    day: BlackoutScheduleConfigurationPerDayDay
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        day = self.day.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "day": day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        day = BlackoutScheduleConfigurationPerDayDay(d.pop("day"))

        blackout_schedule_configuration_per_day = cls(
            type_=type_,
            day=day,
        )

        blackout_schedule_configuration_per_day.additional_properties = d
        return blackout_schedule_configuration_per_day

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
