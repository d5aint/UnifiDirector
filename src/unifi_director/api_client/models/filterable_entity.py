from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_path import FilterPath
    from ..models.filterable_entity_nested_entities import FilterableEntityNestedEntities
    from ..models.filterable_entity_properties import FilterableEntityProperties


T = TypeVar("T", bound="FilterableEntity")


@_attrs_define
class FilterableEntity:
    """
    Attributes:
        path (FilterPath | Unset):
        properties (FilterableEntityProperties | Unset):
        nested_entities (FilterableEntityNestedEntities | Unset):
        name (str | Unset):
    """

    path: FilterPath | Unset = UNSET
    properties: FilterableEntityProperties | Unset = UNSET
    nested_entities: FilterableEntityNestedEntities | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        nested_entities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nested_entities, Unset):
            nested_entities = self.nested_entities.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if properties is not UNSET:
            field_dict["properties"] = properties
        if nested_entities is not UNSET:
            field_dict["nestedEntities"] = nested_entities
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_path import FilterPath
        from ..models.filterable_entity_nested_entities import FilterableEntityNestedEntities
        from ..models.filterable_entity_properties import FilterableEntityProperties

        d = dict(src_dict)
        _path = d.pop("path", UNSET)
        path: FilterPath | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = FilterPath.from_dict(_path)

        _properties = d.pop("properties", UNSET)
        properties: FilterableEntityProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = FilterableEntityProperties.from_dict(_properties)

        _nested_entities = d.pop("nestedEntities", UNSET)
        nested_entities: FilterableEntityNestedEntities | Unset
        if isinstance(_nested_entities, Unset):
            nested_entities = UNSET
        else:
            nested_entities = FilterableEntityNestedEntities.from_dict(_nested_entities)

        name = d.pop("name", UNSET)

        filterable_entity = cls(
            path=path,
            properties=properties,
            nested_entities=nested_entities,
            name=name,
        )

        filterable_entity.additional_properties = d
        return filterable_entity

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
