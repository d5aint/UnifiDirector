from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dns_policy import DNSPolicy


T = TypeVar("T", bound="IntegrationDnsPolicyPageDto")


@_attrs_define
class IntegrationDnsPolicyPageDto:
    """
    Attributes:
        offset (int):
        limit (int):  Example: 25.
        count (int):  Example: 10.
        total_count (int):  Example: 1000.
        data (list[DNSPolicy]):
    """

    offset: int
    limit: int
    count: int
    total_count: int
    data: list[DNSPolicy]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        count = self.count

        total_count = self.total_count

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
                "count": count,
                "totalCount": total_count,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_policy import DNSPolicy

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        count = d.pop("count")

        total_count = d.pop("totalCount")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = DNSPolicy.from_dict(data_item_data)

            data.append(data_item)

        integration_dns_policy_page_dto = cls(
            offset=offset,
            limit=limit,
            count=count,
            total_count=total_count,
            data=data,
        )

        integration_dns_policy_page_dto.additional_properties = d
        return integration_dns_policy_page_dto

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
