from enum import Enum


class IntegrationMcLagPeerDtoRole(str, Enum):
    BOTTOM = "BOTTOM"
    TOP = "TOP"

    def __str__(self) -> str:
        return str(self.value)
