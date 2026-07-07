from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hotspot_voucher_details import HotspotVoucherDetails


T = TypeVar("T", bound="IntegrationVoucherCreationResultDto")


@_attrs_define
class IntegrationVoucherCreationResultDto:
    """
    Attributes:
        vouchers (list[HotspotVoucherDetails] | Unset):
    """

    vouchers: list[HotspotVoucherDetails] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vouchers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vouchers, Unset):
            vouchers = []
            for vouchers_item_data in self.vouchers:
                vouchers_item = vouchers_item_data.to_dict()
                vouchers.append(vouchers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vouchers is not UNSET:
            field_dict["vouchers"] = vouchers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotspot_voucher_details import HotspotVoucherDetails

        d = dict(src_dict)
        _vouchers = d.pop("vouchers", UNSET)
        vouchers: list[HotspotVoucherDetails] | Unset = UNSET
        if _vouchers is not UNSET:
            vouchers = []
            for vouchers_item_data in _vouchers:
                vouchers_item = HotspotVoucherDetails.from_dict(vouchers_item_data)

                vouchers.append(vouchers_item)

        integration_voucher_creation_result_dto = cls(
            vouchers=vouchers,
        )

        integration_voucher_creation_result_dto.additional_properties = d
        return integration_voucher_creation_result_dto

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
