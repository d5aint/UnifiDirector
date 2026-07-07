from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_configuration_for_i_pv_6_network import DHCPConfigurationForIPv6Network


T = TypeVar("T", bound="IPv6ClientAddressAssignment")


@_attrs_define
class IPv6ClientAddressAssignment:
    """
    Attributes:
        slaac_enabled (bool): Allows devices to obtain IPv6 addresses via SLAAC (Stateless Address Autoconfiguration)
            without DHCPv6. At least one addressing method must be active: either enable SLAAC or provide DHCP
            configuration.
        dhcp_configuration (DHCPConfigurationForIPv6Network | Unset):
    """

    slaac_enabled: bool
    dhcp_configuration: DHCPConfigurationForIPv6Network | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slaac_enabled = self.slaac_enabled

        dhcp_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_configuration, Unset):
            dhcp_configuration = self.dhcp_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slaacEnabled": slaac_enabled,
            }
        )
        if dhcp_configuration is not UNSET:
            field_dict["dhcpConfiguration"] = dhcp_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_configuration_for_i_pv_6_network import DHCPConfigurationForIPv6Network

        d = dict(src_dict)
        slaac_enabled = d.pop("slaacEnabled")

        _dhcp_configuration = d.pop("dhcpConfiguration", UNSET)
        dhcp_configuration: DHCPConfigurationForIPv6Network | Unset
        if isinstance(_dhcp_configuration, Unset):
            dhcp_configuration = UNSET
        else:
            dhcp_configuration = DHCPConfigurationForIPv6Network.from_dict(_dhcp_configuration)

        i_pv_6_client_address_assignment = cls(
            slaac_enabled=slaac_enabled,
            dhcp_configuration=dhcp_configuration,
        )

        i_pv_6_client_address_assignment.additional_properties = d
        return i_pv_6_client_address_assignment

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
