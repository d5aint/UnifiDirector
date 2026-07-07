from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata


T = TypeVar("T", bound="IntegrationDnsARecordDto")


@_attrs_define
class IntegrationDnsARecordDto:
    """
    Attributes:
        type_ (str):
        id (UUID):
        enabled (bool):
        metadata (UserDefinedEntityMetadata):
        domain (str):  Example: example.com.
        ipv_4_address (str):  Example: 192.168.1.10.
        ttl_seconds (int): Time to live in seconds. Example: 14400.
    """

    type_: str
    id: UUID
    enabled: bool
    metadata: UserDefinedEntityMetadata
    domain: str
    ipv_4_address: str
    ttl_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = str(self.id)

        enabled = self.enabled

        metadata = self.metadata.to_dict()

        domain = self.domain

        ipv_4_address = self.ipv_4_address

        ttl_seconds = self.ttl_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "enabled": enabled,
                "metadata": metadata,
                "domain": domain,
                "ipv4Address": ipv_4_address,
                "ttlSeconds": ttl_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata

        d = dict(src_dict)
        type_ = d.pop("type")

        id = UUID(d.pop("id"))

        enabled = d.pop("enabled")

        metadata = UserDefinedEntityMetadata.from_dict(d.pop("metadata"))

        domain = d.pop("domain")

        ipv_4_address = d.pop("ipv4Address")

        ttl_seconds = d.pop("ttlSeconds")

        integration_dns_a_record_dto = cls(
            type_=type_,
            id=id,
            enabled=enabled,
            metadata=metadata,
            domain=domain,
            ipv_4_address=ipv_4_address,
            ttl_seconds=ttl_seconds,
        )

        integration_dns_a_record_dto.additional_properties = d
        return integration_dns_a_record_dto

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
