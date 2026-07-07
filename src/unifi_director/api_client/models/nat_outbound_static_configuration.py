from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_address_selector_lower import IPAddressSelectorLower


T = TypeVar("T", bound="NATOutboundStaticConfiguration")


@_attrs_define
class NATOutboundStaticConfiguration:
    """
    Attributes:
        type_ (str):
        wan_interface_id (UUID):
        ip_address_selectors (list[IPAddressSelectorLower]): List of IP addresses or address ranges which determines
            which IP addresses will be used to translate the traffic on network using NAT.
    """

    type_: str
    wan_interface_id: UUID
    ip_address_selectors: list[IPAddressSelectorLower]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        wan_interface_id = str(self.wan_interface_id)

        ip_address_selectors = []
        for ip_address_selectors_item_data in self.ip_address_selectors:
            ip_address_selectors_item = ip_address_selectors_item_data.to_dict()
            ip_address_selectors.append(ip_address_selectors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "wanInterfaceId": wan_interface_id,
                "ipAddressSelectors": ip_address_selectors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_address_selector_lower import IPAddressSelectorLower

        d = dict(src_dict)
        type_ = d.pop("type")

        wan_interface_id = UUID(d.pop("wanInterfaceId"))

        ip_address_selectors = []
        _ip_address_selectors = d.pop("ipAddressSelectors")
        for ip_address_selectors_item_data in _ip_address_selectors:
            ip_address_selectors_item = IPAddressSelectorLower.from_dict(ip_address_selectors_item_data)

            ip_address_selectors.append(ip_address_selectors_item)

        nat_outbound_static_configuration = cls(
            type_=type_,
            wan_interface_id=wan_interface_id,
            ip_address_selectors=ip_address_selectors,
        )

        nat_outbound_static_configuration.additional_properties = d
        return nat_outbound_static_configuration

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
