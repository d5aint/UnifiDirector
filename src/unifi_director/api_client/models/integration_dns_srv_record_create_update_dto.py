from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationDnsSrvRecordCreateUpdateDto")


@_attrs_define
class IntegrationDnsSrvRecordCreateUpdateDto:
    """
    Attributes:
        type_ (str):
        enabled (bool):
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
    enabled: bool
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

        enabled = self.enabled

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
                "enabled": enabled,
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
        d = dict(src_dict)
        type_ = d.pop("type")

        enabled = d.pop("enabled")

        domain = d.pop("domain")

        server_domain = d.pop("serverDomain")

        service = d.pop("service")

        protocol = d.pop("protocol")

        port = d.pop("port")

        priority = d.pop("priority")

        weight = d.pop("weight")

        integration_dns_srv_record_create_update_dto = cls(
            type_=type_,
            enabled=enabled,
            domain=domain,
            server_domain=server_domain,
            service=service,
            protocol=protocol,
            port=port,
            priority=priority,
            weight=weight,
        )

        integration_dns_srv_record_create_update_dto.additional_properties = d
        return integration_dns_srv_record_create_update_dto

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
