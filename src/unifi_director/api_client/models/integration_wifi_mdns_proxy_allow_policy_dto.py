from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcasting_device_filter import BroadcastingDeviceFilter
    from ..models.mdns_service import MDNSService


T = TypeVar("T", bound="IntegrationWifiMdnsProxyAllowPolicyDto")


@_attrs_define
class IntegrationWifiMdnsProxyAllowPolicyDto:
    """
    Attributes:
        action (str):
        device_filter (BroadcastingDeviceFilter | Unset):
        service_filter (list[MDNSService] | Unset):
        bridging_network_ids (list[UUID] | Unset):
    """

    action: str
    device_filter: BroadcastingDeviceFilter | Unset = UNSET
    service_filter: list[MDNSService] | Unset = UNSET
    bridging_network_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        device_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_filter, Unset):
            device_filter = self.device_filter.to_dict()

        service_filter: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_filter, Unset):
            service_filter = []
            for service_filter_item_data in self.service_filter:
                service_filter_item = service_filter_item_data.to_dict()
                service_filter.append(service_filter_item)

        bridging_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.bridging_network_ids, Unset):
            bridging_network_ids = []
            for bridging_network_ids_item_data in self.bridging_network_ids:
                bridging_network_ids_item = str(bridging_network_ids_item_data)
                bridging_network_ids.append(bridging_network_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if device_filter is not UNSET:
            field_dict["deviceFilter"] = device_filter
        if service_filter is not UNSET:
            field_dict["serviceFilter"] = service_filter
        if bridging_network_ids is not UNSET:
            field_dict["bridgingNetworkIds"] = bridging_network_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcasting_device_filter import BroadcastingDeviceFilter
        from ..models.mdns_service import MDNSService

        d = dict(src_dict)
        action = d.pop("action")

        _device_filter = d.pop("deviceFilter", UNSET)
        device_filter: BroadcastingDeviceFilter | Unset
        if isinstance(_device_filter, Unset):
            device_filter = UNSET
        else:
            device_filter = BroadcastingDeviceFilter.from_dict(_device_filter)

        _service_filter = d.pop("serviceFilter", UNSET)
        service_filter: list[MDNSService] | Unset = UNSET
        if _service_filter is not UNSET:
            service_filter = []
            for service_filter_item_data in _service_filter:
                service_filter_item = MDNSService.from_dict(service_filter_item_data)

                service_filter.append(service_filter_item)

        _bridging_network_ids = d.pop("bridgingNetworkIds", UNSET)
        bridging_network_ids: list[UUID] | Unset = UNSET
        if _bridging_network_ids is not UNSET:
            bridging_network_ids = []
            for bridging_network_ids_item_data in _bridging_network_ids:
                bridging_network_ids_item = UUID(bridging_network_ids_item_data)

                bridging_network_ids.append(bridging_network_ids_item)

        integration_wifi_mdns_proxy_allow_policy_dto = cls(
            action=action,
            device_filter=device_filter,
            service_filter=service_filter,
            bridging_network_ids=bridging_network_ids,
        )

        integration_wifi_mdns_proxy_allow_policy_dto.additional_properties = d
        return integration_wifi_mdns_proxy_allow_policy_dto

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
