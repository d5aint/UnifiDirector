from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationWifiMulticastFilteringAllowPolicyDto")


@_attrs_define
class IntegrationWifiMulticastFilteringAllowPolicyDto:
    """
    Attributes:
        action (str):
        source_mac_address_filter (list[str]): List of multicast source MAC addresses allowed. Multicast traffic from
            gateways is always allowed.
    """

    action: str
    source_mac_address_filter: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        source_mac_address_filter = self.source_mac_address_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "sourceMacAddressFilter": source_mac_address_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        source_mac_address_filter = cast(list[str], d.pop("sourceMacAddressFilter"))

        integration_wifi_multicast_filtering_allow_policy_dto = cls(
            action=action,
            source_mac_address_filter=source_mac_address_filter,
        )

        integration_wifi_multicast_filtering_allow_policy_dto.additional_properties = d
        return integration_wifi_multicast_filtering_allow_policy_dto

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
