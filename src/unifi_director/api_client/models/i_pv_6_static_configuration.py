from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_pv_6_client_address_assignment import IPv6ClientAddressAssignment
    from ..models.router_advertisement_configuration import RouterAdvertisementConfiguration


T = TypeVar("T", bound="IPv6StaticConfiguration")


@_attrs_define
class IPv6StaticConfiguration:
    """
    Attributes:
        interface_type (str):
        client_address_assignment (IPv6ClientAddressAssignment):
        host_ip_address (str): The static IPv6 address assigned to this Network.
        prefix_length (int):
        router_advertisement (RouterAdvertisementConfiguration | Unset):
        dns_server_ip_addresses_override (list[str] | Unset): The IPv6 DNS server addresses assigned to this Network. If
            none are specified, they will be selected automatically.
        additional_host_ip_subnets (list[str] | Unset): Additional host IP subnets assigned to this VLAN.
    """

    interface_type: str
    client_address_assignment: IPv6ClientAddressAssignment
    host_ip_address: str
    prefix_length: int
    router_advertisement: RouterAdvertisementConfiguration | Unset = UNSET
    dns_server_ip_addresses_override: list[str] | Unset = UNSET
    additional_host_ip_subnets: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_type = self.interface_type

        client_address_assignment = self.client_address_assignment.to_dict()

        host_ip_address = self.host_ip_address

        prefix_length = self.prefix_length

        router_advertisement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.router_advertisement, Unset):
            router_advertisement = self.router_advertisement.to_dict()

        dns_server_ip_addresses_override: list[str] | Unset = UNSET
        if not isinstance(self.dns_server_ip_addresses_override, Unset):
            dns_server_ip_addresses_override = self.dns_server_ip_addresses_override

        additional_host_ip_subnets: list[str] | Unset = UNSET
        if not isinstance(self.additional_host_ip_subnets, Unset):
            additional_host_ip_subnets = self.additional_host_ip_subnets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaceType": interface_type,
                "clientAddressAssignment": client_address_assignment,
                "hostIpAddress": host_ip_address,
                "prefixLength": prefix_length,
            }
        )
        if router_advertisement is not UNSET:
            field_dict["routerAdvertisement"] = router_advertisement
        if dns_server_ip_addresses_override is not UNSET:
            field_dict["dnsServerIpAddressesOverride"] = dns_server_ip_addresses_override
        if additional_host_ip_subnets is not UNSET:
            field_dict["additionalHostIpSubnets"] = additional_host_ip_subnets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_pv_6_client_address_assignment import IPv6ClientAddressAssignment
        from ..models.router_advertisement_configuration import RouterAdvertisementConfiguration

        d = dict(src_dict)
        interface_type = d.pop("interfaceType")

        client_address_assignment = IPv6ClientAddressAssignment.from_dict(d.pop("clientAddressAssignment"))

        host_ip_address = d.pop("hostIpAddress")

        prefix_length = d.pop("prefixLength")

        _router_advertisement = d.pop("routerAdvertisement", UNSET)
        router_advertisement: RouterAdvertisementConfiguration | Unset
        if isinstance(_router_advertisement, Unset):
            router_advertisement = UNSET
        else:
            router_advertisement = RouterAdvertisementConfiguration.from_dict(_router_advertisement)

        dns_server_ip_addresses_override = cast(list[str], d.pop("dnsServerIpAddressesOverride", UNSET))

        additional_host_ip_subnets = cast(list[str], d.pop("additionalHostIpSubnets", UNSET))

        i_pv_6_static_configuration = cls(
            interface_type=interface_type,
            client_address_assignment=client_address_assignment,
            host_ip_address=host_ip_address,
            prefix_length=prefix_length,
            router_advertisement=router_advertisement,
            dns_server_ip_addresses_override=dns_server_ip_addresses_override,
            additional_host_ip_subnets=additional_host_ip_subnets,
        )

        i_pv_6_static_configuration.additional_properties = d
        return i_pv_6_static_configuration

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
