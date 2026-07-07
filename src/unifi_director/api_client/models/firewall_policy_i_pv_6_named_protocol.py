from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_policy_i_pv_6_named_protocol_name import FirewallPolicyIPv6NamedProtocolName
from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallPolicyIPv6NamedProtocol")


@_attrs_define
class FirewallPolicyIPv6NamedProtocol:
    """Defines rules for matching by protocol name.

    Attributes:
        name (FirewallPolicyIPv6NamedProtocolName | Unset):
    """

    name: FirewallPolicyIPv6NamedProtocolName | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: FirewallPolicyIPv6NamedProtocolName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = FirewallPolicyIPv6NamedProtocolName(_name)

        firewall_policy_i_pv_6_named_protocol = cls(
            name=name,
        )

        firewall_policy_i_pv_6_named_protocol.additional_properties = d
        return firewall_policy_i_pv_6_named_protocol

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
