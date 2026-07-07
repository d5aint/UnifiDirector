from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.port_matching import PortMatching


T = TypeVar("T", bound="IntegrationPortTrafficMatchingListCreateUpdateDto")


@_attrs_define
class IntegrationPortTrafficMatchingListCreateUpdateDto:
    """
    Attributes:
        type_ (str):
        name (str):  Example: Allowed port list|Protected IP list.
        items (list[PortMatching]):
    """

    type_: str
    name: str
    items: list[PortMatching]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.port_matching import PortMatching

        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = PortMatching.from_dict(items_item_data)

            items.append(items_item)

        integration_port_traffic_matching_list_create_update_dto = cls(
            type_=type_,
            name=name,
            items=items,
        )

        integration_port_traffic_matching_list_create_update_dto.additional_properties = d
        return integration_port_traffic_matching_list_create_update_dto

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
