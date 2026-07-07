from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FirewallPolicyNetworkFilter")


@_attrs_define
class FirewallPolicyNetworkFilter:
    """
    Attributes:
        network_ids (list[UUID]): Array of Network IDs to match.
        match_opposite (bool): Match on all Networks except the selected.
    """

    network_ids: list[UUID]
    match_opposite: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_ids = []
        for network_ids_item_data in self.network_ids:
            network_ids_item = str(network_ids_item_data)
            network_ids.append(network_ids_item)

        match_opposite = self.match_opposite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networkIds": network_ids,
                "matchOpposite": match_opposite,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network_ids = []
        _network_ids = d.pop("networkIds")
        for network_ids_item_data in _network_ids:
            network_ids_item = UUID(network_ids_item_data)

            network_ids.append(network_ids_item)

        match_opposite = d.pop("matchOpposite")

        firewall_policy_network_filter = cls(
            network_ids=network_ids,
            match_opposite=match_opposite,
        )

        firewall_policy_network_filter.additional_properties = d
        return firewall_policy_network_filter

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
