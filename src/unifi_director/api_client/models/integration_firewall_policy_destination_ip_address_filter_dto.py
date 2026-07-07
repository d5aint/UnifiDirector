from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_policy_ip_address_filter import FirewallPolicyIPAddressFilter
    from ..models.firewall_policy_port_filter import FirewallPolicyPortFilter


T = TypeVar("T", bound="IntegrationFirewallPolicyDestinationIpAddressFilterDto")


@_attrs_define
class IntegrationFirewallPolicyDestinationIpAddressFilterDto:
    """
    Attributes:
        type_ (str):
        ip_address_filter (FirewallPolicyIPAddressFilter): Match traffic originating from, or destined to selected IP
            addresses.
        port_filter (FirewallPolicyPortFilter | Unset): Defines rules for matching traffic by port.
    """

    type_: str
    ip_address_filter: FirewallPolicyIPAddressFilter
    port_filter: FirewallPolicyPortFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ip_address_filter = self.ip_address_filter.to_dict()

        port_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_filter, Unset):
            port_filter = self.port_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ipAddressFilter": ip_address_filter,
            }
        )
        if port_filter is not UNSET:
            field_dict["portFilter"] = port_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_policy_ip_address_filter import FirewallPolicyIPAddressFilter
        from ..models.firewall_policy_port_filter import FirewallPolicyPortFilter

        d = dict(src_dict)
        type_ = d.pop("type")

        ip_address_filter = FirewallPolicyIPAddressFilter.from_dict(d.pop("ipAddressFilter"))

        _port_filter = d.pop("portFilter", UNSET)
        port_filter: FirewallPolicyPortFilter | Unset
        if isinstance(_port_filter, Unset):
            port_filter = UNSET
        else:
            port_filter = FirewallPolicyPortFilter.from_dict(_port_filter)

        integration_firewall_policy_destination_ip_address_filter_dto = cls(
            type_=type_,
            ip_address_filter=ip_address_filter,
            port_filter=port_filter,
        )

        integration_firewall_policy_destination_ip_address_filter_dto.additional_properties = d
        return integration_firewall_policy_destination_ip_address_filter_dto

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
