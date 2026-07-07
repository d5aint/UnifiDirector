from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_policy_region_filter_regions_item import FirewallPolicyRegionFilterRegionsItem

T = TypeVar("T", bound="FirewallPolicyRegionFilter")


@_attrs_define
class FirewallPolicyRegionFilter:
    """
    Attributes:
        regions (list[FirewallPolicyRegionFilterRegionsItem]): Match traffic originating from selected regions. Regions
            are identified by their ISO 3166-1 alpha-2 country codes.
    """

    regions: list[FirewallPolicyRegionFilterRegionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.value
            regions.append(regions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regions": regions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = FirewallPolicyRegionFilterRegionsItem(regions_item_data)

            regions.append(regions_item)

        firewall_policy_region_filter = cls(
            regions=regions,
        )

        firewall_policy_region_filter.additional_properties = d
        return firewall_policy_region_filter

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
