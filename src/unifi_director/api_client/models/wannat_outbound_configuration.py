from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WANNATOutboundConfiguration")


@_attrs_define
class WANNATOutboundConfiguration:
    """
    Attributes:
        type_ (str):
        wan_interface_id (UUID):
    """

    type_: str
    wan_interface_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        wan_interface_id = str(self.wan_interface_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "wanInterfaceId": wan_interface_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        wan_interface_id = UUID(d.pop("wanInterfaceId"))

        wannat_outbound_configuration = cls(
            type_=type_,
            wan_interface_id=wan_interface_id,
        )

        wannat_outbound_configuration.additional_properties = d
        return wannat_outbound_configuration

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
