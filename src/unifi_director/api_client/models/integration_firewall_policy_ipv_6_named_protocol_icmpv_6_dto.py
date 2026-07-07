from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_policy_i_pv_6_named_protocol_name import FirewallPolicyIPv6NamedProtocolName
from ..models.integration_firewall_policy_ipv_6_named_protocol_icmpv_6_dto_typename_filter import (
    IntegrationFirewallPolicyIpv6NamedProtocolIcmpv6DtoTypenameFilter,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegrationFirewallPolicyIpv6NamedProtocolIcmpv6Dto")


@_attrs_define
class IntegrationFirewallPolicyIpv6NamedProtocolIcmpv6Dto:
    """
    Attributes:
        name (FirewallPolicyIPv6NamedProtocolName | Unset):
        typename_filter (IntegrationFirewallPolicyIpv6NamedProtocolIcmpv6DtoTypenameFilter | Unset): Match specific type
            of ICMPv6 traffic. If null, matches all types.
    """

    name: FirewallPolicyIPv6NamedProtocolName | Unset = UNSET
    typename_filter: IntegrationFirewallPolicyIpv6NamedProtocolIcmpv6DtoTypenameFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        typename_filter: str | Unset = UNSET
        if not isinstance(self.typename_filter, Unset):
            typename_filter = self.typename_filter.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if typename_filter is not UNSET:
            field_dict["typenameFilter"] = typename_filter

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

        _typename_filter = d.pop("typenameFilter", UNSET)
        typename_filter: IntegrationFirewallPolicyIpv6NamedProtocolIcmpv6DtoTypenameFilter | Unset
        if isinstance(_typename_filter, Unset):
            typename_filter = UNSET
        else:
            typename_filter = IntegrationFirewallPolicyIpv6NamedProtocolIcmpv6DtoTypenameFilter(_typename_filter)

        integration_firewall_policy_ipv_6_named_protocol_icmpv_6_dto = cls(
            name=name,
            typename_filter=typename_filter,
        )

        integration_firewall_policy_ipv_6_named_protocol_icmpv_6_dto.additional_properties = d
        return integration_firewall_policy_ipv_6_named_protocol_icmpv_6_dto

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
