from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FirewallPolicyIPv6InterfaceIdentifierFilter")


@_attrs_define
class FirewallPolicyIPv6InterfaceIdentifierFilter:
    """
    Attributes:
        ipv_6_iid (str): IPv6 Interface Identifier. Example: 2001:db8::1/::ffff:ffff:ffff:ffff.
        match_opposite (bool): Match on all IPv6 IIDs except the specified one.
    """

    ipv_6_iid: str
    match_opposite: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_6_iid = self.ipv_6_iid

        match_opposite = self.match_opposite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv6Iid": ipv_6_iid,
                "matchOpposite": match_opposite,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ipv_6_iid = d.pop("ipv6Iid")

        match_opposite = d.pop("matchOpposite")

        firewall_policy_i_pv_6_interface_identifier_filter = cls(
            ipv_6_iid=ipv_6_iid,
            match_opposite=match_opposite,
        )

        firewall_policy_i_pv_6_interface_identifier_filter.additional_properties = d
        return firewall_policy_i_pv_6_interface_identifier_filter

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
