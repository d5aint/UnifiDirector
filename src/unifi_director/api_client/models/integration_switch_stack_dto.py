from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.integration_switch_stack_lag_local_dto import IntegrationSwitchStackLagLocalDto
    from ..models.integration_switch_stack_member_dto import IntegrationSwitchStackMemberDto
    from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata


T = TypeVar("T", bound="IntegrationSwitchStackDto")


@_attrs_define
class IntegrationSwitchStackDto:
    """
    Attributes:
        id (UUID):
        name (str):
        members (list[IntegrationSwitchStackMemberDto]):
        lags (list[IntegrationSwitchStackLagLocalDto]):
        metadata (UserDefinedEntityMetadata):
    """

    id: UUID
    name: str
    members: list[IntegrationSwitchStackMemberDto]
    lags: list[IntegrationSwitchStackLagLocalDto]
    metadata: UserDefinedEntityMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        lags = []
        for lags_item_data in self.lags:
            lags_item = lags_item_data.to_dict()
            lags.append(lags_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "members": members,
                "lags": lags,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_switch_stack_lag_local_dto import IntegrationSwitchStackLagLocalDto
        from ..models.integration_switch_stack_member_dto import IntegrationSwitchStackMemberDto
        from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = IntegrationSwitchStackMemberDto.from_dict(members_item_data)

            members.append(members_item)

        lags = []
        _lags = d.pop("lags")
        for lags_item_data in _lags:
            lags_item = IntegrationSwitchStackLagLocalDto.from_dict(lags_item_data)

            lags.append(lags_item)

        metadata = UserDefinedEntityMetadata.from_dict(d.pop("metadata"))

        integration_switch_stack_dto = cls(
            id=id,
            name=name,
            members=members,
            lags=lags,
            metadata=metadata,
        )

        integration_switch_stack_dto.additional_properties = d
        return integration_switch_stack_dto

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
