from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.integration_mc_lag_local_dto import IntegrationMcLagLocalDto
    from ..models.integration_mc_lag_peer_dto import IntegrationMcLagPeerDto
    from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata


T = TypeVar("T", bound="IntegrationMcLagDomainDto")


@_attrs_define
class IntegrationMcLagDomainDto:
    """
    Attributes:
        id (UUID):
        name (str):
        peers (list[IntegrationMcLagPeerDto]):
        lags (list[IntegrationMcLagLocalDto]):
        metadata (UserDefinedEntityMetadata):
    """

    id: UUID
    name: str
    peers: list[IntegrationMcLagPeerDto]
    lags: list[IntegrationMcLagLocalDto]
    metadata: UserDefinedEntityMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        peers = []
        for peers_item_data in self.peers:
            peers_item = peers_item_data.to_dict()
            peers.append(peers_item)

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
                "peers": peers,
                "lags": lags,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_mc_lag_local_dto import IntegrationMcLagLocalDto
        from ..models.integration_mc_lag_peer_dto import IntegrationMcLagPeerDto
        from ..models.user_defined_entity_metadata import UserDefinedEntityMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        peers = []
        _peers = d.pop("peers")
        for peers_item_data in _peers:
            peers_item = IntegrationMcLagPeerDto.from_dict(peers_item_data)

            peers.append(peers_item)

        lags = []
        _lags = d.pop("lags")
        for lags_item_data in _lags:
            lags_item = IntegrationMcLagLocalDto.from_dict(lags_item_data)

            lags.append(lags_item)

        metadata = UserDefinedEntityMetadata.from_dict(d.pop("metadata"))

        integration_mc_lag_domain_dto = cls(
            id=id,
            name=name,
            peers=peers,
            lags=lags,
            metadata=metadata,
        )

        integration_mc_lag_domain_dto.additional_properties = d
        return integration_mc_lag_domain_dto

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
