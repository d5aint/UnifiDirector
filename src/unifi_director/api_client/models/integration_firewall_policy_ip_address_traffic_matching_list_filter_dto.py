from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IntegrationFirewallPolicyIpAddressTrafficMatchingListFilterDto")


@_attrs_define
class IntegrationFirewallPolicyIpAddressTrafficMatchingListFilterDto:
    """
    Attributes:
        type_ (str):
        match_opposite (bool): Match on all IP addresses except the specified ones.
        traffic_matching_list_id (UUID): ID of Traffic Matching List containing IP addresses to match.
    """

    type_: str
    match_opposite: bool
    traffic_matching_list_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        match_opposite = self.match_opposite

        traffic_matching_list_id = str(self.traffic_matching_list_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "matchOpposite": match_opposite,
                "trafficMatchingListId": traffic_matching_list_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        match_opposite = d.pop("matchOpposite")

        traffic_matching_list_id = UUID(d.pop("trafficMatchingListId"))

        integration_firewall_policy_ip_address_traffic_matching_list_filter_dto = cls(
            type_=type_,
            match_opposite=match_opposite,
            traffic_matching_list_id=traffic_matching_list_id,
        )

        integration_firewall_policy_ip_address_traffic_matching_list_filter_dto.additional_properties = d
        return integration_firewall_policy_ip_address_traffic_matching_list_filter_dto

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
