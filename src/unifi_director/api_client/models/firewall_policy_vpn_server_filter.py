from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FirewallPolicyVPNServerFilter")


@_attrs_define
class FirewallPolicyVPNServerFilter:
    """
    Attributes:
        vpn_server_ids (list[UUID]):
        match_opposite (bool):
    """

    vpn_server_ids: list[UUID]
    match_opposite: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_server_ids = []
        for vpn_server_ids_item_data in self.vpn_server_ids:
            vpn_server_ids_item = str(vpn_server_ids_item_data)
            vpn_server_ids.append(vpn_server_ids_item)

        match_opposite = self.match_opposite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vpnServerIds": vpn_server_ids,
                "matchOpposite": match_opposite,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vpn_server_ids = []
        _vpn_server_ids = d.pop("vpnServerIds")
        for vpn_server_ids_item_data in _vpn_server_ids:
            vpn_server_ids_item = UUID(vpn_server_ids_item_data)

            vpn_server_ids.append(vpn_server_ids_item)

        match_opposite = d.pop("matchOpposite")

        firewall_policy_vpn_server_filter = cls(
            vpn_server_ids=vpn_server_ids,
            match_opposite=match_opposite,
        )

        firewall_policy_vpn_server_filter.additional_properties = d
        return firewall_policy_vpn_server_filter

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
