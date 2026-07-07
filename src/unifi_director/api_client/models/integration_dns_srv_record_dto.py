from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata


T = TypeVar("T", bound="IntegrationDnsSrvRecordDto")


@_attrs_define
class IntegrationDnsSrvRecordDto:
    """
    Attributes:
        type_ (str):
        id (UUID):
        enabled (bool):
        metadata (UserDefinedEntityMetadata):
        domain (str):  Example: example.com.
        server_domain (str): Domain of the server that is running the service. Example: server.example.com.
        service (str): Service associated with this SRV record. Example: _ldap.
        protocol (str): Protocol used by the service. Example: _tcp.
        port (int):
        priority (int): Priority. A lower number is preferred. Example: 255.
        weight (int): Weight. A relative value applicable for records with the same priority. A lower number is
            preferred. Example: 128.
    """

    type_: str
    id: UUID
    enabled: bool
    metadata: UserDefinedEntityMetadata
    domain: str
    server_domain: str
    service: str
    protocol: str
    port: int
    priority: int
    weight: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = str(self.id)

        enabled = self.enabled

        metadata = self.metadata.to_dict()

        domain = self.domain

        server_domain = self.server_domain

        service = self.service

        protocol = self.protocol

        port = self.port

        priority = self.priority

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "enabled": enabled,
                "metadata": metadata,
                "domain": domain,
                "serverDomain": server_domain,
                "service": service,
                "protocol": protocol,
                "port": port,
                "priority": priority,
                "weight": weight,
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

        server_domain = d.pop("serverDomain")

        service = d.pop("service")

        protocol = d.pop("protocol")

        port = d.pop("port")

        priority = d.pop("priority")

        weight = d.pop("weight")

        integration_dns_srv_record_dto = cls(
            type_=type_,
            id=id,
            enabled=enabled,
            metadata=metadata,
            domain=domain,
            server_domain=server_domain,
            service=service,
            protocol=protocol,
            port=port,
            priority=priority,
            weight=weight,
        )

        integration_dns_srv_record_dto.additional_properties = d
        return integration_dns_srv_record_dto

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
