from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_path import FilterPath
    from ..models.filterable_property_type import FilterablePropertyType


T = TypeVar("T", bound="FilterableProperty")


@_attrs_define
class FilterableProperty:
    """
    Attributes:
        path (FilterPath | Unset):
        type_ (FilterablePropertyType | Unset):
        name (str | Unset):
    """

    path: FilterPath | Unset = UNSET
    type_: FilterablePropertyType | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_path import FilterPath
        from ..models.filterable_property_type import FilterablePropertyType

        d = dict(src_dict)
        _path = d.pop("path", UNSET)
        path: FilterPath | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = FilterPath.from_dict(_path)

        _type_ = d.pop("type", UNSET)
        type_: FilterablePropertyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FilterablePropertyType.from_dict(_type_)

        name = d.pop("name", UNSET)

        filterable_property = cls(
            path=path,
            type_=type_,
            name=name,
        )

        filterable_property.additional_properties = d
        return filterable_property

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
