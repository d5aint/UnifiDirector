from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_policy_destination_traffic_filter import FirewallPolicyDestinationTrafficFilter


T = TypeVar("T", bound="FirewallPolicyDestination")


@_attrs_define
class FirewallPolicyDestination:
    """
    Attributes:
        zone_id (UUID): ID of the firewall zone to which the matched traffic is destined.
        traffic_filter (FirewallPolicyDestinationTrafficFilter | Unset):
    """

    zone_id: UUID
    traffic_filter: FirewallPolicyDestinationTrafficFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_id = str(self.zone_id)

        traffic_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic_filter, Unset):
            traffic_filter = self.traffic_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zoneId": zone_id,
            }
        )
        if traffic_filter is not UNSET:
            field_dict["trafficFilter"] = traffic_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_policy_destination_traffic_filter import FirewallPolicyDestinationTrafficFilter

        d = dict(src_dict)
        zone_id = UUID(d.pop("zoneId"))

        _traffic_filter = d.pop("trafficFilter", UNSET)
        traffic_filter: FirewallPolicyDestinationTrafficFilter | Unset
        if isinstance(_traffic_filter, Unset):
            traffic_filter = UNSET
        else:
            traffic_filter = FirewallPolicyDestinationTrafficFilter.from_dict(_traffic_filter)

        firewall_policy_destination = cls(
            zone_id=zone_id,
            traffic_filter=traffic_filter,
        )

        firewall_policy_destination.additional_properties = d
        return firewall_policy_destination

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
