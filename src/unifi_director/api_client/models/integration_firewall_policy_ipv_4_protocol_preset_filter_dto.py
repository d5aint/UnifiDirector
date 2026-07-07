from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.firewall_policy_i_pv_4_protocol_preset import FirewallPolicyIPv4ProtocolPreset


T = TypeVar("T", bound="IntegrationFirewallPolicyIpv4ProtocolPresetFilterDto")


@_attrs_define
class IntegrationFirewallPolicyIpv4ProtocolPresetFilterDto:
    """
    Attributes:
        type_ (str):
        preset (FirewallPolicyIPv4ProtocolPreset): Defines rules for matching by protocol preset.
    """

    type_: str
    preset: FirewallPolicyIPv4ProtocolPreset
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        preset = self.preset.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "preset": preset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_policy_i_pv_4_protocol_preset import FirewallPolicyIPv4ProtocolPreset

        d = dict(src_dict)
        type_ = d.pop("type")

        preset = FirewallPolicyIPv4ProtocolPreset.from_dict(d.pop("preset"))

        integration_firewall_policy_ipv_4_protocol_preset_filter_dto = cls(
            type_=type_,
            preset=preset,
        )

        integration_firewall_policy_ipv_4_protocol_preset_filter_dto.additional_properties = d
        return integration_firewall_policy_ipv_4_protocol_preset_filter_dto

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
