from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blackout_schedule_configuration_per_day_day import BlackoutScheduleConfigurationPerDayDay

if TYPE_CHECKING:
    from ..models.integration_wifi_blackout_schedule_configuration_time_range_dto import (
        IntegrationWifiBlackoutScheduleConfigurationTimeRangeDto,
    )


T = TypeVar("T", bound="IntegrationWifiBlackoutScheduleConfigurationPerDayWithTimeRangeDto")


@_attrs_define
class IntegrationWifiBlackoutScheduleConfigurationPerDayWithTimeRangeDto:
    """
    Attributes:
        type_ (str):
        day (BlackoutScheduleConfigurationPerDayDay):
        time_ranges (list[IntegrationWifiBlackoutScheduleConfigurationTimeRangeDto]):
    """

    type_: str
    day: BlackoutScheduleConfigurationPerDayDay
    time_ranges: list[IntegrationWifiBlackoutScheduleConfigurationTimeRangeDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        day = self.day.value

        time_ranges = []
        for time_ranges_item_data in self.time_ranges:
            time_ranges_item = time_ranges_item_data.to_dict()
            time_ranges.append(time_ranges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "day": day,
                "timeRanges": time_ranges,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_wifi_blackout_schedule_configuration_time_range_dto import (
            IntegrationWifiBlackoutScheduleConfigurationTimeRangeDto,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        day = BlackoutScheduleConfigurationPerDayDay(d.pop("day"))

        time_ranges = []
        _time_ranges = d.pop("timeRanges")
        for time_ranges_item_data in _time_ranges:
            time_ranges_item = IntegrationWifiBlackoutScheduleConfigurationTimeRangeDto.from_dict(time_ranges_item_data)

            time_ranges.append(time_ranges_item)

        integration_wifi_blackout_schedule_configuration_per_day_with_time_range_dto = cls(
            type_=type_,
            day=day,
            time_ranges=time_ranges,
        )

        integration_wifi_blackout_schedule_configuration_per_day_with_time_range_dto.additional_properties = d
        return integration_wifi_blackout_schedule_configuration_per_day_with_time_range_dto

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
