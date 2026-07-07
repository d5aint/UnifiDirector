from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcasting_device_filter import BroadcastingDeviceFilter
    from ..models.integration_blackout_schedule_configuration import IntegrationBlackoutScheduleConfiguration
    from ..models.integration_wifi_basic_data_rate_configuration_dto import IntegrationWifiBasicDataRateConfigurationDto
    from ..models.integration_wifi_client_filtering_policy_dto import IntegrationWifiClientFilteringPolicyDto
    from ..models.mdns_filtering_configuration import MDNSFilteringConfiguration
    from ..models.multicast_filtering_policy import MulticastFilteringPolicy
    from ..models.user_or_derived_or_orchestrated_entity_metadata import UserOrDerivedOrOrchestratedEntityMetadata
    from ..models.wifi_network_reference import WifiNetworkReference
    from ..models.wifi_security_configuration_detail_object import WifiSecurityConfigurationDetailObject


T = TypeVar("T", bound="WifiBroadcastDetails")


@_attrs_define
class WifiBroadcastDetails:
    """
    Attributes:
        type_ (str):
        id (UUID):
        name (str):
        metadata (UserOrDerivedOrOrchestratedEntityMetadata):
        enabled (bool):
        security_configuration (WifiSecurityConfigurationDetailObject):
        multicast_to_unicast_conversion_enabled (bool):
        client_isolation_enabled (bool):
        hide_name (bool):
        uapsd_enabled (bool): Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled
        channel_2_g_locked_to_6 (bool): Locks 2.4GHz radio channel to 6 on all broadcasting devices
        dtim_period_2_g_locked_to_3 (bool): Locks DTIM period to 3 for 2.4GHz radio
        network (WifiNetworkReference | Unset):
        broadcasting_device_filter (BroadcastingDeviceFilter | Unset):
        mdns_proxy_configuration (MDNSFilteringConfiguration | Unset):
        multicast_filtering_policy (MulticastFilteringPolicy | Unset):
        basic_data_rate_kbps_by_frequency_g_hz (IntegrationWifiBasicDataRateConfigurationDto | Unset):
        client_filtering_policy (IntegrationWifiClientFilteringPolicyDto | Unset):
        blackout_schedule_configuration (IntegrationBlackoutScheduleConfiguration | Unset):
    """

    type_: str
    id: UUID
    name: str
    metadata: UserOrDerivedOrOrchestratedEntityMetadata
    enabled: bool
    security_configuration: WifiSecurityConfigurationDetailObject
    multicast_to_unicast_conversion_enabled: bool
    client_isolation_enabled: bool
    hide_name: bool
    uapsd_enabled: bool
    channel_2_g_locked_to_6: bool
    dtim_period_2_g_locked_to_3: bool
    network: WifiNetworkReference | Unset = UNSET
    broadcasting_device_filter: BroadcastingDeviceFilter | Unset = UNSET
    mdns_proxy_configuration: MDNSFilteringConfiguration | Unset = UNSET
    multicast_filtering_policy: MulticastFilteringPolicy | Unset = UNSET
    basic_data_rate_kbps_by_frequency_g_hz: IntegrationWifiBasicDataRateConfigurationDto | Unset = UNSET
    client_filtering_policy: IntegrationWifiClientFilteringPolicyDto | Unset = UNSET
    blackout_schedule_configuration: IntegrationBlackoutScheduleConfiguration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = str(self.id)

        name = self.name

        metadata = self.metadata.to_dict()

        enabled = self.enabled

        security_configuration = self.security_configuration.to_dict()

        multicast_to_unicast_conversion_enabled = self.multicast_to_unicast_conversion_enabled

        client_isolation_enabled = self.client_isolation_enabled

        hide_name = self.hide_name

        uapsd_enabled = self.uapsd_enabled

        channel_2_g_locked_to_6 = self.channel_2_g_locked_to_6

        dtim_period_2_g_locked_to_3 = self.dtim_period_2_g_locked_to_3

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        broadcasting_device_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.broadcasting_device_filter, Unset):
            broadcasting_device_filter = self.broadcasting_device_filter.to_dict()

        mdns_proxy_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mdns_proxy_configuration, Unset):
            mdns_proxy_configuration = self.mdns_proxy_configuration.to_dict()

        multicast_filtering_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.multicast_filtering_policy, Unset):
            multicast_filtering_policy = self.multicast_filtering_policy.to_dict()

        basic_data_rate_kbps_by_frequency_g_hz: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_data_rate_kbps_by_frequency_g_hz, Unset):
            basic_data_rate_kbps_by_frequency_g_hz = self.basic_data_rate_kbps_by_frequency_g_hz.to_dict()

        client_filtering_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_filtering_policy, Unset):
            client_filtering_policy = self.client_filtering_policy.to_dict()

        blackout_schedule_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blackout_schedule_configuration, Unset):
            blackout_schedule_configuration = self.blackout_schedule_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "metadata": metadata,
                "enabled": enabled,
                "securityConfiguration": security_configuration,
                "multicastToUnicastConversionEnabled": multicast_to_unicast_conversion_enabled,
                "clientIsolationEnabled": client_isolation_enabled,
                "hideName": hide_name,
                "uapsdEnabled": uapsd_enabled,
                "channel2gLockedTo6": channel_2_g_locked_to_6,
                "dtimPeriod2gLockedTo3": dtim_period_2_g_locked_to_3,
            }
        )
        if network is not UNSET:
            field_dict["network"] = network
        if broadcasting_device_filter is not UNSET:
            field_dict["broadcastingDeviceFilter"] = broadcasting_device_filter
        if mdns_proxy_configuration is not UNSET:
            field_dict["mdnsProxyConfiguration"] = mdns_proxy_configuration
        if multicast_filtering_policy is not UNSET:
            field_dict["multicastFilteringPolicy"] = multicast_filtering_policy
        if basic_data_rate_kbps_by_frequency_g_hz is not UNSET:
            field_dict["basicDataRateKbpsByFrequencyGHz"] = basic_data_rate_kbps_by_frequency_g_hz
        if client_filtering_policy is not UNSET:
            field_dict["clientFilteringPolicy"] = client_filtering_policy
        if blackout_schedule_configuration is not UNSET:
            field_dict["blackoutScheduleConfiguration"] = blackout_schedule_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcasting_device_filter import BroadcastingDeviceFilter
        from ..models.integration_blackout_schedule_configuration import IntegrationBlackoutScheduleConfiguration
        from ..models.integration_wifi_basic_data_rate_configuration_dto import (
            IntegrationWifiBasicDataRateConfigurationDto,
        )
        from ..models.integration_wifi_client_filtering_policy_dto import IntegrationWifiClientFilteringPolicyDto
        from ..models.mdns_filtering_configuration import MDNSFilteringConfiguration
        from ..models.multicast_filtering_policy import MulticastFilteringPolicy
        from ..models.user_or_derived_or_orchestrated_entity_metadata import UserOrDerivedOrOrchestratedEntityMetadata
        from ..models.wifi_network_reference import WifiNetworkReference
        from ..models.wifi_security_configuration_detail_object import WifiSecurityConfigurationDetailObject

        d = dict(src_dict)
        type_ = d.pop("type")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        metadata = UserOrDerivedOrOrchestratedEntityMetadata.from_dict(d.pop("metadata"))

        enabled = d.pop("enabled")

        security_configuration = WifiSecurityConfigurationDetailObject.from_dict(d.pop("securityConfiguration"))

        multicast_to_unicast_conversion_enabled = d.pop("multicastToUnicastConversionEnabled")

        client_isolation_enabled = d.pop("clientIsolationEnabled")

        hide_name = d.pop("hideName")

        uapsd_enabled = d.pop("uapsdEnabled")

        channel_2_g_locked_to_6 = d.pop("channel2gLockedTo6")

        dtim_period_2_g_locked_to_3 = d.pop("dtimPeriod2gLockedTo3")

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

        _mdns_proxy_configuration = d.pop("mdnsProxyConfiguration", UNSET)
        mdns_proxy_configuration: MDNSFilteringConfiguration | Unset
        if isinstance(_mdns_proxy_configuration, Unset):
            mdns_proxy_configuration = UNSET
        else:
            mdns_proxy_configuration = MDNSFilteringConfiguration.from_dict(_mdns_proxy_configuration)

        _multicast_filtering_policy = d.pop("multicastFilteringPolicy", UNSET)
        multicast_filtering_policy: MulticastFilteringPolicy | Unset
        if isinstance(_multicast_filtering_policy, Unset):
            multicast_filtering_policy = UNSET
        else:
            multicast_filtering_policy = MulticastFilteringPolicy.from_dict(_multicast_filtering_policy)

        _basic_data_rate_kbps_by_frequency_g_hz = d.pop("basicDataRateKbpsByFrequencyGHz", UNSET)
        basic_data_rate_kbps_by_frequency_g_hz: IntegrationWifiBasicDataRateConfigurationDto | Unset
        if isinstance(_basic_data_rate_kbps_by_frequency_g_hz, Unset):
            basic_data_rate_kbps_by_frequency_g_hz = UNSET
        else:
            basic_data_rate_kbps_by_frequency_g_hz = IntegrationWifiBasicDataRateConfigurationDto.from_dict(
                _basic_data_rate_kbps_by_frequency_g_hz
            )

        _client_filtering_policy = d.pop("clientFilteringPolicy", UNSET)
        client_filtering_policy: IntegrationWifiClientFilteringPolicyDto | Unset
        if isinstance(_client_filtering_policy, Unset):
            client_filtering_policy = UNSET
        else:
            client_filtering_policy = IntegrationWifiClientFilteringPolicyDto.from_dict(_client_filtering_policy)

        _blackout_schedule_configuration = d.pop("blackoutScheduleConfiguration", UNSET)
        blackout_schedule_configuration: IntegrationBlackoutScheduleConfiguration | Unset
        if isinstance(_blackout_schedule_configuration, Unset):
            blackout_schedule_configuration = UNSET
        else:
            blackout_schedule_configuration = IntegrationBlackoutScheduleConfiguration.from_dict(
                _blackout_schedule_configuration
            )

        wifi_broadcast_details = cls(
            type_=type_,
            id=id,
            name=name,
            metadata=metadata,
            enabled=enabled,
            security_configuration=security_configuration,
            multicast_to_unicast_conversion_enabled=multicast_to_unicast_conversion_enabled,
            client_isolation_enabled=client_isolation_enabled,
            hide_name=hide_name,
            uapsd_enabled=uapsd_enabled,
            channel_2_g_locked_to_6=channel_2_g_locked_to_6,
            dtim_period_2_g_locked_to_3=dtim_period_2_g_locked_to_3,
            network=network,
            broadcasting_device_filter=broadcasting_device_filter,
            mdns_proxy_configuration=mdns_proxy_configuration,
            multicast_filtering_policy=multicast_filtering_policy,
            basic_data_rate_kbps_by_frequency_g_hz=basic_data_rate_kbps_by_frequency_g_hz,
            client_filtering_policy=client_filtering_policy,
            blackout_schedule_configuration=blackout_schedule_configuration,
        )

        wifi_broadcast_details.additional_properties = d
        return wifi_broadcast_details

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
