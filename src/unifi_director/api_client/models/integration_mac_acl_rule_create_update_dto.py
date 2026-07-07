from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acl_rule_update_action import ACLRuleUpdateAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_rule_device_filter import ACLRuleDeviceFilter
    from ..models.macacl_rule_endpoint import MACACLRuleEndpoint


T = TypeVar("T", bound="IntegrationMacAclRuleCreateUpdateDto")


@_attrs_define
class IntegrationMacAclRuleCreateUpdateDto:
    """
    Attributes:
        type_ (str):
        enabled (bool):  Example: True.
        name (str): ACL rule name
        action (ACLRuleUpdateAction): ACL rule action Example: ALLOW|BLOCK.
        network_id_filter (UUID): Network ID to which this ACL rule applies
        description (str | Unset): ACL rule description
        enforcing_device_filter (ACLRuleDeviceFilter | Unset):
        index (int | Unset): ACL rule index. This property is deprecated and has no effect. Use the dedicated ACL rule
            reordering endpoint.
        source_filter (MACACLRuleEndpoint | Unset): Traffic source filter
        destination_filter (MACACLRuleEndpoint | Unset): Traffic destination filter
    """

    type_: str
    enabled: bool
    name: str
    action: ACLRuleUpdateAction
    network_id_filter: UUID
    description: str | Unset = UNSET
    enforcing_device_filter: ACLRuleDeviceFilter | Unset = UNSET
    index: int | Unset = UNSET
    source_filter: MACACLRuleEndpoint | Unset = UNSET
    destination_filter: MACACLRuleEndpoint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        enabled = self.enabled

        name = self.name

        action = self.action.value

        network_id_filter = str(self.network_id_filter)

        description = self.description

        enforcing_device_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enforcing_device_filter, Unset):
            enforcing_device_filter = self.enforcing_device_filter.to_dict()

        index = self.index

        source_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_filter, Unset):
            source_filter = self.source_filter.to_dict()

        destination_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination_filter, Unset):
            destination_filter = self.destination_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "enabled": enabled,
                "name": name,
                "action": action,
                "networkIdFilter": network_id_filter,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enforcing_device_filter is not UNSET:
            field_dict["enforcingDeviceFilter"] = enforcing_device_filter
        if index is not UNSET:
            field_dict["index"] = index
        if source_filter is not UNSET:
            field_dict["sourceFilter"] = source_filter
        if destination_filter is not UNSET:
            field_dict["destinationFilter"] = destination_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acl_rule_device_filter import ACLRuleDeviceFilter
        from ..models.macacl_rule_endpoint import MACACLRuleEndpoint

        d = dict(src_dict)
        type_ = d.pop("type")

        enabled = d.pop("enabled")

        name = d.pop("name")

        action = ACLRuleUpdateAction(d.pop("action"))

        network_id_filter = UUID(d.pop("networkIdFilter"))

        description = d.pop("description", UNSET)

        _enforcing_device_filter = d.pop("enforcingDeviceFilter", UNSET)
        enforcing_device_filter: ACLRuleDeviceFilter | Unset
        if isinstance(_enforcing_device_filter, Unset):
            enforcing_device_filter = UNSET
        else:
            enforcing_device_filter = ACLRuleDeviceFilter.from_dict(_enforcing_device_filter)

        index = d.pop("index", UNSET)

        _source_filter = d.pop("sourceFilter", UNSET)
        source_filter: MACACLRuleEndpoint | Unset
        if isinstance(_source_filter, Unset):
            source_filter = UNSET
        else:
            source_filter = MACACLRuleEndpoint.from_dict(_source_filter)

        _destination_filter = d.pop("destinationFilter", UNSET)
        destination_filter: MACACLRuleEndpoint | Unset
        if isinstance(_destination_filter, Unset):
            destination_filter = UNSET
        else:
            destination_filter = MACACLRuleEndpoint.from_dict(_destination_filter)

        integration_mac_acl_rule_create_update_dto = cls(
            type_=type_,
            enabled=enabled,
            name=name,
            action=action,
            network_id_filter=network_id_filter,
            description=description,
            enforcing_device_filter=enforcing_device_filter,
            index=index,
            source_filter=source_filter,
            destination_filter=destination_filter,
        )

        integration_mac_acl_rule_create_update_dto.additional_properties = d
        return integration_mac_acl_rule_create_update_dto

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
