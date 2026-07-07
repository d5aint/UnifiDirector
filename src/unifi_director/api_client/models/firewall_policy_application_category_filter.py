from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FirewallPolicyApplicationCategoryFilter")


@_attrs_define
class FirewallPolicyApplicationCategoryFilter:
    """
    Attributes:
        application_category_ids (list[int]): Array of DPI Category IDs to match.
    """

    application_category_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_category_ids = self.application_category_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicationCategoryIds": application_category_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_category_ids = cast(list[int], d.pop("applicationCategoryIds"))

        firewall_policy_application_category_filter = cls(
            application_category_ids=application_category_ids,
        )

        firewall_policy_application_category_filter.additional_properties = d
        return firewall_policy_application_category_filter

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
