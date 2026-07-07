from enum import Enum


class NATOutboundAutoConfigurationIpAddressSelectionMode(str, Enum):
    ALL = "ALL"
    MAIN = "MAIN"

    def __str__(self) -> str:
        return str(self.value)
