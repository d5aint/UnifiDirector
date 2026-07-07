from enum import Enum


class IntegrationWifiHotspotConfigurationOverviewDtoType(str, Enum):
    CAPTIVE_PORTAL = "CAPTIVE_PORTAL"
    PASSPOINT = "PASSPOINT"

    def __str__(self) -> str:
        return str(self.value)
