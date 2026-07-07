from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.port_overview_connector import PortOverviewConnector
from ..models.port_overview_state import PortOverviewState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_po_e_overview import PortPoEOverview


T = TypeVar("T", bound="PortOverview")


@_attrs_define
class PortOverview:
    """
    Attributes:
        idx (int):  Example: 1.
        state (PortOverviewState):
        connector (PortOverviewConnector):
        max_speed_mbps (int):  Example: 10000.
        speed_mbps (int | Unset):  Example: 1000.
        poe (PortPoEOverview | Unset):
    """

    idx: int
    state: PortOverviewState
    connector: PortOverviewConnector
    max_speed_mbps: int
    speed_mbps: int | Unset = UNSET
    poe: PortPoEOverview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idx = self.idx

        state = self.state.value

        connector = self.connector.value

        max_speed_mbps = self.max_speed_mbps

        speed_mbps = self.speed_mbps

        poe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.poe, Unset):
            poe = self.poe.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idx": idx,
                "state": state,
                "connector": connector,
                "maxSpeedMbps": max_speed_mbps,
            }
        )
        if speed_mbps is not UNSET:
            field_dict["speedMbps"] = speed_mbps
        if poe is not UNSET:
            field_dict["poe"] = poe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.port_po_e_overview import PortPoEOverview

        d = dict(src_dict)
        idx = d.pop("idx")

        state = PortOverviewState(d.pop("state"))

        connector = PortOverviewConnector(d.pop("connector"))

        max_speed_mbps = d.pop("maxSpeedMbps")

        speed_mbps = d.pop("speedMbps", UNSET)

        _poe = d.pop("poe", UNSET)
        poe: PortPoEOverview | Unset
        if isinstance(_poe, Unset):
            poe = UNSET
        else:
            poe = PortPoEOverview.from_dict(_poe)

        port_overview = cls(
            idx=idx,
            state=state,
            connector=connector,
            max_speed_mbps=max_speed_mbps,
            speed_mbps=speed_mbps,
            poe=poe,
        )

        port_overview.additional_properties = d
        return port_overview

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
