from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_wifi_client_filtering_policy_dto_action import IntegrationWifiClientFilteringPolicyDtoAction

T = TypeVar("T", bound="IntegrationWifiClientFilteringPolicyDto")


@_attrs_define
class IntegrationWifiClientFilteringPolicyDto:
    """
    Attributes:
        action (IntegrationWifiClientFilteringPolicyDtoAction):
        mac_address_filter (list[str]):
    """

    action: IntegrationWifiClientFilteringPolicyDtoAction
    mac_address_filter: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        mac_address_filter = self.mac_address_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "macAddressFilter": mac_address_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = IntegrationWifiClientFilteringPolicyDtoAction(d.pop("action"))

        mac_address_filter = cast(list[str], d.pop("macAddressFilter"))

        integration_wifi_client_filtering_policy_dto = cls(
            action=action,
            mac_address_filter=mac_address_filter,
        )

        integration_wifi_client_filtering_policy_dto.additional_properties = d
        return integration_wifi_client_filtering_policy_dto

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
