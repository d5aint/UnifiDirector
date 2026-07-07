from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcasting_device_filter import BroadcastingDeviceFilter
    from ..models.user_or_derived_or_orchestrated_entity_metadata import UserOrDerivedOrOrchestratedEntityMetadata
    from ..models.wifi_network_reference import WifiNetworkReference
    from ..models.wifi_security_configuration_overview import WifiSecurityConfigurationOverview


T = TypeVar("T", bound="WifiBroadcastOverview")


@_attrs_define
class WifiBroadcastOverview:
    """
    Attributes:
        type_ (str):
        id (UUID):
        name (str):
        enabled (bool):
        metadata (UserOrDerivedOrOrchestratedEntityMetadata):
        security_configuration (WifiSecurityConfigurationOverview):
        network (WifiNetworkReference | Unset):
        broadcasting_device_filter (BroadcastingDeviceFilter | Unset):
    """

    type_: str
    id: UUID
    name: str
    enabled: bool
    metadata: UserOrDerivedOrOrchestratedEntityMetadata
    security_configuration: WifiSecurityConfigurationOverview
    network: WifiNetworkReference | Unset = UNSET
    broadcasting_device_filter: BroadcastingDeviceFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = str(self.id)

        name = self.name

        enabled = self.enabled

        metadata = self.metadata.to_dict()

        security_configuration = self.security_configuration.to_dict()

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        broadcasting_device_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.broadcasting_device_filter, Unset):
            broadcasting_device_filter = self.broadcasting_device_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "enabled": enabled,
                "metadata": metadata,
                "securityConfiguration": security_configuration,
            }
        )
        if network is not UNSET:
            field_dict["network"] = network
        if broadcasting_device_filter is not UNSET:
            field_dict["broadcastingDeviceFilter"] = broadcasting_device_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcasting_device_filter import BroadcastingDeviceFilter
        from ..models.user_or_derived_or_orchestrated_entity_metadata import UserOrDerivedOrOrchestratedEntityMetadata
        from ..models.wifi_network_reference import WifiNetworkReference
        from ..models.wifi_security_configuration_overview import WifiSecurityConfigurationOverview

        d = dict(src_dict)
        type_ = d.pop("type")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        enabled = d.pop("enabled")

        metadata = UserOrDerivedOrOrchestratedEntityMetadata.from_dict(d.pop("metadata"))

        security_configuration = WifiSecurityConfigurationOverview.from_dict(d.pop("securityConfiguration"))

        _network = d.pop("network", UNSET)
        network: WifiNetworkReference | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = WifiNetworkReference.from_dict(_network)

        _broadcasting_device_filter = d.pop("broadcastingDeviceFilter", UNSET)
        broadcasting_device_filter: BroadcastingDeviceFilter | Unset
        if isinstance(_broadcasting_device_filter, Unset):
            broadcasting_device_filter = UNSET
        else:
            broadcasting_device_filter = BroadcastingDeviceFilter.from_dict(_broadcasting_device_filter)

        wifi_broadcast_overview = cls(
            type_=type_,
            id=id,
            name=name,
            enabled=enabled,
            metadata=metadata,
            security_configuration=security_configuration,
            network=network,
            broadcasting_device_filter=broadcasting_device_filter,
        )

        wifi_broadcast_overview.additional_properties = d
        return wifi_broadcast_overview

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
