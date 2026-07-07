from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_policy_i_pv_6_interface_identifier_filter import FirewallPolicyIPv6InterfaceIdentifierFilter
    from ..models.firewall_policy_port_filter import FirewallPolicyPortFilter


T = TypeVar("T", bound="IntegrationFirewallPolicySourceIpv6IidFilterDto")


@_attrs_define
class IntegrationFirewallPolicySourceIpv6IidFilterDto:
    """
    Attributes:
        type_ (str):
        ipv_6_iid_filter (FirewallPolicyIPv6InterfaceIdentifierFilter):
        mac_address_filter (str | Unset): Match source traffic additionally by a MAC address. If null, match all MAC
            addresses.
        port_filter (FirewallPolicyPortFilter | Unset): Defines rules for matching traffic by port.
    """

    type_: str
    ipv_6_iid_filter: FirewallPolicyIPv6InterfaceIdentifierFilter
    mac_address_filter: str | Unset = UNSET
    port_filter: FirewallPolicyPortFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ipv_6_iid_filter = self.ipv_6_iid_filter.to_dict()

        mac_address_filter = self.mac_address_filter

        port_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_filter, Unset):
            port_filter = self.port_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ipv6IidFilter": ipv_6_iid_filter,
            }
        )
        if mac_address_filter is not UNSET:
            field_dict["macAddressFilter"] = mac_address_filter
        if port_filter is not UNSET:
            field_dict["portFilter"] = port_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_policy_i_pv_6_interface_identifier_filter import (
            FirewallPolicyIPv6InterfaceIdentifierFilter,
        )
        from ..models.firewall_policy_port_filter import FirewallPolicyPortFilter

        d = dict(src_dict)
        type_ = d.pop("type")

        ipv_6_iid_filter = FirewallPolicyIPv6InterfaceIdentifierFilter.from_dict(d.pop("ipv6IidFilter"))

        mac_address_filter = d.pop("macAddressFilter", UNSET)

        _port_filter = d.pop("portFilter", UNSET)
        port_filter: FirewallPolicyPortFilter | Unset
        if isinstance(_port_filter, Unset):
            port_filter = UNSET
        else:
            port_filter = FirewallPolicyPortFilter.from_dict(_port_filter)

        integration_firewall_policy_source_ipv_6_iid_filter_dto = cls(
            type_=type_,
            ipv_6_iid_filter=ipv_6_iid_filter,
            mac_address_filter=mac_address_filter,
            port_filter=port_filter,
        )

        integration_firewall_policy_source_ipv_6_iid_filter_dto.additional_properties = d
        return integration_firewall_policy_source_ipv_6_iid_filter_dto

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
