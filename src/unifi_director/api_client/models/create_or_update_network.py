from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_dhcp_guarding import NetworkDHCPGuarding


T = TypeVar("T", bound="CreateOrUpdateNetwork")


@_attrs_define
class CreateOrUpdateNetwork:
    """
    Attributes:
        management (str):
        name (str):  Example: Default Network.
        enabled (bool):
        vlan_id (int): VLAN ID. Must be 1 for the default network and >= 2 for additional networks.
        dhcp_guarding (NetworkDHCPGuarding | Unset): Details about DHCP Guarding settings for this Network.
    """

    management: str
    name: str
    enabled: bool
    vlan_id: int
    dhcp_guarding: NetworkDHCPGuarding | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        management = self.management

        name = self.name

        enabled = self.enabled

        vlan_id = self.vlan_id

        dhcp_guarding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_guarding, Unset):
            dhcp_guarding = self.dhcp_guarding.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "management": management,
                "name": name,
                "enabled": enabled,
                "vlanId": vlan_id,
            }
        )
        if dhcp_guarding is not UNSET:
            field_dict["dhcpGuarding"] = dhcp_guarding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_dhcp_guarding import NetworkDHCPGuarding

        d = dict(src_dict)
        management = d.pop("management")

        name = d.pop("name")

        enabled = d.pop("enabled")

        vlan_id = d.pop("vlanId")

        _dhcp_guarding = d.pop("dhcpGuarding", UNSET)
        dhcp_guarding: NetworkDHCPGuarding | Unset
        if isinstance(_dhcp_guarding, Unset):
            dhcp_guarding = UNSET
        else:
            dhcp_guarding = NetworkDHCPGuarding.from_dict(_dhcp_guarding)

        create_or_update_network = cls(
            management=management,
            name=name,
            enabled=enabled,
            vlan_id=vlan_id,
            dhcp_guarding=dhcp_guarding,
        )

        create_or_update_network.additional_properties = d
        return create_or_update_network

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
