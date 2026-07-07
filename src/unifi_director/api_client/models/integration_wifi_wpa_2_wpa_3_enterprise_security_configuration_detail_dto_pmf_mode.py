from enum import Enum


class IntegrationWifiWpa2Wpa3EnterpriseSecurityConfigurationDetailDtoPmfMode(str, Enum):
    OPTIONAL = "OPTIONAL"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
