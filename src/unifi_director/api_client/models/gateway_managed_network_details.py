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
    from ..models.user_or_system_defined_or_orchestrated_entity_metadata import (
        UserOrSystemDefinedOrOrchestratedEntityMetadata,
    )


T = TypeVar("T", bound="GatewayManagedNetworkDetails")


@_attrs_define
class GatewayManagedNetworkDetails:
    """
    Attributes:
        management (str):
        id (UUID):
        name (str):  Example: Default Network.
        enabled (bool):
        vlan_id (int): VLAN ID. Must be 1 for the default network and >= 2 for additional networks.
        metadata (UserOrSystemDefinedOrOrchestratedEntityMetadata):
        default (bool):
        isolation_enabled (bool): Whether this network is isolated from all other networks.
        cellular_backup_enabled (bool): Whether this network is allowed to use cellular data when WAN connection(s) are
            down.
        internet_access_enabled (bool): Whether the internet access is allowed for the device on this network.
        mdns_forwarding_enabled (bool): Whether this network should participate in mDNS traffic forwarding.
        ipv_4_configuration (GatewayManagedIPv4Configuration):
        dhcp_guarding (NetworkDHCPGuarding | Unset): Details about DHCP Guarding settings for this Network.
        zone_id (UUID | Unset): Firewall zone ID associated with this Network.
        ipv_6_configuration (NetworkIPv6Configuration | Unset):
    """

    management: str
    id: UUID
    name: str
    enabled: bool
    vlan_id: int
    metadata: UserOrSystemDefinedOrOrchestratedEntityMetadata
    default: bool
    isolation_enabled: bool
    cellular_backup_enabled: bool
    internet_access_enabled: bool
    mdns_forwarding_enabled: bool
    ipv_4_configuration: GatewayManagedIPv4Configuration
    dhcp_guarding: NetworkDHCPGuarding | Unset = UNSET
    zone_id: UUID | Unset = UNSET
    ipv_6_configuration: NetworkIPv6Configuration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        management = self.management

        id = str(self.id)

        name = self.name

        enabled = self.enabled

        vlan_id = self.vlan_id

        metadata = self.metadata.to_dict()

        default = self.default

        isolation_enabled = self.isolation_enabled

        cellular_backup_enabled = self.cellular_backup_enabled

        internet_access_enabled = self.internet_access_enabled

        mdns_forwarding_enabled = self.mdns_forwarding_enabled

        ipv_4_configuration = self.ipv_4_configuration.to_dict()

        dhcp_guarding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_guarding, Unset):
            dhcp_guarding = self.dhcp_guarding.to_dict()

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)

        ipv_6_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv_6_configuration, Unset):
            ipv_6_configuration = self.ipv_6_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "management": management,
                "id": id,
                "name": name,
                "enabled": enabled,
                "vlanId": vlan_id,
                "metadata": metadata,
                "default": default,
                "isolationEnabled": isolation_enabled,
                "cellularBackupEnabled": cellular_backup_enabled,
                "internetAccessEnabled": internet_access_enabled,
                "mdnsForwardingEnabled": mdns_forwarding_enabled,
                "ipv4Configuration": ipv_4_configuration,
            }
        )
        if dhcp_guarding is not UNSET:
            field_dict["dhcpGuarding"] = dhcp_guarding
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if ipv_6_configuration is not UNSET:
            field_dict["ipv6Configuration"] = ipv_6_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_managed_i_pv_4_configuration import GatewayManagedIPv4Configuration
        from ..models.network_dhcp_guarding import NetworkDHCPGuarding
        from ..models.network_i_pv_6_configuration import NetworkIPv6Configuration
        from ..models.user_or_system_defined_or_orchestrated_entity_metadata import (
            UserOrSystemDefinedOrOrchestratedEntityMetadata,
        )

        d = dict(src_dict)
        management = d.pop("management")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        enabled = d.pop("enabled")

        vlan_id = d.pop("vlanId")

        metadata = UserOrSystemDefinedOrOrchestratedEntityMetadata.from_dict(d.pop("metadata"))

        default = d.pop("default")

        isolation_enabled = d.pop("isolationEnabled")

        cellular_backup_enabled = d.pop("cellularBackupEnabled")

        internet_access_enabled = d.pop("internetAccessEnabled")

        mdns_forwarding_enabled = d.pop("mdnsForwardingEnabled")

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

        _ipv_6_configuration = d.pop("ipv6Configuration", UNSET)
        ipv_6_configuration: NetworkIPv6Configuration | Unset
        if isinstance(_ipv_6_configuration, Unset):
            ipv_6_configuration = UNSET
        else:
            ipv_6_configuration = NetworkIPv6Configuration.from_dict(_ipv_6_configuration)

        gateway_managed_network_details = cls(
            management=management,
            id=id,
            name=name,
            enabled=enabled,
            vlan_id=vlan_id,
            metadata=metadata,
            default=default,
            isolation_enabled=isolation_enabled,
            cellular_backup_enabled=cellular_backup_enabled,
            internet_access_enabled=internet_access_enabled,
            mdns_forwarding_enabled=mdns_forwarding_enabled,
            ipv_4_configuration=ipv_4_configuration,
            dhcp_guarding=dhcp_guarding,
            zone_id=zone_id,
            ipv_6_configuration=ipv_6_configuration,
        )

        gateway_managed_network_details.additional_properties = d
        return gateway_managed_network_details

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
