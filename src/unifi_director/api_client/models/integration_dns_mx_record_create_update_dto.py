from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationDnsMxRecordCreateUpdateDto")


@_attrs_define
class IntegrationDnsMxRecordCreateUpdateDto:
    """
    Attributes:
        type_ (str):
        enabled (bool):
        domain (str):  Example: example.com.
        mail_server_domain (str):  Example: mail.example.com.
        priority (int): Priority. A lower number is preferred. Example: 255.
    """

    type_: str
    enabled: bool
    domain: str
    mail_server_domain: str
    priority: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        enabled = self.enabled

        domain = self.domain

        mail_server_domain = self.mail_server_domain

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "enabled": enabled,
                "domain": domain,
                "mailServerDomain": mail_server_domain,
                "priority": priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        enabled = d.pop("enabled")

        domain = d.pop("domain")

        mail_server_domain = d.pop("mailServerDomain")

        priority = d.pop("priority")

        integration_dns_mx_record_create_update_dto = cls(
            type_=type_,
            enabled=enabled,
            domain=domain,
            mail_server_domain=mail_server_domain,
            priority=priority,
        )

        integration_dns_mx_record_create_update_dto.additional_properties = d
        return integration_dns_mx_record_create_update_dto

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
