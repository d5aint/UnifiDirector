from enum import Enum


class IntegrationWifiWpa2Wpa3PersonalSecurityConfigurationDetailDtoPmfMode(str, Enum):
    OPTIONAL = "OPTIONAL"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
