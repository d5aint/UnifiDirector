from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata


T = TypeVar("T", bound="DNSPolicy")


@_attrs_define
class DNSPolicy:
    """
    Attributes:
        type_ (str):
        id (UUID):
        enabled (bool):
        metadata (UserDefinedEntityMetadata):
        domain (str | Unset):
    """

    type_: str
    id: UUID
    enabled: bool
    metadata: UserDefinedEntityMetadata
    domain: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = str(self.id)

        enabled = self.enabled

        metadata = self.metadata.to_dict()

        domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "enabled": enabled,
                "metadata": metadata,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata

        d = dict(src_dict)
        type_ = d.pop("type")

        id = UUID(d.pop("id"))

        enabled = d.pop("enabled")

        metadata = UserDefinedEntityMetadata.from_dict(d.pop("metadata"))

        domain = d.pop("domain", UNSET)

        dns_policy = cls(
            type_=type_,
            id=id,
            enabled=enabled,
            metadata=metadata,
            domain=domain,
        )

        dns_policy.additional_properties = d
        return dns_policy

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
