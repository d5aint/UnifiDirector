from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_or_update_firewall_policy_connection_state_filter_item import (
    CreateOrUpdateFirewallPolicyConnectionStateFilterItem,
)
from ..models.create_or_update_firewall_policy_ipsec_filter import CreateOrUpdateFirewallPolicyIpsecFilter
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_policy_action import FirewallPolicyAction
    from ..models.firewall_policy_destination import FirewallPolicyDestination
    from ..models.firewall_policy_ip_protocol_scope import FirewallPolicyIPProtocolScope
    from ..models.firewall_policy_source import FirewallPolicySource
    from ..models.firewall_schedule import FirewallSchedule


T = TypeVar("T", bound="CreateOrUpdateFirewallPolicy")


@_attrs_define
class CreateOrUpdateFirewallPolicy:
    """
    Attributes:
        enabled (bool):
        name (str):  Example: My firewall policy.
        action (FirewallPolicyAction): Defines action for matched traffic.
        source (FirewallPolicySource):
        destination (FirewallPolicyDestination):
        ip_protocol_scope (FirewallPolicyIPProtocolScope): Defines rules for matching by IP version and protocol.
        logging_enabled (bool): Generate syslog entries when traffic is matched. Such entries are sent to a remote
            syslog server.
        description (str | Unset):  Example: A description for my firewall policy.
        connection_state_filter (list[CreateOrUpdateFirewallPolicyConnectionStateFilterItem] | Unset): Match on firewall
            connection state. If null, matches all connection states.
        ipsec_filter (CreateOrUpdateFirewallPolicyIpsecFilter | Unset): Match on traffic encrypted, or not encrypted by
            IPsec. If null, matches all traffic.
        schedule (FirewallSchedule | Unset): Defines date and time when the entity is active. If null, the entity is
            always active.
    """

    enabled: bool
    name: str
    action: FirewallPolicyAction
    source: FirewallPolicySource
    destination: FirewallPolicyDestination
    ip_protocol_scope: FirewallPolicyIPProtocolScope
    logging_enabled: bool
    description: str | Unset = UNSET
    connection_state_filter: list[CreateOrUpdateFirewallPolicyConnectionStateFilterItem] | Unset = UNSET
    ipsec_filter: CreateOrUpdateFirewallPolicyIpsecFilter | Unset = UNSET
    schedule: FirewallSchedule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        name = self.name

        action = self.action.to_dict()

        source = self.source.to_dict()

        destination = self.destination.to_dict()

        ip_protocol_scope = self.ip_protocol_scope.to_dict()

        logging_enabled = self.logging_enabled

        description = self.description

        connection_state_filter: list[str] | Unset = UNSET
        if not isinstance(self.connection_state_filter, Unset):
            connection_state_filter = []
            for connection_state_filter_item_data in self.connection_state_filter:
                connection_state_filter_item = connection_state_filter_item_data.value
                connection_state_filter.append(connection_state_filter_item)

        ipsec_filter: str | Unset = UNSET
        if not isinstance(self.ipsec_filter, Unset):
            ipsec_filter = self.ipsec_filter.value

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "name": name,
                "action": action,
                "source": source,
                "destination": destination,
                "ipProtocolScope": ip_protocol_scope,
                "loggingEnabled": logging_enabled,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if connection_state_filter is not UNSET:
            field_dict["connectionStateFilter"] = connection_state_filter
        if ipsec_filter is not UNSET:
            field_dict["ipsecFilter"] = ipsec_filter
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_policy_action import FirewallPolicyAction
        from ..models.firewall_policy_destination import FirewallPolicyDestination
        from ..models.firewall_policy_ip_protocol_scope import FirewallPolicyIPProtocolScope
        from ..models.firewall_policy_source import FirewallPolicySource
        from ..models.firewall_schedule import FirewallSchedule

        d = dict(src_dict)
        enabled = d.pop("enabled")

        name = d.pop("name")

        action = FirewallPolicyAction.from_dict(d.pop("action"))

        source = FirewallPolicySource.from_dict(d.pop("source"))

        destination = FirewallPolicyDestination.from_dict(d.pop("destination"))

        ip_protocol_scope = FirewallPolicyIPProtocolScope.from_dict(d.pop("ipProtocolScope"))

        logging_enabled = d.pop("loggingEnabled")

        description = d.pop("description", UNSET)

        _connection_state_filter = d.pop("connectionStateFilter", UNSET)
        connection_state_filter: list[CreateOrUpdateFirewallPolicyConnectionStateFilterItem] | Unset = UNSET
        if _connection_state_filter is not UNSET:
            connection_state_filter = []
            for connection_state_filter_item_data in _connection_state_filter:
                connection_state_filter_item = CreateOrUpdateFirewallPolicyConnectionStateFilterItem(
                    connection_state_filter_item_data
                )

                connection_state_filter.append(connection_state_filter_item)

        _ipsec_filter = d.pop("ipsecFilter", UNSET)
        ipsec_filter: CreateOrUpdateFirewallPolicyIpsecFilter | Unset
        if isinstance(_ipsec_filter, Unset):
            ipsec_filter = UNSET
        else:
            ipsec_filter = CreateOrUpdateFirewallPolicyIpsecFilter(_ipsec_filter)

        _schedule = d.pop("schedule", UNSET)
        schedule: FirewallSchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = FirewallSchedule.from_dict(_schedule)

        create_or_update_firewall_policy = cls(
            enabled=enabled,
            name=name,
            action=action,
            source=source,
            destination=destination,
            ip_protocol_scope=ip_protocol_scope,
            logging_enabled=logging_enabled,
            description=description,
            connection_state_filter=connection_state_filter,
            ipsec_filter=ipsec_filter,
            schedule=schedule,
        )

        create_or_update_firewall_policy.additional_properties = d
        return create_or_update_firewall_policy

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
