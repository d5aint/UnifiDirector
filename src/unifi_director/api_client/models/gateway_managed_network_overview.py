from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_or_system_defined_or_orchestrated_entity_metadata import (
        UserOrSystemDefinedOrOrchestratedEntityMetadata,
    )


T = TypeVar("T", bound="GatewayManagedNetworkOverview")


@_attrs_define
class GatewayManagedNetworkOverview:
    """
    Attributes:
        management (str):
        id (UUID):
        name (str):  Example: Default Network.
        enabled (bool):
        vlan_id (int): VLAN ID. Must be 1 for the default network and >= 2 for additional networks.
        metadata (UserOrSystemDefinedOrOrchestratedEntityMetadata):
        default (bool):
        zone_id (UUID | Unset):
    """

    management: str
    id: UUID
    name: str
    enabled: bool
    vlan_id: int
    metadata: UserOrSystemDefinedOrOrchestratedEntityMetadata
    default: bool
    zone_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        management = self.management

        id = str(self.id)

        name = self.name

        enabled = self.enabled

        vlan_id = self.vlan_id

        metadata = self.metadata.to_dict()

        default = self.default

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)

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
            }
        )
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id

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

        _zone_id = d.pop("zoneId", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id, Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)

        gateway_managed_network_overview = cls(
            management=management,
            id=id,
            name=name,
            enabled=enabled,
            vlan_id=vlan_id,
            metadata=metadata,
            default=default,
            zone_id=zone_id,
        )

        gateway_managed_network_overview.additional_properties = d
        return gateway_managed_network_overview

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
