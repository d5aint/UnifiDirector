from enum import Enum


class FirewallPolicyConnectionStateFilterItem(str, Enum):
    ESTABLISHED = "ESTABLISHED"
    INVALID = "INVALID"
    NEW = "NEW"
    RELATED = "RELATED"

    def __str__(self) -> str:
        return str(self.value)
