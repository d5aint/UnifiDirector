from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.property_filter_expression_function import PropertyFilterExpressionFunction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filterable_entity import FilterableEntity
    from ..models.filterable_property import FilterableProperty


T = TypeVar("T", bound="PropertyFilterExpression")


@_attrs_define
class PropertyFilterExpression:
    """
    Attributes:
        entity (FilterableEntity | Unset):
        property_ (FilterableProperty | Unset):
        function (PropertyFilterExpressionFunction | Unset):
        arguments (list[Any] | Unset):
    """

    entity: FilterableEntity | Unset = UNSET
    property_: FilterableProperty | Unset = UNSET
    function: PropertyFilterExpressionFunction | Unset = UNSET
    arguments: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        property_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.to_dict()

        function: str | Unset = UNSET
        if not isinstance(self.function, Unset):
            function = self.function.value

        arguments: list[Any] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity is not UNSET:
            field_dict["entity"] = entity
        if property_ is not UNSET:
            field_dict["property"] = property_
        if function is not UNSET:
            field_dict["function"] = function
        if arguments is not UNSET:
            field_dict["arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filterable_entity import FilterableEntity
        from ..models.filterable_property import FilterableProperty

        d = dict(src_dict)
        _entity = d.pop("entity", UNSET)
        entity: FilterableEntity | Unset
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = FilterableEntity.from_dict(_entity)

        _property_ = d.pop("property", UNSET)
        property_: FilterableProperty | Unset
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = FilterableProperty.from_dict(_property_)

        _function = d.pop("function", UNSET)
        function: PropertyFilterExpressionFunction | Unset
        if isinstance(_function, Unset):
            function = UNSET
        else:
            function = PropertyFilterExpressionFunction(_function)

        arguments = cast(list[Any], d.pop("arguments", UNSET))

        property_filter_expression = cls(
            entity=entity,
            property_=property_,
            function=function,
            arguments=arguments,
        )

        property_filter_expression.additional_properties = d
        return property_filter_expression

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
