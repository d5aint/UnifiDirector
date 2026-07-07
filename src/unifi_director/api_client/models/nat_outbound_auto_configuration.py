from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nat_outbound_auto_configuration_ip_address_selection_mode import (
    NATOutboundAutoConfigurationIpAddressSelectionMode,
)

T = TypeVar("T", bound="NATOutboundAutoConfiguration")


@_attrs_define
class NATOutboundAutoConfiguration:
    """
    Attributes:
        type_ (str):
        wan_interface_id (UUID):
        ip_address_selection_mode (NATOutboundAutoConfigurationIpAddressSelectionMode): IP address selection mode which
            determines how the IP address will be selected from the group of IP addresses to translate the traffic on
            network using NAT.
    """

    type_: str
    wan_interface_id: UUID
    ip_address_selection_mode: NATOutboundAutoConfigurationIpAddressSelectionMode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        wan_interface_id = str(self.wan_interface_id)

        ip_address_selection_mode = self.ip_address_selection_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "wanInterfaceId": wan_interface_id,
                "ipAddressSelectionMode": ip_address_selection_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        wan_interface_id = UUID(d.pop("wanInterfaceId"))

        ip_address_selection_mode = NATOutboundAutoConfigurationIpAddressSelectionMode(d.pop("ipAddressSelectionMode"))

        nat_outbound_auto_configuration = cls(
            type_=type_,
            wan_interface_id=wan_interface_id,
            ip_address_selection_mode=ip_address_selection_mode,
        )

        nat_outbound_auto_configuration.additional_properties = d
        return nat_outbound_auto_configuration

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
