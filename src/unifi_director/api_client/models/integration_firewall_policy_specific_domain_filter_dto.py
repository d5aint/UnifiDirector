from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationFirewallPolicySpecificDomainFilterDto")


@_attrs_define
class IntegrationFirewallPolicySpecificDomainFilterDto:
    """
    Attributes:
        type_ (str):
        domains (list[str]): List of domains to match.
    """

    type_: str
    domains: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        domains = self.domains

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "domains": domains,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        domains = cast(list[str], d.pop("domains"))

        integration_firewall_policy_specific_domain_filter_dto = cls(
            type_=type_,
            domains=domains,
        )

        integration_firewall_policy_specific_domain_filter_dto.additional_properties = d
        return integration_firewall_policy_specific_domain_filter_dto

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
