from enum import Enum


class FilterablePropertyTypeSupportedFunctionsItem(str, Enum):
    CONTAINS = "CONTAINS"
    CONTAINS_ALL = "CONTAINS_ALL"
    CONTAINS_ANY = "CONTAINS_ANY"
    CONTAINS_EXACTLY = "CONTAINS_EXACTLY"
    EQ = "EQ"
    GE = "GE"
    GT = "GT"
    IN = "IN"
    IS_EMPTY = "IS_EMPTY"
    IS_NOT_NULL = "IS_NOT_NULL"
    IS_NULL = "IS_NULL"
    LE = "LE"
    LIKE = "LIKE"
    LT = "LT"
    NE = "NE"
    NOT_IN = "NOT_IN"

    def __str__(self) -> str:
        return str(self.value)
