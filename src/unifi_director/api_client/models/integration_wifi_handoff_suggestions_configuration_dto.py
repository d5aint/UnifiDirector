from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegrationWifiHandoffSuggestionsConfigurationDto")


@_attrs_define
class IntegrationWifiHandoffSuggestionsConfigurationDto:
    """
    Attributes:
        band_5g_hz_rssi_threshold (int | Unset): RSSI threshold (dBm) for the 5 GHz band. If null, then it is disabled.
        band_6g_hz_rssi_threshold (int | Unset): RSSI threshold (dBm) for the 6 GHz band. If null, then it is disabled.
    """

    band_5g_hz_rssi_threshold: int | Unset = UNSET
    band_6g_hz_rssi_threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        band_5g_hz_rssi_threshold = self.band_5g_hz_rssi_threshold

        band_6g_hz_rssi_threshold = self.band_6g_hz_rssi_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if band_5g_hz_rssi_threshold is not UNSET:
            field_dict["band5GHzRssiThreshold"] = band_5g_hz_rssi_threshold
        if band_6g_hz_rssi_threshold is not UNSET:
            field_dict["band6GHzRssiThreshold"] = band_6g_hz_rssi_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        band_5g_hz_rssi_threshold = d.pop("band5GHzRssiThreshold", UNSET)

        band_6g_hz_rssi_threshold = d.pop("band6GHzRssiThreshold", UNSET)

        integration_wifi_handoff_suggestions_configuration_dto = cls(
            band_5g_hz_rssi_threshold=band_5g_hz_rssi_threshold,
            band_6g_hz_rssi_threshold=band_6g_hz_rssi_threshold,
        )

        integration_wifi_handoff_suggestions_configuration_dto.additional_properties = d
        return integration_wifi_handoff_suggestions_configuration_dto

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
