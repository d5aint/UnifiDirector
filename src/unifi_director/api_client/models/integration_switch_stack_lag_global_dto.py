from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.integration_lag_member_dto import IntegrationLagMemberDto
    from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata


T = TypeVar("T", bound="IntegrationSwitchStackLagGlobalDto")


@_attrs_define
class IntegrationSwitchStackLagGlobalDto:
    """
    Attributes:
        type_ (str):
        id (UUID):
        members (list[IntegrationLagMemberDto]):
        metadata (UserDefinedEntityMetadata):
        switch_stack_id (UUID):
    """

    type_: str
    id: UUID
    members: list[IntegrationLagMemberDto]
    metadata: UserDefinedEntityMetadata
    switch_stack_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = str(self.id)

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        metadata = self.metadata.to_dict()

        switch_stack_id = str(self.switch_stack_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "members": members,
                "metadata": metadata,
                "switchStackId": switch_stack_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_lag_member_dto import IntegrationLagMemberDto
        from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata

        d = dict(src_dict)
        type_ = d.pop("type")

        id = UUID(d.pop("id"))

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = IntegrationLagMemberDto.from_dict(members_item_data)

            members.append(members_item)

        metadata = UserDefinedEntityMetadata.from_dict(d.pop("metadata"))

        switch_stack_id = UUID(d.pop("switchStackId"))

        integration_switch_stack_lag_global_dto = cls(
            type_=type_,
            id=id,
            members=members,
            metadata=metadata,
            switch_stack_id=switch_stack_id,
        )

        integration_switch_stack_lag_global_dto.additional_properties = d
        return integration_switch_stack_lag_global_dto

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
