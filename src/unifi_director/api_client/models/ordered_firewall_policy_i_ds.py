from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderedFirewallPolicyIDs")


@_attrs_define
class OrderedFirewallPolicyIDs:
    """
    Attributes:
        before_system_defined (list[UUID]):
        after_system_defined (list[UUID]):
    """

    before_system_defined: list[UUID]
    after_system_defined: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        before_system_defined = []
        for before_system_defined_item_data in self.before_system_defined:
            before_system_defined_item = str(before_system_defined_item_data)
            before_system_defined.append(before_system_defined_item)

        after_system_defined = []
        for after_system_defined_item_data in self.after_system_defined:
            after_system_defined_item = str(after_system_defined_item_data)
            after_system_defined.append(after_system_defined_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "beforeSystemDefined": before_system_defined,
                "afterSystemDefined": after_system_defined,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        before_system_defined = []
        _before_system_defined = d.pop("beforeSystemDefined")
        for before_system_defined_item_data in _before_system_defined:
            before_system_defined_item = UUID(before_system_defined_item_data)

            before_system_defined.append(before_system_defined_item)

        after_system_defined = []
        _after_system_defined = d.pop("afterSystemDefined")
        for after_system_defined_item_data in _after_system_defined:
            after_system_defined_item = UUID(after_system_defined_item_data)

            after_system_defined.append(after_system_defined_item)

        ordered_firewall_policy_i_ds = cls(
            before_system_defined=before_system_defined,
            after_system_defined=after_system_defined,
        )

        ordered_firewall_policy_i_ds.additional_properties = d
        return ordered_firewall_policy_i_ds

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
