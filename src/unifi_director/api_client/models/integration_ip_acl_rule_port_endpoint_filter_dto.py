from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationIpAclRulePortEndpointFilterDto")


@_attrs_define
class IntegrationIpAclRulePortEndpointFilterDto:
    """
    Attributes:
        type_ (str):
        port_filter (list[int]): Ports this ACL rule will be applied to.
    """

    type_: str
    port_filter: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        port_filter = self.port_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "portFilter": port_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        port_filter = cast(list[int], d.pop("portFilter"))

        integration_ip_acl_rule_port_endpoint_filter_dto = cls(
            type_=type_,
            port_filter=port_filter,
        )

        integration_ip_acl_rule_port_endpoint_filter_dto.additional_properties = d
        return integration_ip_acl_rule_port_endpoint_filter_dto

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
