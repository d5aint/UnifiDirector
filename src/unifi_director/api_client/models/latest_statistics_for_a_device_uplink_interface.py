from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LatestStatisticsForADeviceUplinkInterface")


@_attrs_define
class LatestStatisticsForADeviceUplinkInterface:
    """
    Attributes:
        tx_rate_bps (int | Unset):
        rx_rate_bps (int | Unset):
    """

    tx_rate_bps: int | Unset = UNSET
    rx_rate_bps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_rate_bps = self.tx_rate_bps

        rx_rate_bps = self.rx_rate_bps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_rate_bps is not UNSET:
            field_dict["txRateBps"] = tx_rate_bps
        if rx_rate_bps is not UNSET:
            field_dict["rxRateBps"] = rx_rate_bps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tx_rate_bps = d.pop("txRateBps", UNSET)

        rx_rate_bps = d.pop("rxRateBps", UNSET)

        latest_statistics_for_a_device_uplink_interface = cls(
            tx_rate_bps=tx_rate_bps,
            rx_rate_bps=rx_rate_bps,
        )

        latest_statistics_for_a_device_uplink_interface.additional_properties = d
        return latest_statistics_for_a_device_uplink_interface

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
