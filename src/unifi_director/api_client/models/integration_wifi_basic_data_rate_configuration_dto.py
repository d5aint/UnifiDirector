from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_wifi_basic_data_rate_configuration_dto_5 import IntegrationWifiBasicDataRateConfigurationDto5
from ..models.integration_wifi_basic_data_rate_configuration_dto_24 import (
    IntegrationWifiBasicDataRateConfigurationDto24,
)

T = TypeVar("T", bound="IntegrationWifiBasicDataRateConfigurationDto")


@_attrs_define
class IntegrationWifiBasicDataRateConfigurationDto:
    """
    Attributes:
        field_2_4 (IntegrationWifiBasicDataRateConfigurationDto24):  Example: 2000.
        field_5 (IntegrationWifiBasicDataRateConfigurationDto5):  Example: 6000.
    """

    field_2_4: IntegrationWifiBasicDataRateConfigurationDto24
    field_5: IntegrationWifiBasicDataRateConfigurationDto5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_2_4 = self.field_2_4.value

        field_5 = self.field_5.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "2.4": field_2_4,
                "5": field_5,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_2_4 = IntegrationWifiBasicDataRateConfigurationDto24(d.pop("2.4"))

        field_5 = IntegrationWifiBasicDataRateConfigurationDto5(d.pop("5"))

        integration_wifi_basic_data_rate_configuration_dto = cls(
            field_2_4=field_2_4,
            field_5=field_5,
        )

        integration_wifi_basic_data_rate_configuration_dto.additional_properties = d
        return integration_wifi_basic_data_rate_configuration_dto

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
