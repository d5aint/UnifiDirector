from enum import Enum


class FilterablePropertyTypeValueType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DECIMAL = "DECIMAL"
    INTEGER = "INTEGER"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"
    UUID = "UUID"

    def __str__(self) -> str:
        return str(self.value)
