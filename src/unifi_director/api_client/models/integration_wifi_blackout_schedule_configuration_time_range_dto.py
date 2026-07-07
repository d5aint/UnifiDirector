from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationWifiBlackoutScheduleConfigurationTimeRangeDto")


@_attrs_define
class IntegrationWifiBlackoutScheduleConfigurationTimeRangeDto:
    """
    Attributes:
        start_time (str): Start time in 24-hour format (HH:mm)
        end_time (str): End time in 24-hour format (HH:mm)
    """

    start_time: str
    end_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startTime": start_time,
                "endTime": end_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        integration_wifi_blackout_schedule_configuration_time_range_dto = cls(
            start_time=start_time,
            end_time=end_time,
        )

        integration_wifi_blackout_schedule_configuration_time_range_dto.additional_properties = d
        return integration_wifi_blackout_schedule_configuration_time_range_dto

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
