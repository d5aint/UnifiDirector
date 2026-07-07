from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_wifi_non_enterprise_radius_configuration_dto import (
        IntegrationWifiNonEnterpriseRadiusConfigurationDto,
    )
    from ..models.integration_wifi_sae_configuration_dto import IntegrationWifiSaeConfigurationDto


T = TypeVar("T", bound="IntegrationWifiWpa3PersonalSecurityConfigurationDetailDto")


@_attrs_define
class IntegrationWifiWpa3PersonalSecurityConfigurationDetailDto:
    """
    Attributes:
        type_ (str):
        passphrase (str):
        sae_configuration (IntegrationWifiSaeConfigurationDto):
        radius_configuration (IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset):
        group_rekey_interval_seconds (int | Unset): Group rekey interval in seconds. Sets how often connected device
            groups are assigned a new key. If null, then it is disabled. This feature is not available for IoT
            configuration.
        fast_roaming_enabled (bool | Unset): Fast roaming enabled flag. This feature is not available for IoT
            configuration.
    """

    type_: str
    passphrase: str
    sae_configuration: IntegrationWifiSaeConfigurationDto
    radius_configuration: IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset = UNSET
    group_rekey_interval_seconds: int | Unset = UNSET
    fast_roaming_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        passphrase = self.passphrase

        sae_configuration = self.sae_configuration.to_dict()

        radius_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius_configuration, Unset):
            radius_configuration = self.radius_configuration.to_dict()

        group_rekey_interval_seconds = self.group_rekey_interval_seconds

        fast_roaming_enabled = self.fast_roaming_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "passphrase": passphrase,
                "saeConfiguration": sae_configuration,
            }
        )
        if radius_configuration is not UNSET:
            field_dict["radiusConfiguration"] = radius_configuration
        if group_rekey_interval_seconds is not UNSET:
            field_dict["groupRekeyIntervalSeconds"] = group_rekey_interval_seconds
        if fast_roaming_enabled is not UNSET:
            field_dict["fastRoamingEnabled"] = fast_roaming_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_wifi_non_enterprise_radius_configuration_dto import (
            IntegrationWifiNonEnterpriseRadiusConfigurationDto,
        )
        from ..models.integration_wifi_sae_configuration_dto import IntegrationWifiSaeConfigurationDto

        d = dict(src_dict)
        type_ = d.pop("type")

        passphrase = d.pop("passphrase")

        sae_configuration = IntegrationWifiSaeConfigurationDto.from_dict(d.pop("saeConfiguration"))

        _radius_configuration = d.pop("radiusConfiguration", UNSET)
        radius_configuration: IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset
        if isinstance(_radius_configuration, Unset):
            radius_configuration = UNSET
        else:
            radius_configuration = IntegrationWifiNonEnterpriseRadiusConfigurationDto.from_dict(_radius_configuration)

        group_rekey_interval_seconds = d.pop("groupRekeyIntervalSeconds", UNSET)

        fast_roaming_enabled = d.pop("fastRoamingEnabled", UNSET)

        integration_wifi_wpa_3_personal_security_configuration_detail_dto = cls(
            type_=type_,
            passphrase=passphrase,
            sae_configuration=sae_configuration,
            radius_configuration=radius_configuration,
            group_rekey_interval_seconds=group_rekey_interval_seconds,
            fast_roaming_enabled=fast_roaming_enabled,
        )

        integration_wifi_wpa_3_personal_security_configuration_detail_dto.additional_properties = d
        return integration_wifi_wpa_3_personal_security_configuration_detail_dto

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
