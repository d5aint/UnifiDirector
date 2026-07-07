from enum import Enum


class IntegrationIpAclRuleCreateUpdateDtoProtocolFilterItem(str, Enum):
    TCP = "TCP"
    UDP = "UDP"

    def __str__(self) -> str:
        return str(self.value)
