"""UniFi Traffic Matching List Management Module."""

__version__ = "1.0.0"

import logging
from typing import Any, Dict, Iterator, Optional
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.errors import UnexpectedStatus
from ..api_client.models.traffic_matching_list import TrafficMatchingList
from ..api_client.models.create_or_update_traffic_matching_list import (
    CreateOrUpdateTrafficMatchingList,
)
from ..api_client.api.traffic_matching_lists import (
    create_traffic_matching_list,
    delete_traffic_matching_list,
    get_traffic_matching_list,
    get_traffic_matching_lists,
    update_traffic_matching_list,
)

logger = logging.getLogger(__name__)


class UnifiTrafficMatchingManager:

    def __init__(self, client: Client, site_id: UUID) -> None:
        self.client = client
        self.site_id = site_id
        logger.debug(f"{self.__class__.__name__} initialized.")

    def iter_matching_lists(self, limit: int = 200) -> Iterator[TrafficMatchingList]:
        offset = 0
        while True:
            try:
                page = get_traffic_matching_lists.sync(
                    client=self.client, site_id=self.site_id, offset=offset, limit=limit
                )
                data = getattr(page, "data", None)
                if not data:
                    break
                yield from data
                if len(data) < limit:
                    break
                offset += limit
            except httpx.HTTPError as e:
                logger.error(f"Network error during retrieval at offset {offset}: {e}")
                break

    def get_list(self, matching_list_id: UUID | str) -> Optional[TrafficMatchingList]:
        target_id = UUID(str(matching_list_id))
        try:
            return get_traffic_matching_list.sync(
                client=self.client, site_id=self.site_id, traffic_matching_list_id=target_id
            )
        except httpx.HTTPError as e:
            logger.error(f"Failed to retrieve list {target_id}: {e}")
            return None

    def create_list(self, config_data: Dict[str, Any]) -> Optional[TrafficMatchingList]:
        try:
            body = CreateOrUpdateTrafficMatchingList.from_dict(config_data)
            res = create_traffic_matching_list.sync(client=self.client, site_id=self.site_id, body=body)
            logger.info(f"Successfully provisioned matching list: {config_data.get('name')}")
            return res
        except Exception as e:
            logger.error(f"Traffic matching list provisioning failed: {e}")
            return None

    def update_list(self, matching_list_id: UUID | str, config_data: Dict[str, Any]) -> Optional[TrafficMatchingList]:
        target_id = UUID(str(matching_list_id))
        try:
            body = CreateOrUpdateTrafficMatchingList.from_dict(config_data)
            return update_traffic_matching_list.sync(
                client=self.client, site_id=self.site_id, traffic_matching_list_id=target_id, body=body
            )
        except Exception as e:
            logger.error(f"Update failed for matching list {target_id}: {e}")
            return None

    def delete_list(self, matching_list_id: UUID | str) -> bool:
        target_id = UUID(str(matching_list_id))
        logger.warning(f"DELETING TRAFFIC MATCHING LIST: {target_id}")
        try:
            delete_traffic_matching_list.sync_detailed(
                client=self.client, site_id=self.site_id, traffic_matching_list_id=target_id
            )
            return True
        except httpx.HTTPError as e:
            logger.error(f"Deletion failed for {target_id}: {e}")
            return False
