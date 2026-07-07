from enum import Enum


class IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDtoSecurityMode(str, Enum):
    DEFAULT = "DEFAULT"
    HIGH_SECURITY_192_BIT = "HIGH_SECURITY_192_BIT"

    def __str__(self) -> str:
        return str(self.value)
