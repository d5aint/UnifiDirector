from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IPv4DHCPRelayConfiguration")


@_attrs_define
class IPv4DHCPRelayConfiguration:
    """
    Attributes:
        mode (str):
        dhcp_server_ip_addresses (list[str]): DHCP Server IP addresses
    """

    mode: str
    dhcp_server_ip_addresses: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        dhcp_server_ip_addresses = self.dhcp_server_ip_addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "dhcpServerIpAddresses": dhcp_server_ip_addresses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = d.pop("mode")

        dhcp_server_ip_addresses = cast(list[str], d.pop("dhcpServerIpAddresses"))

        i_pv_4dhcp_relay_configuration = cls(
            mode=mode,
            dhcp_server_ip_addresses=dhcp_server_ip_addresses,
        )

        i_pv_4dhcp_relay_configuration.additional_properties = d
        return i_pv_4dhcp_relay_configuration

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
