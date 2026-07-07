from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterPath")


@_attrs_define
class FilterPath:
    """
    Attributes:
        name (str | Unset):
        parent (Any | Unset):
        depth (int | Unset):
        names (list[str] | Unset):
    """

    name: str | Unset = UNSET
    parent: Any | Unset = UNSET
    depth: int | Unset = UNSET
    names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent = self.parent

        depth = self.depth

        names: list[str] | Unset = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if depth is not UNSET:
            field_dict["depth"] = depth
        if names is not UNSET:
            field_dict["names"] = names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        parent = d.pop("parent", UNSET)

        depth = d.pop("depth", UNSET)

        names = cast(list[str], d.pop("names", UNSET))

        filter_path = cls(
            name=name,
            parent=parent,
            depth=depth,
            names=names,
        )

        filter_path.additional_properties = d
        return filter_path

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
