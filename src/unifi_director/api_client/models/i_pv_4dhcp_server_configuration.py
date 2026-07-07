from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_address_range import IPAddressRange


T = TypeVar("T", bound="IPv4DHCPServerConfiguration")


@_attrs_define
class IPv4DHCPServerConfiguration:
    """
    Attributes:
        mode (str):
        ip_address_range (IPAddressRange):
        lease_time_seconds (int): The lease time in seconds for addresses in this range.
        gateway_ip_address_override (str | Unset): Gateway IP address provided to DHCP clients. If null, the default
            gateway will be assigned.
        dns_server_ip_addresses_override (list[str] | Unset): List of DNS servers assigned to client devices by the DHCP
            server. If none are specified, they will be selected automatically.
        domain_name (str | Unset): Domain name that can be used to access network in the browser.
    """

    mode: str
    ip_address_range: IPAddressRange
    lease_time_seconds: int
    gateway_ip_address_override: str | Unset = UNSET
    dns_server_ip_addresses_override: list[str] | Unset = UNSET
    domain_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        ip_address_range = self.ip_address_range.to_dict()

        lease_time_seconds = self.lease_time_seconds

        gateway_ip_address_override = self.gateway_ip_address_override

        dns_server_ip_addresses_override: list[str] | Unset = UNSET
        if not isinstance(self.dns_server_ip_addresses_override, Unset):
            dns_server_ip_addresses_override = self.dns_server_ip_addresses_override

        domain_name = self.domain_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "ipAddressRange": ip_address_range,
                "leaseTimeSeconds": lease_time_seconds,
            }
        )
        if gateway_ip_address_override is not UNSET:
            field_dict["gatewayIpAddressOverride"] = gateway_ip_address_override
        if dns_server_ip_addresses_override is not UNSET:
            field_dict["dnsServerIpAddressesOverride"] = dns_server_ip_addresses_override
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_address_range import IPAddressRange

        d = dict(src_dict)
        mode = d.pop("mode")

        ip_address_range = IPAddressRange.from_dict(d.pop("ipAddressRange"))

        lease_time_seconds = d.pop("leaseTimeSeconds")

        gateway_ip_address_override = d.pop("gatewayIpAddressOverride", UNSET)

        dns_server_ip_addresses_override = cast(list[str], d.pop("dnsServerIpAddressesOverride", UNSET))

        domain_name = d.pop("domainName", UNSET)

        i_pv_4dhcp_server_configuration = cls(
            mode=mode,
            ip_address_range=ip_address_range,
            lease_time_seconds=lease_time_seconds,
            gateway_ip_address_override=gateway_ip_address_override,
            dns_server_ip_addresses_override=dns_server_ip_addresses_override,
            domain_name=domain_name,
        )

        i_pv_4dhcp_server_configuration.additional_properties = d
        return i_pv_4dhcp_server_configuration

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
