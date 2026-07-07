from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.integration_ipv_6_address_suffix_range_selector_dto import (
        IntegrationIpv6AddressSuffixRangeSelectorDto,
    )


T = TypeVar("T", bound="DHCPConfigurationForIPv6Network")


@_attrs_define
class DHCPConfigurationForIPv6Network:
    """
    Attributes:
        ip_address_suffix_range (IntegrationIpv6AddressSuffixRangeSelectorDto):
        lease_time_seconds (int): The lease time in seconds for IP addresses in this range.
    """

    ip_address_suffix_range: IntegrationIpv6AddressSuffixRangeSelectorDto
    lease_time_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_address_suffix_range = self.ip_address_suffix_range.to_dict()

        lease_time_seconds = self.lease_time_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipAddressSuffixRange": ip_address_suffix_range,
                "leaseTimeSeconds": lease_time_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_ipv_6_address_suffix_range_selector_dto import (
            IntegrationIpv6AddressSuffixRangeSelectorDto,
        )

        d = dict(src_dict)
        ip_address_suffix_range = IntegrationIpv6AddressSuffixRangeSelectorDto.from_dict(d.pop("ipAddressSuffixRange"))

        lease_time_seconds = d.pop("leaseTimeSeconds")

        dhcp_configuration_for_i_pv_6_network = cls(
            ip_address_suffix_range=ip_address_suffix_range,
            lease_time_seconds=lease_time_seconds,
        )

        dhcp_configuration_for_i_pv_6_network.additional_properties = d
        return dhcp_configuration_for_i_pv_6_network

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
