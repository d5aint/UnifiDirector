from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.firewall_policy_i_pv_4_and_i_pv_6_named_protocol import FirewallPolicyIPv4AndIPv6NamedProtocol


T = TypeVar("T", bound="IntegrationFirewallPolicyIpv4AndIpv6NamedProtocolFilterDto")


@_attrs_define
class IntegrationFirewallPolicyIpv4AndIpv6NamedProtocolFilterDto:
    """
    Attributes:
        type_ (str):
        protocol (FirewallPolicyIPv4AndIPv6NamedProtocol): Defines rules for matching by protocol name.
        match_opposite (bool): Match on all protocols except the specified protocol.
    """

    type_: str
    protocol: FirewallPolicyIPv4AndIPv6NamedProtocol
    match_opposite: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        protocol = self.protocol.to_dict()

        match_opposite = self.match_opposite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "protocol": protocol,
                "matchOpposite": match_opposite,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_policy_i_pv_4_and_i_pv_6_named_protocol import FirewallPolicyIPv4AndIPv6NamedProtocol

        d = dict(src_dict)
        type_ = d.pop("type")

        protocol = FirewallPolicyIPv4AndIPv6NamedProtocol.from_dict(d.pop("protocol"))

        match_opposite = d.pop("matchOpposite")

        integration_firewall_policy_ipv_4_and_ipv_6_named_protocol_filter_dto = cls(
            type_=type_,
            protocol=protocol,
            match_opposite=match_opposite,
        )

        integration_firewall_policy_ipv_4_and_ipv_6_named_protocol_filter_dto.additional_properties = d
        return integration_firewall_policy_ipv_4_and_ipv_6_named_protocol_filter_dto

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
