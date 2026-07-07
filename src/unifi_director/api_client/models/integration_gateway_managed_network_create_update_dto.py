from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_managed_i_pv_4_configuration import GatewayManagedIPv4Configuration
    from ..models.network_dhcp_guarding import NetworkDHCPGuarding
    from ..models.network_i_pv_6_configuration import NetworkIPv6Configuration


T = TypeVar("T", bound="IntegrationGatewayManagedNetworkCreateUpdateDto")


@_attrs_define
class IntegrationGatewayManagedNetworkCreateUpdateDto:
    """
    Attributes:
        management (str):
        name (str):  Example: Default Network.
        enabled (bool):
        vlan_id (int): VLAN ID. Must be 1 for the default network and >= 2 for additional networks.
        isolation_enabled (bool): Whether this network is isolated from all other networks.
        cellular_backup_enabled (bool): Whether this network is allowed to use cellular data when WAN connection(s) are
            down.
        internet_access_enabled (bool): Whether the internet access is allowed for the device on this network.
        ipv_4_configuration (GatewayManagedIPv4Configuration):
        dhcp_guarding (NetworkDHCPGuarding | Unset): Details about DHCP Guarding settings for this Network.
        zone_id (UUID | Unset): Firewall zone ID associated with this Network.
        mdns_forwarding_enabled (bool | Unset): Whether this network should participate in mDNS traffic forwarding. If
            null, the default from the site mDNS setting is used.
        ipv_6_configuration (NetworkIPv6Configuration | Unset):
    """

    management: str
    name: str
    enabled: bool
    vlan_id: int
    isolation_enabled: bool
    cellular_backup_enabled: bool
    internet_access_enabled: bool
    ipv_4_configuration: GatewayManagedIPv4Configuration
    dhcp_guarding: NetworkDHCPGuarding | Unset = UNSET
    zone_id: UUID | Unset = UNSET
    mdns_forwarding_enabled: bool | Unset = UNSET
    ipv_6_configuration: NetworkIPv6Configuration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        management = self.management

        name = self.name

        enabled = self.enabled

        vlan_id = self.vlan_id

        isolation_enabled = self.isolation_enabled

        cellular_backup_enabled = self.cellular_backup_enabled

        internet_access_enabled = self.internet_access_enabled

        ipv_4_configuration = self.ipv_4_configuration.to_dict()

        dhcp_guarding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_guarding, Unset):
            dhcp_guarding = self.dhcp_guarding.to_dict()

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)

        mdns_forwarding_enabled = self.mdns_forwarding_enabled

        ipv_6_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_6_configuration, Unset):
            ipv_6_configuration = self.ipv_6_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "management": management,
                "name": name,
                "enabled": enabled,
                "vlanId": vlan_id,
                "isolationEnabled": isolation_enabled,
                "cellularBackupEnabled": cellular_backup_enabled,
                "internetAccessEnabled": internet_access_enabled,
                "ipv4Configuration": ipv_4_configuration,
            }
        )
        if dhcp_guarding is not UNSET:
            field_dict["dhcpGuarding"] = dhcp_guarding
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if mdns_forwarding_enabled is not UNSET:
            field_dict["mdnsForwardingEnabled"] = mdns_forwarding_enabled
        if ipv_6_configuration is not UNSET:
            field_dict["ipv6Configuration"] = ipv_6_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_managed_i_pv_4_configuration import GatewayManagedIPv4Configuration
        from ..models.network_dhcp_guarding import NetworkDHCPGuarding
        from ..models.network_i_pv_6_configuration import NetworkIPv6Configuration

        d = dict(src_dict)
        management = d.pop("management")

        name = d.pop("name")

        enabled = d.pop("enabled")

        vlan_id = d.pop("vlanId")

        isolation_enabled = d.pop("isolationEnabled")

        cellular_backup_enabled = d.pop("cellularBackupEnabled")

        internet_access_enabled = d.pop("internetAccessEnabled")

        ipv_4_configuration = GatewayManagedIPv4Configuration.from_dict(d.pop("ipv4Configuration"))

        _dhcp_guarding = d.pop("dhcpGuarding", UNSET)
        dhcp_guarding: NetworkDHCPGuarding | Unset
        if isinstance(_dhcp_guarding, Unset):
            dhcp_guarding = UNSET
        else:
            dhcp_guarding = NetworkDHCPGuarding.from_dict(_dhcp_guarding)

        _zone_id = d.pop("zoneId", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id, Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)

        mdns_forwarding_enabled = d.pop("mdnsForwardingEnabled", UNSET)

        _ipv_6_configuration = d.pop("ipv6Configuration", UNSET)
        ipv_6_configuration: NetworkIPv6Configuration | Unset
        if isinstance(_ipv_6_configuration, Unset):
            ipv_6_configuration = UNSET
        else:
            ipv_6_configuration = NetworkIPv6Configuration.from_dict(_ipv_6_configuration)

        integration_gateway_managed_network_create_update_dto = cls(
            management=management,
            name=name,
            enabled=enabled,
            vlan_id=vlan_id,
            isolation_enabled=isolation_enabled,
            cellular_backup_enabled=cellular_backup_enabled,
            internet_access_enabled=internet_access_enabled,
            ipv_4_configuration=ipv_4_configuration,
            dhcp_guarding=dhcp_guarding,
            zone_id=zone_id,
            mdns_forwarding_enabled=mdns_forwarding_enabled,
            ipv_6_configuration=ipv_6_configuration,
        )

        integration_gateway_managed_network_create_update_dto.additional_properties = d
        return integration_gateway_managed_network_create_update_dto

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
