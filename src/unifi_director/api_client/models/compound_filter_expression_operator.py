from enum import Enum


class CompoundFilterExpressionOperator(str, Enum):
    AND = "AND"
    NOT = "NOT"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
