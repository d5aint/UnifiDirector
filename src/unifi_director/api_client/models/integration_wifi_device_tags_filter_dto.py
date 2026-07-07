from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationWifiDeviceTagsFilterDto")


@_attrs_define
class IntegrationWifiDeviceTagsFilterDto:
    """
    Attributes:
        type_ (str):
        device_tag_ids (list[UUID]):
    """

    type_: str
    device_tag_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        device_tag_ids = []
        for device_tag_ids_item_data in self.device_tag_ids:
            device_tag_ids_item = str(device_tag_ids_item_data)
            device_tag_ids.append(device_tag_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "deviceTagIds": device_tag_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        device_tag_ids = []
        _device_tag_ids = d.pop("deviceTagIds")
        for device_tag_ids_item_data in _device_tag_ids:
            device_tag_ids_item = UUID(device_tag_ids_item_data)

            device_tag_ids.append(device_tag_ids_item)

        integration_wifi_device_tags_filter_dto = cls(
            type_=type_,
            device_tag_ids=device_tag_ids,
        )

        integration_wifi_device_tags_filter_dto.additional_properties = d
        return integration_wifi_device_tags_filter_dto

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
