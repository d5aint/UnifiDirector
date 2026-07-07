from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_managed_i_pv_4dhcp_configuration import GatewayManagedIPv4DHCPConfiguration
    from ..models.wannat_outbound_configuration import WANNATOutboundConfiguration


T = TypeVar("T", bound="GatewayManagedIPv4Configuration")


@_attrs_define
class GatewayManagedIPv4Configuration:
    """
    Attributes:
        auto_scale_enabled (bool): Whether the Network can automatically scale its subnet size based on the number of
            active DHCP leases.
        host_ip_address (str):
        prefix_length (int):
        additional_host_ip_subnets (list[str] | Unset): Additional host IP subnets assigned to this VLAN.
        dhcp_configuration (GatewayManagedIPv4DHCPConfiguration | Unset):
        nat_outbound_ip_address_configuration (list[WANNATOutboundConfiguration] | Unset): List of NAT Outbound
            Configurations defining which IP addresses are used for NAT translation. This array must contain all WAN
            interfaces with `static` or `PPPoE` IPv4 connection configuration.
    """

    auto_scale_enabled: bool
    host_ip_address: str
    prefix_length: int
    additional_host_ip_subnets: list[str] | Unset = UNSET
    dhcp_configuration: GatewayManagedIPv4DHCPConfiguration | Unset = UNSET
    nat_outbound_ip_address_configuration: list[WANNATOutboundConfiguration] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_scale_enabled = self.auto_scale_enabled

        host_ip_address = self.host_ip_address

        prefix_length = self.prefix_length

        additional_host_ip_subnets: list[str] | Unset = UNSET
        if not isinstance(self.additional_host_ip_subnets, Unset):
            additional_host_ip_subnets = self.additional_host_ip_subnets

        dhcp_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_configuration, Unset):
            dhcp_configuration = self.dhcp_configuration.to_dict()

        nat_outbound_ip_address_configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nat_outbound_ip_address_configuration, Unset):
            nat_outbound_ip_address_configuration = []
            for nat_outbound_ip_address_configuration_item_data in self.nat_outbound_ip_address_configuration:
                nat_outbound_ip_address_configuration_item = nat_outbound_ip_address_configuration_item_data.to_dict()
                nat_outbound_ip_address_configuration.append(nat_outbound_ip_address_configuration_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoScaleEnabled": auto_scale_enabled,
                "hostIpAddress": host_ip_address,
                "prefixLength": prefix_length,
            }
        )
        if additional_host_ip_subnets is not UNSET:
            field_dict["additionalHostIpSubnets"] = additional_host_ip_subnets
        if dhcp_configuration is not UNSET:
            field_dict["dhcpConfiguration"] = dhcp_configuration
        if nat_outbound_ip_address_configuration is not UNSET:
            field_dict["natOutboundIpAddressConfiguration"] = nat_outbound_ip_address_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_managed_i_pv_4dhcp_configuration import GatewayManagedIPv4DHCPConfiguration
        from ..models.wannat_outbound_configuration import WANNATOutboundConfiguration

        d = dict(src_dict)
        auto_scale_enabled = d.pop("autoScaleEnabled")

        host_ip_address = d.pop("hostIpAddress")

        prefix_length = d.pop("prefixLength")

        additional_host_ip_subnets = cast(list[str], d.pop("additionalHostIpSubnets", UNSET))

        _dhcp_configuration = d.pop("dhcpConfiguration", UNSET)
        dhcp_configuration: GatewayManagedIPv4DHCPConfiguration | Unset
        if isinstance(_dhcp_configuration, Unset):
            dhcp_configuration = UNSET
        else:
            dhcp_configuration = GatewayManagedIPv4DHCPConfiguration.from_dict(_dhcp_configuration)

        _nat_outbound_ip_address_configuration = d.pop("natOutboundIpAddressConfiguration", UNSET)
        nat_outbound_ip_address_configuration: list[WANNATOutboundConfiguration] | Unset = UNSET
        if _nat_outbound_ip_address_configuration is not UNSET:
            nat_outbound_ip_address_configuration = []
            for nat_outbound_ip_address_configuration_item_data in _nat_outbound_ip_address_configuration:
                nat_outbound_ip_address_configuration_item = WANNATOutboundConfiguration.from_dict(
                    nat_outbound_ip_address_configuration_item_data
                )

                nat_outbound_ip_address_configuration.append(nat_outbound_ip_address_configuration_item)

        gateway_managed_i_pv_4_configuration = cls(
            auto_scale_enabled=auto_scale_enabled,
            host_ip_address=host_ip_address,
            prefix_length=prefix_length,
            additional_host_ip_subnets=additional_host_ip_subnets,
            dhcp_configuration=dhcp_configuration,
            nat_outbound_ip_address_configuration=nat_outbound_ip_address_configuration,
        )

        gateway_managed_i_pv_4_configuration.additional_properties = d
        return gateway_managed_i_pv_4_configuration

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
