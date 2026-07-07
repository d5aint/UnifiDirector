from enum import Enum


class NetworkReferenceResourceResourceType(str, Enum):
    CLIENT = "CLIENT"
    DEVICE = "DEVICE"
    NAT_RULE = "NAT_RULE"
    NEXT_AI = "NEXT_AI"
    OSPF_ROUTE = "OSPF_ROUTE"
    SD_WAN = "SD_WAN"
    STATIC_ROUTE = "STATIC_ROUTE"
    WIFI = "WIFI"

    def __str__(self) -> str:
        return str(self.value)
