from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_or_orchestrated_entity_metadata import UserOrOrchestratedEntityMetadata


T = TypeVar("T", bound="DeviceTag")


@_attrs_define
class DeviceTag:
    """
    Attributes:
        id (UUID):
        name (str):
        device_ids (list[UUID]):
        metadata (UserOrOrchestratedEntityMetadata):
    """

    id: UUID
    name: str
    device_ids: list[UUID]
    metadata: UserOrOrchestratedEntityMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        device_ids = []
        for device_ids_item_data in self.device_ids:
            device_ids_item = str(device_ids_item_data)
            device_ids.append(device_ids_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "deviceIds": device_ids,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_or_orchestrated_entity_metadata import UserOrOrchestratedEntityMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        device_ids = []
        _device_ids = d.pop("deviceIds")
        for device_ids_item_data in _device_ids:
            device_ids_item = UUID(device_ids_item_data)

            device_ids.append(device_ids_item)

        metadata = UserOrOrchestratedEntityMetadata.from_dict(d.pop("metadata"))

        device_tag = cls(
            id=id,
            name=name,
            device_ids=device_ids,
            metadata=metadata,
        )

        device_tag.additional_properties = d
        return device_tag

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
