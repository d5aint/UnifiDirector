from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.latest_statistics_for_wireless_radio import LatestStatisticsForWirelessRadio


T = TypeVar("T", bound="LatestStatisticsForDeviceInterfaces")


@_attrs_define
class LatestStatisticsForDeviceInterfaces:
    """
    Attributes:
        radios (list[LatestStatisticsForWirelessRadio] | Unset):
    """

    radios: list[LatestStatisticsForWirelessRadio] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radios: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.radios, Unset):
            radios = []
            for radios_item_data in self.radios:
                radios_item = radios_item_data.to_dict()
                radios.append(radios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radios is not UNSET:
            field_dict["radios"] = radios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.latest_statistics_for_wireless_radio import LatestStatisticsForWirelessRadio

        d = dict(src_dict)
        _radios = d.pop("radios", UNSET)
        radios: list[LatestStatisticsForWirelessRadio] | Unset = UNSET
        if _radios is not UNSET:
            radios = []
            for radios_item_data in _radios:
                radios_item = LatestStatisticsForWirelessRadio.from_dict(radios_item_data)

                radios.append(radios_item)

        latest_statistics_for_device_interfaces = cls(
            radios=radios,
        )

        latest_statistics_for_device_interfaces.additional_properties = d
        return latest_statistics_for_device_interfaces

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
