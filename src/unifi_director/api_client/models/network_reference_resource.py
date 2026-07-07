from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_reference_resource_resource_type import NetworkReferenceResourceResourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_reference_detail import NetworkReferenceDetail


T = TypeVar("T", bound="NetworkReferenceResource")


@_attrs_define
class NetworkReferenceResource:
    """
    Attributes:
        resource_type (NetworkReferenceResourceResourceType):
        reference_count (int): Number of references of this type
        references (list[NetworkReferenceDetail] | Unset): List of references, present only if resourceType has API
            model defined
    """

    resource_type: NetworkReferenceResourceResourceType
    reference_count: int
    references: list[NetworkReferenceDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type.value

        reference_count = self.reference_count

        references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceType": resource_type,
                "referenceCount": reference_count,
            }
        )
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_reference_detail import NetworkReferenceDetail

        d = dict(src_dict)
        resource_type = NetworkReferenceResourceResourceType(d.pop("resourceType"))

        reference_count = d.pop("referenceCount")

        _references = d.pop("references", UNSET)
        references: list[NetworkReferenceDetail] | Unset = UNSET
        if _references is not UNSET:
            references = []
            for references_item_data in _references:
                references_item = NetworkReferenceDetail.from_dict(references_item_data)

                references.append(references_item)

        network_reference_resource = cls(
            resource_type=resource_type,
            reference_count=reference_count,
            references=references,
        )

        network_reference_resource.additional_properties = d
        return network_reference_resource

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
