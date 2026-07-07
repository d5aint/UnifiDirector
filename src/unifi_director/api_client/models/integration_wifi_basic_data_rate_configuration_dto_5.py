from enum import Enum


class IntegrationWifiBasicDataRateConfigurationDto5(str, Enum):
    VALUE_0 = "6000"
    VALUE_1 = "9000"
    VALUE_2 = "12000"
    VALUE_3 = "24000"

    def __str__(self) -> str:
        return str(self.value)
