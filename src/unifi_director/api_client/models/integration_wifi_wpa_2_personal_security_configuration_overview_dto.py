from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wifi_network_reference import WifiNetworkReference


T = TypeVar("T", bound="IntegrationWifiWpa2PersonalSecurityConfigurationOverviewDto")


@_attrs_define
class IntegrationWifiWpa2PersonalSecurityConfigurationOverviewDto:
    """
    Attributes:
        type_ (str):
        preshared_key_network_ids (list[WifiNetworkReference] | Unset):
    """

    type_: str
    preshared_key_network_ids: list[WifiNetworkReference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        preshared_key_network_ids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.preshared_key_network_ids, Unset):
            preshared_key_network_ids = []
            for preshared_key_network_ids_item_data in self.preshared_key_network_ids:
                preshared_key_network_ids_item = preshared_key_network_ids_item_data.to_dict()
                preshared_key_network_ids.append(preshared_key_network_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if preshared_key_network_ids is not UNSET:
            field_dict["presharedKeyNetworkIds"] = preshared_key_network_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wifi_network_reference import WifiNetworkReference

        d = dict(src_dict)
        type_ = d.pop("type")

        _preshared_key_network_ids = d.pop("presharedKeyNetworkIds", UNSET)
        preshared_key_network_ids: list[WifiNetworkReference] | Unset = UNSET
        if _preshared_key_network_ids is not UNSET:
            preshared_key_network_ids = []
            for preshared_key_network_ids_item_data in _preshared_key_network_ids:
                preshared_key_network_ids_item = WifiNetworkReference.from_dict(preshared_key_network_ids_item_data)

                preshared_key_network_ids.append(preshared_key_network_ids_item)

        integration_wifi_wpa_2_personal_security_configuration_overview_dto = cls(
            type_=type_,
            preshared_key_network_ids=preshared_key_network_ids,
        )

        integration_wifi_wpa_2_personal_security_configuration_overview_dto.additional_properties = d
        return integration_wifi_wpa_2_personal_security_configuration_overview_dto

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
