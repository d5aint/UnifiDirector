from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_standard_wifi_broadcast_create_update_dto_broadcasting_frequencies_g_hz_item import (
    IntegrationStandardWifiBroadcastCreateUpdateDtoBroadcastingFrequenciesGHzItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcasting_device_filter import BroadcastingDeviceFilter
    from ..models.dns_assistance_configuration import DNSAssistanceConfiguration
    from ..models.integration_blackout_schedule_configuration import IntegrationBlackoutScheduleConfiguration
    from ..models.integration_wifi_basic_data_rate_configuration_dto import IntegrationWifiBasicDataRateConfigurationDto
    from ..models.integration_wifi_client_filtering_policy_dto import IntegrationWifiClientFilteringPolicyDto
    from ..models.integration_wifi_dtim_period_configuration_dto import IntegrationWifiDtimPeriodConfigurationDto
    from ..models.integration_wifi_handoff_suggestions_configuration_dto import (
        IntegrationWifiHandoffSuggestionsConfigurationDto,
    )
    from ..models.mdns_filtering_configuration import MDNSFilteringConfiguration
    from ..models.multicast_filtering_policy import MulticastFilteringPolicy
    from ..models.wifi_hotspot_configuration import WifiHotspotConfiguration
    from ..models.wifi_network_reference import WifiNetworkReference
    from ..models.wifi_security_configuration_detail_object import WifiSecurityConfigurationDetailObject


T = TypeVar("T", bound="IntegrationStandardWifiBroadcastCreateUpdateDto")


@_attrs_define
class IntegrationStandardWifiBroadcastCreateUpdateDto:
    """
    Attributes:
        type_ (str):
        name (str):
        enabled (bool):
        security_configuration (WifiSecurityConfigurationDetailObject):
        multicast_to_unicast_conversion_enabled (bool):
        client_isolation_enabled (bool):
        hide_name (bool):
        uapsd_enabled (bool): Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled
        channel_2_g_locked_to_6 (bool): Locks 2.4GHz radio channel to 6 on all broadcasting devices Default: False.
        dtim_period_2_g_locked_to_3 (bool): Locks DTIM period to 3 for 2.4GHz radio Default: False.
        broadcasting_frequencies_g_hz
            (list[IntegrationStandardWifiBroadcastCreateUpdateDtoBroadcastingFrequenciesGHzItem]):  Example: [2.4, 5].
        arp_proxy_enabled (bool):
        bss_transition_enabled (bool):
        advertise_device_name (bool): Indicates whether the device name is advertised in beacon frames.
        network (WifiNetworkReference | Unset):
        broadcasting_device_filter (BroadcastingDeviceFilter | Unset):
        mdns_proxy_configuration (MDNSFilteringConfiguration | Unset):
        multicast_filtering_policy (MulticastFilteringPolicy | Unset):
        basic_data_rate_kbps_by_frequency_g_hz (IntegrationWifiBasicDataRateConfigurationDto | Unset):
        client_filtering_policy (IntegrationWifiClientFilteringPolicyDto | Unset):
        blackout_schedule_configuration (IntegrationBlackoutScheduleConfiguration | Unset):
        hotspot_configuration (WifiHotspotConfiguration | Unset):
        mlo_enabled (bool | Unset):
        band_steering_enabled (bool | Unset):
        dtim_period_by_frequency_g_hz_override (IntegrationWifiDtimPeriodConfigurationDto | Unset):
        dns_assistance_configuration (DNSAssistanceConfiguration | Unset):
        handoff_suggestions_configuration (IntegrationWifiHandoffSuggestionsConfigurationDto | Unset):
    """

    type_: str
    name: str
    enabled: bool
    security_configuration: WifiSecurityConfigurationDetailObject
    multicast_to_unicast_conversion_enabled: bool
    client_isolation_enabled: bool
    hide_name: bool
    uapsd_enabled: bool
    broadcasting_frequencies_g_hz: list[IntegrationStandardWifiBroadcastCreateUpdateDtoBroadcastingFrequenciesGHzItem]
    arp_proxy_enabled: bool
    bss_transition_enabled: bool
    advertise_device_name: bool
    channel_2_g_locked_to_6: bool = False
    dtim_period_2_g_locked_to_3: bool = False
    network: WifiNetworkReference | Unset = UNSET
    broadcasting_device_filter: BroadcastingDeviceFilter | Unset = UNSET
    mdns_proxy_configuration: MDNSFilteringConfiguration | Unset = UNSET
    multicast_filtering_policy: MulticastFilteringPolicy | Unset = UNSET
    basic_data_rate_kbps_by_frequency_g_hz: IntegrationWifiBasicDataRateConfigurationDto | Unset = UNSET
    client_filtering_policy: IntegrationWifiClientFilteringPolicyDto | Unset = UNSET
    blackout_schedule_configuration: IntegrationBlackoutScheduleConfiguration | Unset = UNSET
    hotspot_configuration: WifiHotspotConfiguration | Unset = UNSET
    mlo_enabled: bool | Unset = UNSET
    band_steering_enabled: bool | Unset = UNSET
    dtim_period_by_frequency_g_hz_override: IntegrationWifiDtimPeriodConfigurationDto | Unset = UNSET
    dns_assistance_configuration: DNSAssistanceConfiguration | Unset = UNSET
    handoff_suggestions_configuration: IntegrationWifiHandoffSuggestionsConfigurationDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        enabled = self.enabled

        security_configuration = self.security_configuration.to_dict()

        multicast_to_unicast_conversion_enabled = self.multicast_to_unicast_conversion_enabled

        client_isolation_enabled = self.client_isolation_enabled

        hide_name = self.hide_name

        uapsd_enabled = self.uapsd_enabled

        channel_2_g_locked_to_6 = self.channel_2_g_locked_to_6

        dtim_period_2_g_locked_to_3 = self.dtim_period_2_g_locked_to_3

        broadcasting_frequencies_g_hz = []
        for broadcasting_frequencies_g_hz_item_data in self.broadcasting_frequencies_g_hz:
            broadcasting_frequencies_g_hz_item = broadcasting_frequencies_g_hz_item_data.value
            broadcasting_frequencies_g_hz.append(broadcasting_frequencies_g_hz_item)

        arp_proxy_enabled = self.arp_proxy_enabled

        bss_transition_enabled = self.bss_transition_enabled

        advertise_device_name = self.advertise_device_name

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

        hotspot_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hotspot_configuration, Unset):
            hotspot_configuration = self.hotspot_configuration.to_dict()

        mlo_enabled = self.mlo_enabled

        band_steering_enabled = self.band_steering_enabled

        dtim_period_by_frequency_g_hz_override: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dtim_period_by_frequency_g_hz_override, Unset):
            dtim_period_by_frequency_g_hz_override = self.dtim_period_by_frequency_g_hz_override.to_dict()

        dns_assistance_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns_assistance_configuration, Unset):
            dns_assistance_configuration = self.dns_assistance_configuration.to_dict()

        handoff_suggestions_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.handoff_suggestions_configuration, Unset):
            handoff_suggestions_configuration = self.handoff_suggestions_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "enabled": enabled,
                "securityConfiguration": security_configuration,
                "multicastToUnicastConversionEnabled": multicast_to_unicast_conversion_enabled,
                "clientIsolationEnabled": client_isolation_enabled,
                "hideName": hide_name,
                "uapsdEnabled": uapsd_enabled,
                "channel2gLockedTo6": channel_2_g_locked_to_6,
                "dtimPeriod2gLockedTo3": dtim_period_2_g_locked_to_3,
                "broadcastingFrequenciesGHz": broadcasting_frequencies_g_hz,
                "arpProxyEnabled": arp_proxy_enabled,
                "bssTransitionEnabled": bss_transition_enabled,
                "advertiseDeviceName": advertise_device_name,
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
        if hotspot_configuration is not UNSET:
            field_dict["hotspotConfiguration"] = hotspot_configuration
        if mlo_enabled is not UNSET:
            field_dict["mloEnabled"] = mlo_enabled
        if band_steering_enabled is not UNSET:
            field_dict["bandSteeringEnabled"] = band_steering_enabled
        if dtim_period_by_frequency_g_hz_override is not UNSET:
            field_dict["dtimPeriodByFrequencyGHzOverride"] = dtim_period_by_frequency_g_hz_override
        if dns_assistance_configuration is not UNSET:
            field_dict["dnsAssistanceConfiguration"] = dns_assistance_configuration
        if handoff_suggestions_configuration is not UNSET:
            field_dict["handoffSuggestionsConfiguration"] = handoff_suggestions_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcasting_device_filter import BroadcastingDeviceFilter
        from ..models.dns_assistance_configuration import DNSAssistanceConfiguration
        from ..models.integration_blackout_schedule_configuration import IntegrationBlackoutScheduleConfiguration
        from ..models.integration_wifi_basic_data_rate_configuration_dto import (
            IntegrationWifiBasicDataRateConfigurationDto,
        )
        from ..models.integration_wifi_client_filtering_policy_dto import IntegrationWifiClientFilteringPolicyDto
        from ..models.integration_wifi_dtim_period_configuration_dto import IntegrationWifiDtimPeriodConfigurationDto
        from ..models.integration_wifi_handoff_suggestions_configuration_dto import (
            IntegrationWifiHandoffSuggestionsConfigurationDto,
        )
        from ..models.mdns_filtering_configuration import MDNSFilteringConfiguration
        from ..models.multicast_filtering_policy import MulticastFilteringPolicy
        from ..models.wifi_hotspot_configuration import WifiHotspotConfiguration
        from ..models.wifi_network_reference import WifiNetworkReference
        from ..models.wifi_security_configuration_detail_object import WifiSecurityConfigurationDetailObject

        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        enabled = d.pop("enabled")

        security_configuration = WifiSecurityConfigurationDetailObject.from_dict(d.pop("securityConfiguration"))

        multicast_to_unicast_conversion_enabled = d.pop("multicastToUnicastConversionEnabled")

        client_isolation_enabled = d.pop("clientIsolationEnabled")

        hide_name = d.pop("hideName")

        uapsd_enabled = d.pop("uapsdEnabled")

        channel_2_g_locked_to_6 = d.pop("channel2gLockedTo6")

        dtim_period_2_g_locked_to_3 = d.pop("dtimPeriod2gLockedTo3")

        broadcasting_frequencies_g_hz = []
        _broadcasting_frequencies_g_hz = d.pop("broadcastingFrequenciesGHz")
        for broadcasting_frequencies_g_hz_item_data in _broadcasting_frequencies_g_hz:
            broadcasting_frequencies_g_hz_item = (
                IntegrationStandardWifiBroadcastCreateUpdateDtoBroadcastingFrequenciesGHzItem(
                    broadcasting_frequencies_g_hz_item_data
                )
            )

            broadcasting_frequencies_g_hz.append(broadcasting_frequencies_g_hz_item)

        arp_proxy_enabled = d.pop("arpProxyEnabled")

        bss_transition_enabled = d.pop("bssTransitionEnabled")

        advertise_device_name = d.pop("advertiseDeviceName")

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

        _hotspot_configuration = d.pop("hotspotConfiguration", UNSET)
        hotspot_configuration: WifiHotspotConfiguration | Unset
        if isinstance(_hotspot_configuration, Unset):
            hotspot_configuration = UNSET
        else:
            hotspot_configuration = WifiHotspotConfiguration.from_dict(_hotspot_configuration)

        mlo_enabled = d.pop("mloEnabled", UNSET)

        band_steering_enabled = d.pop("bandSteeringEnabled", UNSET)

        _dtim_period_by_frequency_g_hz_override = d.pop("dtimPeriodByFrequencyGHzOverride", UNSET)
        dtim_period_by_frequency_g_hz_override: IntegrationWifiDtimPeriodConfigurationDto | Unset
        if isinstance(_dtim_period_by_frequency_g_hz_override, Unset):
            dtim_period_by_frequency_g_hz_override = UNSET
        else:
            dtim_period_by_frequency_g_hz_override = IntegrationWifiDtimPeriodConfigurationDto.from_dict(
                _dtim_period_by_frequency_g_hz_override
            )

        _dns_assistance_configuration = d.pop("dnsAssistanceConfiguration", UNSET)
        dns_assistance_configuration: DNSAssistanceConfiguration | Unset
        if isinstance(_dns_assistance_configuration, Unset):
            dns_assistance_configuration = UNSET
        else:
            dns_assistance_configuration = DNSAssistanceConfiguration.from_dict(_dns_assistance_configuration)

        _handoff_suggestions_configuration = d.pop("handoffSuggestionsConfiguration", UNSET)
        handoff_suggestions_configuration: IntegrationWifiHandoffSuggestionsConfigurationDto | Unset
        if isinstance(_handoff_suggestions_configuration, Unset):
            handoff_suggestions_configuration = UNSET
        else:
            handoff_suggestions_configuration = IntegrationWifiHandoffSuggestionsConfigurationDto.from_dict(
                _handoff_suggestions_configuration
            )

        integration_standard_wifi_broadcast_create_update_dto = cls(
            type_=type_,
            name=name,
            enabled=enabled,
            security_configuration=security_configuration,
            multicast_to_unicast_conversion_enabled=multicast_to_unicast_conversion_enabled,
            client_isolation_enabled=client_isolation_enabled,
            hide_name=hide_name,
            uapsd_enabled=uapsd_enabled,
            channel_2_g_locked_to_6=channel_2_g_locked_to_6,
            dtim_period_2_g_locked_to_3=dtim_period_2_g_locked_to_3,
            broadcasting_frequencies_g_hz=broadcasting_frequencies_g_hz,
            arp_proxy_enabled=arp_proxy_enabled,
            bss_transition_enabled=bss_transition_enabled,
            advertise_device_name=advertise_device_name,
            network=network,
            broadcasting_device_filter=broadcasting_device_filter,
            mdns_proxy_configuration=mdns_proxy_configuration,
            multicast_filtering_policy=multicast_filtering_policy,
            basic_data_rate_kbps_by_frequency_g_hz=basic_data_rate_kbps_by_frequency_g_hz,
            client_filtering_policy=client_filtering_policy,
            blackout_schedule_configuration=blackout_schedule_configuration,
            hotspot_configuration=hotspot_configuration,
            mlo_enabled=mlo_enabled,
            band_steering_enabled=band_steering_enabled,
            dtim_period_by_frequency_g_hz_override=dtim_period_by_frequency_g_hz_override,
            dns_assistance_configuration=dns_assistance_configuration,
            handoff_suggestions_configuration=handoff_suggestions_configuration,
        )

        integration_standard_wifi_broadcast_create_update_dto.additional_properties = d
        return integration_standard_wifi_broadcast_create_update_dto

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
