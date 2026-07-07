from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_wifi_wpa_3_enterprise_security_configuration_detail_dto_security_mode import (
    IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDtoSecurityMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_wifi_enterprise_radius_configuration_dto import (
        IntegrationWifiEnterpriseRadiusConfigurationDto,
    )


T = TypeVar("T", bound="IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDto")


@_attrs_define
class IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDto:
    """
    Attributes:
        type_ (str):
        radius_configuration (IntegrationWifiEnterpriseRadiusConfigurationDto):
        coa_enabled (bool): Indicates whether Change of Authorization (COA) is enabled
        security_mode (IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDtoSecurityMode):
        group_rekey_interval_seconds (int | Unset): Group rekey interval in seconds. Sets how often connected device
            groups are assigned a new key. If null, then it is disabled. This feature is not available for IoT
            configuration.
        fast_roaming_enabled (bool | Unset): Fast roaming enabled flag. This feature is not available for IoT
            configuration.
    """

    type_: str
    radius_configuration: IntegrationWifiEnterpriseRadiusConfigurationDto
    coa_enabled: bool
    security_mode: IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDtoSecurityMode
    group_rekey_interval_seconds: int | Unset = UNSET
    fast_roaming_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        radius_configuration = self.radius_configuration.to_dict()

        coa_enabled = self.coa_enabled

        security_mode = self.security_mode.value

        group_rekey_interval_seconds = self.group_rekey_interval_seconds

        fast_roaming_enabled = self.fast_roaming_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "radiusConfiguration": radius_configuration,
                "coaEnabled": coa_enabled,
                "securityMode": security_mode,
            }
        )
        if group_rekey_interval_seconds is not UNSET:
            field_dict["groupRekeyIntervalSeconds"] = group_rekey_interval_seconds
        if fast_roaming_enabled is not UNSET:
            field_dict["fastRoamingEnabled"] = fast_roaming_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_wifi_enterprise_radius_configuration_dto import (
            IntegrationWifiEnterpriseRadiusConfigurationDto,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        radius_configuration = IntegrationWifiEnterpriseRadiusConfigurationDto.from_dict(d.pop("radiusConfiguration"))

        coa_enabled = d.pop("coaEnabled")

        security_mode = IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDtoSecurityMode(d.pop("securityMode"))

        group_rekey_interval_seconds = d.pop("groupRekeyIntervalSeconds", UNSET)

        fast_roaming_enabled = d.pop("fastRoamingEnabled", UNSET)

        integration_wifi_wpa_3_enterprise_security_configuration_detail_dto = cls(
            type_=type_,
            radius_configuration=radius_configuration,
            coa_enabled=coa_enabled,
            security_mode=security_mode,
            group_rekey_interval_seconds=group_rekey_interval_seconds,
            fast_roaming_enabled=fast_roaming_enabled,
        )

        integration_wifi_wpa_3_enterprise_security_configuration_detail_dto.additional_properties = d
        return integration_wifi_wpa_3_enterprise_security_configuration_detail_dto

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
