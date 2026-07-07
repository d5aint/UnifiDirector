from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_defined_or_derived_entity_metadata import UserDefinedOrDerivedEntityMetadata


T = TypeVar("T", bound="VPNServerOverview")


@_attrs_define
class VPNServerOverview:
    """
    Attributes:
        type_ (str):
        id (UUID):
        name (str):
        enabled (bool):
        metadata (UserDefinedOrDerivedEntityMetadata):
    """

    type_: str
    id: UUID
    name: str
    enabled: bool
    metadata: UserDefinedOrDerivedEntityMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = str(self.id)

        name = self.name

        enabled = self.enabled

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "enabled": enabled,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_defined_or_derived_entity_metadata import UserDefinedOrDerivedEntityMetadata

        d = dict(src_dict)
        type_ = d.pop("type")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        enabled = d.pop("enabled")

        metadata = UserDefinedOrDerivedEntityMetadata.from_dict(d.pop("metadata"))

        vpn_server_overview = cls(
            type_=type_,
            id=id,
            name=name,
            enabled=enabled,
            metadata=metadata,
        )

        vpn_server_overview.additional_properties = d
        return vpn_server_overview

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
