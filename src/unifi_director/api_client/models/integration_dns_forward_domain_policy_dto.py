from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata


T = TypeVar("T", bound="IntegrationDnsForwardDomainPolicyDto")


@_attrs_define
class IntegrationDnsForwardDomainPolicyDto:
    """
    Attributes:
        type_ (str):
        id (UUID):
        enabled (bool):
        metadata (UserDefinedEntityMetadata):
        domain (str):  Example: example.com.
        ip_address (str): IP address of the DNS Server that the DNS query is forwarded to. Example:
            8.8.4.4|2001:4860:4860::8844.
    """

    type_: str
    id: UUID
    enabled: bool
    metadata: UserDefinedEntityMetadata
    domain: str
    ip_address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = str(self.id)

        enabled = self.enabled

        metadata = self.metadata.to_dict()

        domain = self.domain

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "enabled": enabled,
                "metadata": metadata,
                "domain": domain,
                "ipAddress": ip_address,
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

        ip_address = d.pop("ipAddress")

        integration_dns_forward_domain_policy_dto = cls(
            type_=type_,
            id=id,
            enabled=enabled,
            metadata=metadata,
            domain=domain,
            ip_address=ip_address,
        )

        integration_dns_forward_domain_policy_dto.additional_properties = d
        return integration_dns_forward_domain_policy_dto

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
