from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mdns_proxy_policy import MDNSProxyPolicy


T = TypeVar("T", bound="IntegrationWifiMdnsProxyCustomConfigurationDto")


@_attrs_define
class IntegrationWifiMdnsProxyCustomConfigurationDto:
    """
    Attributes:
        mode (str):
        policies (list[MDNSProxyPolicy]):
    """

    mode: str
    policies: list[MDNSProxyPolicy]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        policies = []
        for policies_item_data in self.policies:
            policies_item = policies_item_data.to_dict()
            policies.append(policies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "policies": policies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mdns_proxy_policy import MDNSProxyPolicy

        d = dict(src_dict)
        mode = d.pop("mode")

        policies = []
        _policies = d.pop("policies")
        for policies_item_data in _policies:
            policies_item = MDNSProxyPolicy.from_dict(policies_item_data)

            policies.append(policies_item)

        integration_wifi_mdns_proxy_custom_configuration_dto = cls(
            mode=mode,
            policies=policies,
        )

        integration_wifi_mdns_proxy_custom_configuration_dto.additional_properties = d
        return integration_wifi_mdns_proxy_custom_configuration_dto

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
