from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationWifiMdnsProxyCustomServiceDto")


@_attrs_define
class IntegrationWifiMdnsProxyCustomServiceDto:
    """
    Attributes:
        type_ (str):
        name (str):
        type_domain (str):
    """

    type_: str
    name: str
    type_domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        type_domain = self.type_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "typeDomain": type_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        type_domain = d.pop("typeDomain")

        integration_wifi_mdns_proxy_custom_service_dto = cls(
            type_=type_,
            name=name,
            type_domain=type_domain,
        )

        integration_wifi_mdns_proxy_custom_service_dto.additional_properties = d
        return integration_wifi_mdns_proxy_custom_service_dto

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
