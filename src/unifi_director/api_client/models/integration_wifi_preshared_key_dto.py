from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wifi_network_reference import WifiNetworkReference


T = TypeVar("T", bound="IntegrationWifiPresharedKeyDto")


@_attrs_define
class IntegrationWifiPresharedKeyDto:
    """
    Attributes:
        network (WifiNetworkReference):
        passphrase (str):
    """

    network: WifiNetworkReference
    passphrase: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network.to_dict()

        passphrase = self.passphrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
                "passphrase": passphrase,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wifi_network_reference import WifiNetworkReference

        d = dict(src_dict)
        network = WifiNetworkReference.from_dict(d.pop("network"))

        passphrase = d.pop("passphrase")

        integration_wifi_preshared_key_dto = cls(
            network=network,
            passphrase=passphrase,
        )

        integration_wifi_preshared_key_dto.additional_properties = d
        return integration_wifi_preshared_key_dto

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
