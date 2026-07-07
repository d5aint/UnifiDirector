from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.network_reference_resource import NetworkReferenceResource


T = TypeVar("T", bound="NetworkReferences")


@_attrs_define
class NetworkReferences:
    """
    Attributes:
        reference_resources (list[NetworkReferenceResource]): List of network reference resources
    """

    reference_resources: list[NetworkReferenceResource]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_resources = []
        for reference_resources_item_data in self.reference_resources:
            reference_resources_item = reference_resources_item_data.to_dict()
            reference_resources.append(reference_resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "referenceResources": reference_resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_reference_resource import NetworkReferenceResource

        d = dict(src_dict)
        reference_resources = []
        _reference_resources = d.pop("referenceResources")
        for reference_resources_item_data in _reference_resources:
            reference_resources_item = NetworkReferenceResource.from_dict(reference_resources_item_data)

            reference_resources.append(reference_resources_item)

        network_references = cls(
            reference_resources=reference_resources,
        )

        network_references.additional_properties = d
        return network_references

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
