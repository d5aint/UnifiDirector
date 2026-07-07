from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_wifi_radius_mac_authentication_configuration_dto_mac_address_format import (
    IntegrationWifiRadiusMacAuthenticationConfigurationDtoMacAddressFormat,
)

T = TypeVar("T", bound="IntegrationWifiRadiusMacAuthenticationConfigurationDto")


@_attrs_define
class IntegrationWifiRadiusMacAuthenticationConfigurationDto:
    """
    Attributes:
        mac_address_format (IntegrationWifiRadiusMacAuthenticationConfigurationDtoMacAddressFormat):
    """

    mac_address_format: IntegrationWifiRadiusMacAuthenticationConfigurationDtoMacAddressFormat
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac_address_format = self.mac_address_format.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "macAddressFormat": mac_address_format,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mac_address_format = IntegrationWifiRadiusMacAuthenticationConfigurationDtoMacAddressFormat(
            d.pop("macAddressFormat")
        )

        integration_wifi_radius_mac_authentication_configuration_dto = cls(
            mac_address_format=mac_address_format,
        )

        integration_wifi_radius_mac_authentication_configuration_dto.additional_properties = d
        return integration_wifi_radius_mac_authentication_configuration_dto

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
