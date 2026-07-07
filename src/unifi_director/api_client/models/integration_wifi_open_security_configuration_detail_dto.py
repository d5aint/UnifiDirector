from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_wifi_open_security_configuration_detail_dto_encryption import (
    IntegrationWifiOpenSecurityConfigurationDetailDtoEncryption,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_wifi_non_enterprise_radius_configuration_dto import (
        IntegrationWifiNonEnterpriseRadiusConfigurationDto,
    )


T = TypeVar("T", bound="IntegrationWifiOpenSecurityConfigurationDetailDto")


@_attrs_define
class IntegrationWifiOpenSecurityConfigurationDetailDto:
    """
    Attributes:
        type_ (str):
        radius_configuration (IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset):
        encryption (IntegrationWifiOpenSecurityConfigurationDetailDtoEncryption | Unset): Encryption mode for open
            security. If null, plain open with no encryption.
    """

    type_: str
    radius_configuration: IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset = UNSET
    encryption: IntegrationWifiOpenSecurityConfigurationDetailDtoEncryption | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        radius_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius_configuration, Unset):
            radius_configuration = self.radius_configuration.to_dict()

        encryption: str | Unset = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if radius_configuration is not UNSET:
            field_dict["radiusConfiguration"] = radius_configuration
        if encryption is not UNSET:
            field_dict["encryption"] = encryption

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_wifi_non_enterprise_radius_configuration_dto import (
            IntegrationWifiNonEnterpriseRadiusConfigurationDto,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        _radius_configuration = d.pop("radiusConfiguration", UNSET)
        radius_configuration: IntegrationWifiNonEnterpriseRadiusConfigurationDto | Unset
        if isinstance(_radius_configuration, Unset):
            radius_configuration = UNSET
        else:
            radius_configuration = IntegrationWifiNonEnterpriseRadiusConfigurationDto.from_dict(_radius_configuration)

        _encryption = d.pop("encryption", UNSET)
        encryption: IntegrationWifiOpenSecurityConfigurationDetailDtoEncryption | Unset
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = IntegrationWifiOpenSecurityConfigurationDetailDtoEncryption(_encryption)

        integration_wifi_open_security_configuration_detail_dto = cls(
            type_=type_,
            radius_configuration=radius_configuration,
            encryption=encryption,
        )

        integration_wifi_open_security_configuration_detail_dto.additional_properties = d
        return integration_wifi_open_security_configuration_detail_dto

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
