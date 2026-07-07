from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compound_filter_expression_operator import CompoundFilterExpressionOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_expression import FilterExpression
    from ..models.filterable_entity import FilterableEntity


T = TypeVar("T", bound="CompoundFilterExpression")


@_attrs_define
class CompoundFilterExpression:
    """
    Attributes:
        entity (FilterableEntity | Unset):
        operator (CompoundFilterExpressionOperator | Unset):
        expressions (list[FilterExpression] | Unset):
    """

    entity: FilterableEntity | Unset = UNSET
    operator: CompoundFilterExpressionOperator | Unset = UNSET
    expressions: list[FilterExpression] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        expressions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expressions, Unset):
            expressions = []
            for expressions_item_data in self.expressions:
                expressions_item = expressions_item_data.to_dict()
                expressions.append(expressions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity is not UNSET:
            field_dict["entity"] = entity
        if operator is not UNSET:
            field_dict["operator"] = operator
        if expressions is not UNSET:
            field_dict["expressions"] = expressions

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

        _operator = d.pop("operator", UNSET)
        operator: CompoundFilterExpressionOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = CompoundFilterExpressionOperator(_operator)

        _expressions = d.pop("expressions", UNSET)
        expressions: list[FilterExpression] | Unset = UNSET
        if _expressions is not UNSET:
            expressions = []
            for expressions_item_data in _expressions:
                expressions_item = FilterExpression.from_dict(expressions_item_data)

                expressions.append(expressions_item)

        compound_filter_expression = cls(
            entity=entity,
            operator=operator,
            expressions=expressions,
        )

        compound_filter_expression.additional_properties = d
        return compound_filter_expression

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
