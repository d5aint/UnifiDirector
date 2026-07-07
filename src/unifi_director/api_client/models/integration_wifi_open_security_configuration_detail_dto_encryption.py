from enum import Enum


class IntegrationWifiOpenSecurityConfigurationDetailDtoEncryption(str, Enum):
    ENHANCED_OPEN = "ENHANCED_OPEN"
    ENHANCED_OPEN_WITH_TRANSITION = "ENHANCED_OPEN_WITH_TRANSITION"

    def __str__(self) -> str:
        return str(self.value)
