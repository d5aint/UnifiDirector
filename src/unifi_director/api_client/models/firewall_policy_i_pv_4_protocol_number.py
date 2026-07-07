from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FirewallPolicyIPv4ProtocolNumber")


@_attrs_define
class FirewallPolicyIPv4ProtocolNumber:
    """Defines rules for matching by protocol number.

    Attributes:
        type_ (str):
        protocol_number (int): Protocol number as defined by IANA.
        match_opposite (bool): Match on all protocols except the specified protocol.
    """

    type_: str
    protocol_number: int
    match_opposite: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        protocol_number = self.protocol_number

        match_opposite = self.match_opposite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "protocolNumber": protocol_number,
                "matchOpposite": match_opposite,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        protocol_number = d.pop("protocolNumber")

        match_opposite = d.pop("matchOpposite")

        firewall_policy_i_pv_4_protocol_number = cls(
            type_=type_,
            protocol_number=protocol_number,
            match_opposite=match_opposite,
        )

        firewall_policy_i_pv_4_protocol_number.additional_properties = d
        return firewall_policy_i_pv_4_protocol_number

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
