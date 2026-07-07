from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_wifi_wpa_2_personal_security_configuration_detail_dto_pmf_mode import (
    IntegrationWifiWpa2PersonalSecurityConfigurationDetailDtoPmfMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_wifi_non_enterprise_radius_configuration_dto import (
        IntegrationWifiNonEnterpriseRadiusConfigurationDto,
    )
    from ..models.integration_wifi_preshared_key_dto import IntegrationWifiPresharedKeyDto


T = TypeVar("T", bound="IntegrationWifiWpa2PersonalSecurityConfigurationDetailDto")


@_attrs_define
class IntegrationWifiWpa2PersonalSecurityConfigurationDetailDto:
    """
    Attributes:
        type_ (str):
        radius_configuration (IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset):
        group_rekey_interval_seconds (int | Unset): Group rekey interval in seconds. Sets how often connected device
            groups are assigned a new key. If null, then it is disabled. This feature is not available for IoT
            configuration.
        fast_roaming_enabled (bool | Unset): Fast roaming enabled flag. This feature is not available for IoT
            configuration.
        passphrase (str | Unset):
        preshared_keys (list[IntegrationWifiPresharedKeyDto] | Unset):
        pmf_mode (IntegrationWifiWpa2PersonalSecurityConfigurationDetailDtoPmfMode | Unset): Protected Management Frames
            mode. If null, then it is disabled. This feature is not available for IoT configuration.
    """

    type_: str
    radius_configuration: IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset = UNSET
    group_rekey_interval_seconds: int | Unset = UNSET
    fast_roaming_enabled: bool | Unset = UNSET
    passphrase: str | Unset = UNSET
    preshared_keys: list[IntegrationWifiPresharedKeyDto] | Unset = UNSET
    pmf_mode: IntegrationWifiWpa2PersonalSecurityConfigurationDetailDtoPmfMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        radius_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius_configuration, Unset):
            radius_configuration = self.radius_configuration.to_dict()

        group_rekey_interval_seconds = self.group_rekey_interval_seconds

        fast_roaming_enabled = self.fast_roaming_enabled

        passphrase = self.passphrase

        preshared_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.preshared_keys, Unset):
            preshared_keys = []
            for preshared_keys_item_data in self.preshared_keys:
                preshared_keys_item = preshared_keys_item_data.to_dict()
                preshared_keys.append(preshared_keys_item)

        pmf_mode: str | Unset = UNSET
        if not isinstance(self.pmf_mode, Unset):
            pmf_mode = self.pmf_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if radius_configuration is not UNSET:
            field_dict["radiusConfiguration"] = radius_configuration
        if group_rekey_interval_seconds is not UNSET:
            field_dict["groupRekeyIntervalSeconds"] = group_rekey_interval_seconds
        if fast_roaming_enabled is not UNSET:
            field_dict["fastRoamingEnabled"] = fast_roaming_enabled
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase
        if preshared_keys is not UNSET:
            field_dict["presharedKeys"] = preshared_keys
        if pmf_mode is not UNSET:
            field_dict["pmfMode"] = pmf_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_wifi_non_enterprise_radius_configuration_dto import (
            IntegrationWifiNonEnterpriseRadiusConfigurationDto,
        )
        from ..models.integration_wifi_preshared_key_dto import IntegrationWifiPresharedKeyDto

        d = dict(src_dict)
        type_ = d.pop("type")

        _radius_configuration = d.pop("radiusConfiguration", UNSET)
        radius_configuration: IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset
        if isinstance(_radius_configuration, Unset):
            radius_configuration = UNSET
        else:
            radius_configuration = IntegrationWifiNonEnterpriseRadiusConfigurationDto.from_dict(_radius_configuration)

        group_rekey_interval_seconds = d.pop("groupRekeyIntervalSeconds", UNSET)

        fast_roaming_enabled = d.pop("fastRoamingEnabled", UNSET)

        passphrase = d.pop("passphrase", UNSET)

        _preshared_keys = d.pop("presharedKeys", UNSET)
        preshared_keys: list[IntegrationWifiPresharedKeyDto] | Unset = UNSET
        if _preshared_keys is not UNSET:
            preshared_keys = []
            for preshared_keys_item_data in _preshared_keys:
                preshared_keys_item = IntegrationWifiPresharedKeyDto.from_dict(preshared_keys_item_data)

                preshared_keys.append(preshared_keys_item)

        _pmf_mode = d.pop("pmfMode", UNSET)
        pmf_mode: IntegrationWifiWpa2PersonalSecurityConfigurationDetailDtoPmfMode | Unset
        if isinstance(_pmf_mode, Unset):
            pmf_mode = UNSET
        else:
            pmf_mode = IntegrationWifiWpa2PersonalSecurityConfigurationDetailDtoPmfMode(_pmf_mode)

        integration_wifi_wpa_2_personal_security_configuration_detail_dto = cls(
            type_=type_,
            radius_configuration=radius_configuration,
            group_rekey_interval_seconds=group_rekey_interval_seconds,
            fast_roaming_enabled=fast_roaming_enabled,
            passphrase=passphrase,
            preshared_keys=preshared_keys,
            pmf_mode=pmf_mode,
        )

        integration_wifi_wpa_2_personal_security_configuration_detail_dto.additional_properties = d
        return integration_wifi_wpa_2_personal_security_configuration_detail_dto

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
