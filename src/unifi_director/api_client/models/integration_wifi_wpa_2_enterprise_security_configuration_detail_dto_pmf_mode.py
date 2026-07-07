from enum import Enum


class IntegrationWifiWpa2EnterpriseSecurityConfigurationDetailDtoPmfMode(str, Enum):
    OPTIONAL = "OPTIONAL"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
