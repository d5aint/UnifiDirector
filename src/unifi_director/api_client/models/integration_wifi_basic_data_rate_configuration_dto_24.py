from enum import Enum


class IntegrationWifiBasicDataRateConfigurationDto24(str, Enum):
    VALUE_0 = "1000"
    VALUE_1 = "2000"
    VALUE_2 = "5500"
    VALUE_3 = "6000"
    VALUE_4 = "9000"
    VALUE_5 = "11000"
    VALUE_6 = "12000"
    VALUE_7 = "24000"

    def __str__(self) -> str:
        return str(self.value)
