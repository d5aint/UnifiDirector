from enum import Enum


class IntegrationWifiDerivedNasIdDtoSource(str, Enum):
    BSSID = "BSSID"
    DEVICE_MAC_ADDRESS = "DEVICE_MAC_ADDRESS"
    DEVICE_NAME = "DEVICE_NAME"
    SITE_NAME = "SITE_NAME"

    def __str__(self) -> str:
        return str(self.value)
