from enum import Enum


class CreateOrUpdateFirewallPolicyIpsecFilter(str, Enum):
    MATCH_ENCRYPTED = "MATCH_ENCRYPTED"
    MATCH_NOT_ENCRYPTED = "MATCH_NOT_ENCRYPTED"

    def __str__(self) -> str:
        return str(self.value)
