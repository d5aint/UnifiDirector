from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegrationMacAclRuleMacAddressEndpointFilterDto")


@_attrs_define
class IntegrationMacAclRuleMacAddressEndpointFilterDto:
    """
    Attributes:
        type_ (str):
        mac_addresses (list[str]): Source/destination MAC addresses this ACL rule will apply to.
        prefix_length (int | Unset): MAC address prefix length. When null, full MAC address(-es) will be used.
    """

    type_: str
    mac_addresses: list[str]
    prefix_length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac_addresses = self.mac_addresses

        prefix_length = self.prefix_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "macAddresses": mac_addresses,
            }
        )
        if prefix_length is not UNSET:
            field_dict["prefixLength"] = prefix_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        mac_addresses = cast(list[str], d.pop("macAddresses"))

        prefix_length = d.pop("prefixLength", UNSET)

        integration_mac_acl_rule_mac_address_endpoint_filter_dto = cls(
            type_=type_,
            mac_addresses=mac_addresses,
            prefix_length=prefix_length,
        )

        integration_mac_acl_rule_mac_address_endpoint_filter_dto.additional_properties = d
        return integration_mac_acl_rule_mac_address_endpoint_filter_dto

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
