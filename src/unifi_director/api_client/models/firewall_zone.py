from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_or_system_defined_entity_metadata import UserOrSystemDefinedEntityMetadata


T = TypeVar("T", bound="FirewallZone")


@_attrs_define
class FirewallZone:
    """
    Attributes:
        id (UUID):  Example: ffcdb32c-6278-4364-8947-df4f77118df8.
        name (str): Name of a firewall zone Example: Hotspot|My custom zone.
        network_ids (list[UUID]): List of Network IDs
        metadata (UserOrSystemDefinedEntityMetadata):
    """

    id: UUID
    name: str
    network_ids: list[UUID]
    metadata: UserOrSystemDefinedEntityMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        network_ids = []
        for network_ids_item_data in self.network_ids:
            network_ids_item = str(network_ids_item_data)
            network_ids.append(network_ids_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "networkIds": network_ids,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_or_system_defined_entity_metadata import UserOrSystemDefinedEntityMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        network_ids = []
        _network_ids = d.pop("networkIds")
        for network_ids_item_data in _network_ids:
            network_ids_item = UUID(network_ids_item_data)

            network_ids.append(network_ids_item)

        metadata = UserOrSystemDefinedEntityMetadata.from_dict(d.pop("metadata"))

        firewall_zone = cls(
            id=id,
            name=name,
            network_ids=network_ids,
            metadata=metadata,
        )

        firewall_zone.additional_properties = d
        return firewall_zone

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
