from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filterable_property_type_allowed_functions_item import FilterablePropertyTypeAllowedFunctionsItem
from ..models.filterable_property_type_supported_functions_item import FilterablePropertyTypeSupportedFunctionsItem
from ..models.filterable_property_type_value_type import FilterablePropertyTypeValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterablePropertyType")


@_attrs_define
class FilterablePropertyType:
    """
    Attributes:
        allowed_functions (list[FilterablePropertyTypeAllowedFunctionsItem] | Unset):
        value_type (FilterablePropertyTypeValueType | Unset):
        supported_functions (list[FilterablePropertyTypeSupportedFunctionsItem] | Unset):
    """

    allowed_functions: list[FilterablePropertyTypeAllowedFunctionsItem] | Unset = UNSET
    value_type: FilterablePropertyTypeValueType | Unset = UNSET
    supported_functions: list[FilterablePropertyTypeSupportedFunctionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_functions: list[str] | Unset = UNSET
        if not isinstance(self.allowed_functions, Unset):
            allowed_functions = []
            for allowed_functions_item_data in self.allowed_functions:
                allowed_functions_item = allowed_functions_item_data.value
                allowed_functions.append(allowed_functions_item)

        value_type: str | Unset = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.value

        supported_functions: list[str] | Unset = UNSET
        if not isinstance(self.supported_functions, Unset):
            supported_functions = []
            for supported_functions_item_data in self.supported_functions:
                supported_functions_item = supported_functions_item_data.value
                supported_functions.append(supported_functions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_functions is not UNSET:
            field_dict["allowedFunctions"] = allowed_functions
        if value_type is not UNSET:
            field_dict["valueType"] = value_type
        if supported_functions is not UNSET:
            field_dict["supportedFunctions"] = supported_functions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _allowed_functions = d.pop("allowedFunctions", UNSET)
        allowed_functions: list[FilterablePropertyTypeAllowedFunctionsItem] | Unset = UNSET
        if _allowed_functions is not UNSET:
            allowed_functions = []
            for allowed_functions_item_data in _allowed_functions:
                allowed_functions_item = FilterablePropertyTypeAllowedFunctionsItem(allowed_functions_item_data)

                allowed_functions.append(allowed_functions_item)

        _value_type = d.pop("valueType", UNSET)
        value_type: FilterablePropertyTypeValueType | Unset
        if isinstance(_value_type, Unset):
            value_type = UNSET
        else:
            value_type = FilterablePropertyTypeValueType(_value_type)

        _supported_functions = d.pop("supportedFunctions", UNSET)
        supported_functions: list[FilterablePropertyTypeSupportedFunctionsItem] | Unset = UNSET
        if _supported_functions is not UNSET:
            supported_functions = []
            for supported_functions_item_data in _supported_functions:
                supported_functions_item = FilterablePropertyTypeSupportedFunctionsItem(supported_functions_item_data)

                supported_functions.append(supported_functions_item)

        filterable_property_type = cls(
            allowed_functions=allowed_functions,
            value_type=value_type,
            supported_functions=supported_functions,
        )

        filterable_property_type.additional_properties = d
        return filterable_property_type

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
