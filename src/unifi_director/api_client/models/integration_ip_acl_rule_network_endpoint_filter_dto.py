from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegrationIpAclRuleNetworkEndpointFilterDto")


@_attrs_define
class IntegrationIpAclRuleNetworkEndpointFilterDto:
    """
    Attributes:
        type_ (str):
        network_ids (list[UUID]): Network IDs
        port_filter (list[int] | Unset): Ports this ACL rule will be applied to. If null, the rule will be applied to
            all ports.
    """

    type_: str
    network_ids: list[UUID]
    port_filter: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        network_ids = []
        for network_ids_item_data in self.network_ids:
            network_ids_item = str(network_ids_item_data)
            network_ids.append(network_ids_item)

        port_filter: list[int] | Unset = UNSET
        if not isinstance(self.port_filter, Unset):
            port_filter = self.port_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "networkIds": network_ids,
            }
        )
        if port_filter is not UNSET:
            field_dict["portFilter"] = port_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        network_ids = []
        _network_ids = d.pop("networkIds")
        for network_ids_item_data in _network_ids:
            network_ids_item = UUID(network_ids_item_data)

            network_ids.append(network_ids_item)

        port_filter = cast(list[int], d.pop("portFilter", UNSET))

        integration_ip_acl_rule_network_endpoint_filter_dto = cls(
            type_=type_,
            network_ids=network_ids,
            port_filter=port_filter,
        )

        integration_ip_acl_rule_network_endpoint_filter_dto.additional_properties = d
        return integration_ip_acl_rule_network_endpoint_filter_dto

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
