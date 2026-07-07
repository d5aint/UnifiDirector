from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WifiSecurityConfigurationDetailObject")


@_attrs_define
class WifiSecurityConfigurationDetailObject:
    """
    Attributes:
        type_ (str):
        radius_configuration (Any | Unset):
    """

    type_: str
    radius_configuration: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        radius_configuration = self.radius_configuration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if radius_configuration is not UNSET:
            field_dict["radiusConfiguration"] = radius_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        radius_configuration = d.pop("radiusConfiguration", UNSET)

        wifi_security_configuration_detail_object = cls(
            type_=type_,
            radius_configuration=radius_configuration,
        )

        wifi_security_configuration_detail_object.additional_properties = d
        return wifi_security_configuration_detail_object

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
