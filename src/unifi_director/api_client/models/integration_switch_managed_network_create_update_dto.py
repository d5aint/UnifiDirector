from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_dhcp_guarding import NetworkDHCPGuarding
    from ..models.switch_managed_i_pv_4_configuration import SwitchManagedIPv4Configuration


T = TypeVar("T", bound="IntegrationSwitchManagedNetworkCreateUpdateDto")


@_attrs_define
class IntegrationSwitchManagedNetworkCreateUpdateDto:
    """
    Attributes:
        management (str):
        name (str):  Example: Default Network.
        enabled (bool):
        vlan_id (int): VLAN ID. Must be 1 for the default network and >= 2 for additional networks.
        isolation_enabled (bool): Whether this network is isolated from all other networks.
        cellular_backup_enabled (bool): Whether this network is allowed to use cellular data when WAN connection(s) are
            down.
        device_id (UUID): ID of the L3 switching capable device that manages this network.
        ipv_4_configuration (SwitchManagedIPv4Configuration):
        dhcp_guarding (NetworkDHCPGuarding | Unset): Details about DHCP Guarding settings for this Network.
    """

    management: str
    name: str
    enabled: bool
    vlan_id: int
    isolation_enabled: bool
    cellular_backup_enabled: bool
    device_id: UUID
    ipv_4_configuration: SwitchManagedIPv4Configuration
    dhcp_guarding: NetworkDHCPGuarding | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        management = self.management

        name = self.name

        enabled = self.enabled

        vlan_id = self.vlan_id

        isolation_enabled = self.isolation_enabled

        cellular_backup_enabled = self.cellular_backup_enabled

        device_id = str(self.device_id)

        ipv_4_configuration = self.ipv_4_configuration.to_dict()

        dhcp_guarding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_guarding, Unset):
            dhcp_guarding = self.dhcp_guarding.to_dict()

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
                "deviceId": device_id,
                "ipv4Configuration": ipv_4_configuration,
            }
        )
        if dhcp_guarding is not UNSET:
            field_dict["dhcpGuarding"] = dhcp_guarding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_dhcp_guarding import NetworkDHCPGuarding
        from ..models.switch_managed_i_pv_4_configuration import SwitchManagedIPv4Configuration

        d = dict(src_dict)
        management = d.pop("management")

        name = d.pop("name")

        enabled = d.pop("enabled")

        vlan_id = d.pop("vlanId")

        isolation_enabled = d.pop("isolationEnabled")

        cellular_backup_enabled = d.pop("cellularBackupEnabled")

        device_id = UUID(d.pop("deviceId"))

        ipv_4_configuration = SwitchManagedIPv4Configuration.from_dict(d.pop("ipv4Configuration"))

        _dhcp_guarding = d.pop("dhcpGuarding", UNSET)
        dhcp_guarding: NetworkDHCPGuarding | Unset
        if isinstance(_dhcp_guarding, Unset):
            dhcp_guarding = UNSET
        else:
            dhcp_guarding = NetworkDHCPGuarding.from_dict(_dhcp_guarding)

        integration_switch_managed_network_create_update_dto = cls(
            management=management,
            name=name,
            enabled=enabled,
            vlan_id=vlan_id,
            isolation_enabled=isolation_enabled,
            cellular_backup_enabled=cellular_backup_enabled,
            device_id=device_id,
            ipv_4_configuration=ipv_4_configuration,
            dhcp_guarding=dhcp_guarding,
        )

        integration_switch_managed_network_create_update_dto.additional_properties = d
        return integration_switch_managed_network_create_update_dto

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
