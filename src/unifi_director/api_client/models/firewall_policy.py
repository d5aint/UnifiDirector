from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_policy_connection_state_filter_item import FirewallPolicyConnectionStateFilterItem
from ..models.firewall_policy_ipsec_filter import FirewallPolicyIpsecFilter
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_policy_action import FirewallPolicyAction
    from ..models.firewall_policy_destination import FirewallPolicyDestination
    from ..models.firewall_policy_ip_protocol_scope import FirewallPolicyIPProtocolScope
    from ..models.firewall_policy_source import FirewallPolicySource
    from ..models.firewall_schedule import FirewallSchedule
    from ..models.user_or_system_defined_or_derived_entity_metadata import UserOrSystemDefinedOrDerivedEntityMetadata


T = TypeVar("T", bound="FirewallPolicy")


@_attrs_define
class FirewallPolicy:
    """
    Attributes:
        id (UUID):
        enabled (bool):
        name (str):  Example: My firewall policy.
        index (int):
        action (FirewallPolicyAction): Defines action for matched traffic.
        source (FirewallPolicySource):
        destination (FirewallPolicyDestination):
        ip_protocol_scope (FirewallPolicyIPProtocolScope): Defines rules for matching by IP version and protocol.
        logging_enabled (bool): Generate syslog entries when traffic is matched. Such entries are sent to a remote
            syslog server.
        metadata (UserOrSystemDefinedOrDerivedEntityMetadata):
        description (str | Unset):  Example: A description for my firewall policy.
        connection_state_filter (list[FirewallPolicyConnectionStateFilterItem] | Unset): Match on firewall connection
            state. If null, matches all connection states.
        ipsec_filter (FirewallPolicyIpsecFilter | Unset): Match on traffic encrypted, or not encrypted by IPsec. If
            null, matches all traffic.
        schedule (FirewallSchedule | Unset): Defines date and time when the entity is active. If null, the entity is
            always active.
    """

    id: UUID
    enabled: bool
    name: str
    index: int
    action: FirewallPolicyAction
    source: FirewallPolicySource
    destination: FirewallPolicyDestination
    ip_protocol_scope: FirewallPolicyIPProtocolScope
    logging_enabled: bool
    metadata: UserOrSystemDefinedOrDerivedEntityMetadata
    description: str | Unset = UNSET
    connection_state_filter: list[FirewallPolicyConnectionStateFilterItem] | Unset = UNSET
    ipsec_filter: FirewallPolicyIpsecFilter | Unset = UNSET
    schedule: FirewallSchedule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        enabled = self.enabled

        name = self.name

        index = self.index

        action = self.action.to_dict()

        source = self.source.to_dict()

        destination = self.destination.to_dict()

        ip_protocol_scope = self.ip_protocol_scope.to_dict()

        logging_enabled = self.logging_enabled

        metadata = self.metadata.to_dict()

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
                "id": id,
                "enabled": enabled,
                "name": name,
                "index": index,
                "action": action,
                "source": source,
                "destination": destination,
                "ipProtocolScope": ip_protocol_scope,
                "loggingEnabled": logging_enabled,
                "metadata": metadata,
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
        from ..models.user_or_system_defined_or_derived_entity_metadata import (
            UserOrSystemDefinedOrDerivedEntityMetadata,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        enabled = d.pop("enabled")

        name = d.pop("name")

        index = d.pop("index")

        action = FirewallPolicyAction.from_dict(d.pop("action"))

        source = FirewallPolicySource.from_dict(d.pop("source"))

        destination = FirewallPolicyDestination.from_dict(d.pop("destination"))

        ip_protocol_scope = FirewallPolicyIPProtocolScope.from_dict(d.pop("ipProtocolScope"))

        logging_enabled = d.pop("loggingEnabled")

        metadata = UserOrSystemDefinedOrDerivedEntityMetadata.from_dict(d.pop("metadata"))

        description = d.pop("description", UNSET)

        _connection_state_filter = d.pop("connectionStateFilter", UNSET)
        connection_state_filter: list[FirewallPolicyConnectionStateFilterItem] | Unset = UNSET
        if _connection_state_filter is not UNSET:
            connection_state_filter = []
            for connection_state_filter_item_data in _connection_state_filter:
                connection_state_filter_item = FirewallPolicyConnectionStateFilterItem(
                    connection_state_filter_item_data
                )

                connection_state_filter.append(connection_state_filter_item)

        _ipsec_filter = d.pop("ipsecFilter", UNSET)
        ipsec_filter: FirewallPolicyIpsecFilter | Unset
        if isinstance(_ipsec_filter, Unset):
            ipsec_filter = UNSET
        else:
            ipsec_filter = FirewallPolicyIpsecFilter(_ipsec_filter)

        _schedule = d.pop("schedule", UNSET)
        schedule: FirewallSchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = FirewallSchedule.from_dict(_schedule)

        firewall_policy = cls(
            id=id,
            enabled=enabled,
            name=name,
            index=index,
            action=action,
            source=source,
            destination=destination,
            ip_protocol_scope=ip_protocol_scope,
            logging_enabled=logging_enabled,
            metadata=metadata,
            description=description,
            connection_state_filter=connection_state_filter,
            ipsec_filter=ipsec_filter,
            schedule=schedule,
        )

        firewall_policy.additional_properties = d
        return firewall_policy

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
