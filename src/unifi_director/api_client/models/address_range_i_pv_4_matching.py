from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddressRangeIPv4Matching")


@_attrs_define
class AddressRangeIPv4Matching:
    """
    Attributes:
        type_ (str):
        start (str): IPv4 start address Example: 192.168.1.10.
        stop (str): IPv4 stop address Example: 192.168.1.20.
    """

    type_: str
    start: str
    stop: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        start = self.start

        stop = self.stop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "start": start,
                "stop": stop,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        start = d.pop("start")

        stop = d.pop("stop")

        address_range_i_pv_4_matching = cls(
            type_=type_,
            start=start,
            stop=stop,
        )

        address_range_i_pv_4_matching.additional_properties = d
        return address_range_i_pv_4_matching

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
