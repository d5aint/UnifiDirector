from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_wifi_radius_mac_authentication_configuration_dto import (
        IntegrationWifiRadiusMacAuthenticationConfigurationDto,
    )
    from ..models.wifi_radius_nasid_configuration import WifiRadiusNASIDConfiguration


T = TypeVar("T", bound="IntegrationWifiEnterpriseRadiusConfigurationDto")


@_attrs_define
class IntegrationWifiEnterpriseRadiusConfigurationDto:
    """
    Attributes:
        profile_id (UUID):
        nas_id (WifiRadiusNASIDConfiguration):
        mac_authentication_configuration (IntegrationWifiRadiusMacAuthenticationConfigurationDto | Unset):
    """

    profile_id: UUID
    nas_id: WifiRadiusNASIDConfiguration
    mac_authentication_configuration: IntegrationWifiRadiusMacAuthenticationConfigurationDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = str(self.profile_id)

        nas_id = self.nas_id.to_dict()

        mac_authentication_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mac_authentication_configuration, Unset):
            mac_authentication_configuration = self.mac_authentication_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileId": profile_id,
                "nasId": nas_id,
            }
        )
        if mac_authentication_configuration is not UNSET:
            field_dict["macAuthenticationConfiguration"] = mac_authentication_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_wifi_radius_mac_authentication_configuration_dto import (
            IntegrationWifiRadiusMacAuthenticationConfigurationDto,
        )
        from ..models.wifi_radius_nasid_configuration import WifiRadiusNASIDConfiguration

        d = dict(src_dict)
        profile_id = UUID(d.pop("profileId"))

        nas_id = WifiRadiusNASIDConfiguration.from_dict(d.pop("nasId"))

        _mac_authentication_configuration = d.pop("macAuthenticationConfiguration", UNSET)
        mac_authentication_configuration: IntegrationWifiRadiusMacAuthenticationConfigurationDto | Unset
        if isinstance(_mac_authentication_configuration, Unset):
            mac_authentication_configuration = UNSET
        else:
            mac_authentication_configuration = IntegrationWifiRadiusMacAuthenticationConfigurationDto.from_dict(
                _mac_authentication_configuration
            )

        integration_wifi_enterprise_radius_configuration_dto = cls(
            profile_id=profile_id,
            nas_id=nas_id,
            mac_authentication_configuration=mac_authentication_configuration,
        )

        integration_wifi_enterprise_radius_configuration_dto.additional_properties = d
        return integration_wifi_enterprise_radius_configuration_dto

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
