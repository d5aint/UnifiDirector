from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FirewallPolicySiteToSiteVPNTunnelFilter")


@_attrs_define
class FirewallPolicySiteToSiteVPNTunnelFilter:
    """
    Attributes:
        site_to_site_vpn_tunnel_id (UUID):
    """

    site_to_site_vpn_tunnel_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_to_site_vpn_tunnel_id = str(self.site_to_site_vpn_tunnel_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteToSiteVpnTunnelId": site_to_site_vpn_tunnel_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_to_site_vpn_tunnel_id = UUID(d.pop("siteToSiteVpnTunnelId"))

        firewall_policy_site_to_site_vpn_tunnel_filter = cls(
            site_to_site_vpn_tunnel_id=site_to_site_vpn_tunnel_id,
        )

        firewall_policy_site_to_site_vpn_tunnel_filter.additional_properties = d
        return firewall_policy_site_to_site_vpn_tunnel_filter

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
