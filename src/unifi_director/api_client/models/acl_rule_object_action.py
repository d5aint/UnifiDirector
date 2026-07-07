from enum import Enum


class ACLRuleObjectAction(str, Enum):
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"

    def __str__(self) -> str:
        return str(self.value)
