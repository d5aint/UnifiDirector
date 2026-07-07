from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationWifiDevicesFilterDto")


@_attrs_define
class IntegrationWifiDevicesFilterDto:
    """
    Attributes:
        type_ (str):
        device_ids (list[UUID]): List of Access Point capable device IDs to which the WiFi broadcast applies.
    """

    type_: str
    device_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        device_ids = []
        for device_ids_item_data in self.device_ids:
            device_ids_item = str(device_ids_item_data)
            device_ids.append(device_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "deviceIds": device_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        device_ids = []
        _device_ids = d.pop("deviceIds")
        for device_ids_item_data in _device_ids:
            device_ids_item = UUID(device_ids_item_data)

            device_ids.append(device_ids_item)

        integration_wifi_devices_filter_dto = cls(
            type_=type_,
            device_ids=device_ids,
        )

        integration_wifi_devices_filter_dto.additional_properties = d
        return integration_wifi_devices_filter_dto

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
