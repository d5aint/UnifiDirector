from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationDnsForwardDomainPolicyCreateUpdateDto")


@_attrs_define
class IntegrationDnsForwardDomainPolicyCreateUpdateDto:
    """
    Attributes:
        type_ (str):
        enabled (bool):
        domain (str):  Example: example.com.
        ip_address (str): IP address of the DNS Server that the DNS query is forwarded to. Example:
            8.8.4.4|2001:4860:4860::8844.
    """

    type_: str
    enabled: bool
    domain: str
    ip_address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        enabled = self.enabled

        domain = self.domain

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "enabled": enabled,
                "domain": domain,
                "ipAddress": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        enabled = d.pop("enabled")

        domain = d.pop("domain")

        ip_address = d.pop("ipAddress")

        integration_dns_forward_domain_policy_create_update_dto = cls(
            type_=type_,
            enabled=enabled,
            domain=domain,
            ip_address=ip_address,
        )

        integration_dns_forward_domain_policy_create_update_dto.additional_properties = d
        return integration_dns_forward_domain_policy_create_update_dto

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
