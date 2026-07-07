"""UniFi Network Management Module."""

__version__ = "1.0.0"

import logging
from typing import Any, Dict, Iterator, Optional
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.errors import UnexpectedStatus
from ..api_client.models.create_or_update_network import CreateOrUpdateNetwork
from ..api_client.models.network_details import NetworkDetails
from ..api_client.models.network_references import NetworkReferences
from ..api_client.api.networks import (
    create_network,
    delete_network,
    get_network_details,
    get_network_references,
    get_networks_overview_page,
    update_network,
)

logger = logging.getLogger(__name__)


class UnifiNetworkManager:

    def __init__(self, client: Client, site_id: UUID) -> None:
        self.client = client
        self.site_id = site_id
        logger.debug(f"{self.__class__.__name__} initialized.")

    def iter_networks(self, limit: int = 200) -> Iterator[Any]:
        """Yield all networks sorted by VLAN ID."""
        offset = 0
        all_networks: list = []

        while True:
            try:
                response = get_networks_overview_page.sync(
                    client=self.client, site_id=self.site_id, offset=offset, limit=limit
                )
                data = getattr(response, "data", None)
                if not data:
                    break
                all_networks.extend(data)
                if len(data) < limit:
                    break
                offset += limit
            except (httpx.HTTPError, UnexpectedStatus) as e:
                logger.error(f"Error during network retrieval: {e}")
                break

        # WHY: Accumulate all pages before sorting so VLAN IDs are globally ordered,
        # not per-page — partial pages at boundaries would break ordering otherwise.
        all_networks.sort(key=lambda net: getattr(net, "vlan_id", 0))
        yield from all_networks

    def get_network(self, network_id: UUID | str) -> Optional[NetworkDetails]:
        target_id = UUID(str(network_id))
        try:
            return get_network_details.sync(client=self.client, site_id=self.site_id, network_id=target_id)
        except (httpx.HTTPError, UnexpectedStatus) as e:
            logger.error(f"Failed to fetch network {target_id}: {e}")
            return None

    def get_references(self, network_id: UUID | str) -> Optional[NetworkReferences]:
        target_id = UUID(str(network_id))
        try:
            return get_network_references.sync(client=self.client, site_id=self.site_id, network_id=target_id)
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch references for {target_id}: {e}")
            return None

    def create_network(self, network_data: Dict[str, Any]) -> Optional[NetworkDetails]:
        try:
            body = CreateOrUpdateNetwork.from_dict(network_data)
            return create_network.sync(client=self.client, site_id=self.site_id, body=body)
        except (httpx.HTTPError, UnexpectedStatus) as e:
            logger.error(f"Failed to create network: {e}")
            return None

    def update_network(self, network_id: UUID | str, network_data: Dict[str, Any]) -> Optional[NetworkDetails]:
        target_id = UUID(str(network_id))
        try:
            body = CreateOrUpdateNetwork.from_dict(network_data)
            return update_network.sync(client=self.client, site_id=self.site_id, network_id=target_id, body=body)
        except (httpx.HTTPError, UnexpectedStatus) as e:
            logger.error(f"Failed to update network {target_id}: {e}")
            return None

    def delete_network(self, network_id: UUID | str, force: bool = False) -> bool:
        target_id = UUID(str(network_id))
        logger.warning(f"Initiating DELETE for network: {target_id} (Force: {force})")
        try:
            delete_network.sync_detailed(client=self.client, site_id=self.site_id, network_id=target_id, force=force)
            logger.info(f"Successfully deleted network: {target_id}")
            return True
        except (httpx.HTTPError, UnexpectedStatus) as e:
            logger.error(f"Failed to delete network {target_id}: {e}")
            return False
