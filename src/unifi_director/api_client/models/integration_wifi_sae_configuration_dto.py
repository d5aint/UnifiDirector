from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationWifiSaeConfigurationDto")


@_attrs_define
class IntegrationWifiSaeConfigurationDto:
    """
    Attributes:
        anticlogging_threshold_seconds (int):
        sync_time_seconds (int):
    """

    anticlogging_threshold_seconds: int
    sync_time_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anticlogging_threshold_seconds = self.anticlogging_threshold_seconds

        sync_time_seconds = self.sync_time_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anticloggingThresholdSeconds": anticlogging_threshold_seconds,
                "syncTimeSeconds": sync_time_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        anticlogging_threshold_seconds = d.pop("anticloggingThresholdSeconds")

        sync_time_seconds = d.pop("syncTimeSeconds")

        integration_wifi_sae_configuration_dto = cls(
            anticlogging_threshold_seconds=anticlogging_threshold_seconds,
            sync_time_seconds=sync_time_seconds,
        )

        integration_wifi_sae_configuration_dto.additional_properties = d
        return integration_wifi_sae_configuration_dto

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
