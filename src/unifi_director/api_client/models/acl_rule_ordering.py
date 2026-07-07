from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ACLRuleOrdering")


@_attrs_define
class ACLRuleOrdering:
    """
    Attributes:
        ordered_acl_rule_ids (list[UUID]):
    """

    ordered_acl_rule_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordered_acl_rule_ids = []
        for ordered_acl_rule_ids_item_data in self.ordered_acl_rule_ids:
            ordered_acl_rule_ids_item = str(ordered_acl_rule_ids_item_data)
            ordered_acl_rule_ids.append(ordered_acl_rule_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderedAclRuleIds": ordered_acl_rule_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ordered_acl_rule_ids = []
        _ordered_acl_rule_ids = d.pop("orderedAclRuleIds")
        for ordered_acl_rule_ids_item_data in _ordered_acl_rule_ids:
            ordered_acl_rule_ids_item = UUID(ordered_acl_rule_ids_item_data)

            ordered_acl_rule_ids.append(ordered_acl_rule_ids_item)

        acl_rule_ordering = cls(
            ordered_acl_rule_ids=ordered_acl_rule_ids,
        )

        acl_rule_ordering.additional_properties = d
        return acl_rule_ordering

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
