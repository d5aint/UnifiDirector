from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_expression import FilterExpression
    from ..models.filterable_entity import FilterableEntity


T = TypeVar("T", bound="NotFilterExpression")


@_attrs_define
class NotFilterExpression:
    """
    Attributes:
        entity (FilterableEntity | Unset):
        expression (FilterExpression | Unset):
    """

    entity: FilterableEntity | Unset = UNSET
    expression: FilterExpression | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        expression: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expression, Unset):
            expression = self.expression.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity is not UNSET:
            field_dict["entity"] = entity
        if expression is not UNSET:
            field_dict["expression"] = expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_expression import FilterExpression
        from ..models.filterable_entity import FilterableEntity

        d = dict(src_dict)
        _entity = d.pop("entity", UNSET)
        entity: FilterableEntity | Unset
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = FilterableEntity.from_dict(_entity)

        _expression = d.pop("expression", UNSET)
        expression: FilterExpression | Unset
        if isinstance(_expression, Unset):
            expression = UNSET
        else:
            expression = FilterExpression.from_dict(_expression)

        not_filter_expression = cls(
            entity=entity,
            expression=expression,
        )

        not_filter_expression.additional_properties = d
        return not_filter_expression

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
