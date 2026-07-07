from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationFirewallPolicyActionAllowDto")


@_attrs_define
class IntegrationFirewallPolicyActionAllowDto:
    """
    Attributes:
        type_ (str):
        allow_return_traffic (bool): Creates a derived policy for the mirrored firewall zone pair to automatically allow
            the return traffic.
    """

    type_: str
    allow_return_traffic: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        allow_return_traffic = self.allow_return_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "allowReturnTraffic": allow_return_traffic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        allow_return_traffic = d.pop("allowReturnTraffic")

        integration_firewall_policy_action_allow_dto = cls(
            type_=type_,
            allow_return_traffic=allow_return_traffic,
        )

        integration_firewall_policy_action_allow_dto.additional_properties = d
        return integration_firewall_policy_action_allow_dto

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
