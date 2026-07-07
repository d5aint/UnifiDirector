from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_or_system_defined_or_orchestrated_entity_metadata import (
        UserOrSystemDefinedOrOrchestratedEntityMetadata,
    )


T = TypeVar("T", bound="SwitchManagedNetworkOverview")


@_attrs_define
class SwitchManagedNetworkOverview:
    """
    Attributes:
        management (str):
        id (UUID):
        name (str):  Example: Default Network.
        enabled (bool):
        vlan_id (int): VLAN ID. Must be 1 for the default network and >= 2 for additional networks.
        metadata (UserOrSystemDefinedOrOrchestratedEntityMetadata):
        default (bool):
        device_id (UUID): ID of the switch this Network is managed by. Example: 550e8400-e29b-41d4-a716-446655440000.
    """

    management: str
    id: UUID
    name: str
    enabled: bool
    vlan_id: int
    metadata: UserOrSystemDefinedOrOrchestratedEntityMetadata
    default: bool
    device_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        management = self.management

        id = str(self.id)

        name = self.name

        enabled = self.enabled

        vlan_id = self.vlan_id

        metadata = self.metadata.to_dict()

        default = self.default

        device_id = str(self.device_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "management": management,
                "id": id,
                "name": name,
                "enabled": enabled,
                "vlanId": vlan_id,
                "metadata": metadata,
                "default": default,
                "deviceId": device_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_or_system_defined_or_orchestrated_entity_metadata import (
            UserOrSystemDefinedOrOrchestratedEntityMetadata,
        )

        d = dict(src_dict)
        management = d.pop("management")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        enabled = d.pop("enabled")

        vlan_id = d.pop("vlanId")

        metadata = UserOrSystemDefinedOrOrchestratedEntityMetadata.from_dict(d.pop("metadata"))

        default = d.pop("default")

        device_id = UUID(d.pop("deviceId"))

        switch_managed_network_overview = cls(
            management=management,
            id=id,
            name=name,
            enabled=enabled,
            vlan_id=vlan_id,
            metadata=metadata,
            default=default,
            device_id=device_id,
        )

        switch_managed_network_overview.additional_properties = d
        return switch_managed_network_overview

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
