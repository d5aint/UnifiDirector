from enum import Enum


class ACLRuleUpdateAction(str, Enum):
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"

    def __str__(self) -> str:
        return str(self.value)
