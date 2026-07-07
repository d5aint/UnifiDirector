from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationDnsTxtRecordCreateUpdateDto")


@_attrs_define
class IntegrationDnsTxtRecordCreateUpdateDto:
    """
    Attributes:
        type_ (str):
        enabled (bool):
        domain (str):  Example: example.com.
        text (str): The text value associated with this TXT DNS record. Text can contain up to four 255-character
            strings. Lines containing commas must be enclosed in double quotes ("). Example: This is an example value of a
            TXT DNS Record..
    """

    type_: str
    enabled: bool
    domain: str
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        enabled = self.enabled

        domain = self.domain

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "enabled": enabled,
                "domain": domain,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        enabled = d.pop("enabled")

        domain = d.pop("domain")

        text = d.pop("text")

        integration_dns_txt_record_create_update_dto = cls(
            type_=type_,
            enabled=enabled,
            domain=domain,
            text=text,
        )

        integration_dns_txt_record_create_update_dto.additional_properties = d
        return integration_dns_txt_record_create_update_dto

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
