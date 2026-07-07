from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ordered_firewall_policy_i_ds import OrderedFirewallPolicyIDs


T = TypeVar("T", bound="IntegrationFirewallPolicyOrderingDto")


@_attrs_define
class IntegrationFirewallPolicyOrderingDto:
    """
    Attributes:
        ordered_firewall_policy_ids (OrderedFirewallPolicyIDs):
    """

    ordered_firewall_policy_ids: OrderedFirewallPolicyIDs
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordered_firewall_policy_ids = self.ordered_firewall_policy_ids.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderedFirewallPolicyIds": ordered_firewall_policy_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ordered_firewall_policy_i_ds import OrderedFirewallPolicyIDs

        d = dict(src_dict)
        ordered_firewall_policy_ids = OrderedFirewallPolicyIDs.from_dict(d.pop("orderedFirewallPolicyIds"))

        integration_firewall_policy_ordering_dto = cls(
            ordered_firewall_policy_ids=ordered_firewall_policy_ids,
        )

        integration_firewall_policy_ordering_dto.additional_properties = d
        return integration_firewall_policy_ordering_dto

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
