from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_mc_lag_peer_dto_role import IntegrationMcLagPeerDtoRole

T = TypeVar("T", bound="IntegrationMcLagPeerDto")


@_attrs_define
class IntegrationMcLagPeerDto:
    """
    Attributes:
        role (IntegrationMcLagPeerDtoRole):
        device_id (UUID):
        link_port_idxs (list[int]):
    """

    role: IntegrationMcLagPeerDtoRole
    device_id: UUID
    link_port_idxs: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        device_id = str(self.device_id)

        link_port_idxs = self.link_port_idxs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "deviceId": device_id,
                "linkPortIdxs": link_port_idxs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = IntegrationMcLagPeerDtoRole(d.pop("role"))

        device_id = UUID(d.pop("deviceId"))

        link_port_idxs = cast(list[int], d.pop("linkPortIdxs"))

        integration_mc_lag_peer_dto = cls(
            role=role,
            device_id=device_id,
            link_port_idxs=link_port_idxs,
        )

        integration_mc_lag_peer_dto.additional_properties = d
        return integration_mc_lag_peer_dto

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
