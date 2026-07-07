from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_policy_i_pv_4_protocol import FirewallPolicyIPv4Protocol


T = TypeVar("T", bound="IntegrationFirewallPolicyIpv4ProtocolScopeDto")


@_attrs_define
class IntegrationFirewallPolicyIpv4ProtocolScopeDto:
    """
    Attributes:
        ip_version (str):
        protocol_filter (FirewallPolicyIPv4Protocol | Unset): Defines protocol matching. If null, matches all protocols.
    """

    ip_version: str
    protocol_filter: FirewallPolicyIPv4Protocol | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_version = self.ip_version

        protocol_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protocol_filter, Unset):
            protocol_filter = self.protocol_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipVersion": ip_version,
            }
        )
        if protocol_filter is not UNSET:
            field_dict["protocolFilter"] = protocol_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_policy_i_pv_4_protocol import FirewallPolicyIPv4Protocol

        d = dict(src_dict)
        ip_version = d.pop("ipVersion")

        _protocol_filter = d.pop("protocolFilter", UNSET)
        protocol_filter: FirewallPolicyIPv4Protocol | Unset
        if isinstance(_protocol_filter, Unset):
            protocol_filter = UNSET
        else:
            protocol_filter = FirewallPolicyIPv4Protocol.from_dict(_protocol_filter)

        integration_firewall_policy_ipv_4_protocol_scope_dto = cls(
            ip_version=ip_version,
            protocol_filter=protocol_filter,
        )

        integration_firewall_policy_ipv_4_protocol_scope_dto.additional_properties = d
        return integration_firewall_policy_ipv_4_protocol_scope_dto

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
