"""UniFi Wi-Fi Broadcast Management Module."""

__version__ = "1.0.0"

import logging
from typing import Any, Dict, Iterator, Optional
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.models.wifi_broadcast_details import WifiBroadcastDetails
from ..api_client.models.wifi_broadcast_create_or_update import WifiBroadcastCreateOrUpdate
from ..api_client.api.wi_fi_broadcasts import (
    create_wifi_broadcast,
    delete_wifi_broadcast,
    get_wifi_broadcast_details,
    get_wifi_broadcast_page,
    update_wifi_broadcast,
)

logger = logging.getLogger(__name__)


class UnifiWifiManager:

    def __init__(self, client: Client, site_id: UUID) -> None:
        self.client = client
        self.site_id = site_id
        logger.debug(f"{self.__class__.__name__} initialized.")

    def iter_broadcasts(self, limit: int = 50) -> Iterator[Any]:
        offset = 0
        while True:
            try:
                page = get_wifi_broadcast_page.sync(
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
                logger.error(f"Network error during broadcast retrieval at offset {offset}: {e}")
                break

    def get_broadcast(self, broadcast_id: UUID | str) -> Optional[WifiBroadcastDetails]:
        try:
            target_id = UUID(str(broadcast_id))
        except ValueError:
            logger.error(f"Invalid input: '{broadcast_id}' is not a valid hexadecimal UUID.")
            return None
        try:
            return get_wifi_broadcast_details.sync(
                client=self.client, site_id=self.site_id, wifi_broadcast_id=target_id
            )
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch details for {target_id}: {e}")
            return None

    def provision_broadcast(self, config_data: Dict[str, Any]) -> Optional[WifiBroadcastDetails]:
        try:
            body = WifiBroadcastCreateOrUpdate.from_dict(config_data)
            res = create_wifi_broadcast.sync(client=self.client, site_id=self.site_id, body=body)
            logger.info(f"Successfully provisioned broadcast: {config_data.get('name')}")
            return res
        except Exception as e:
            logger.error(f"Provisioning failed: {e}")
            return None

    def update_broadcast(self, broadcast_id: UUID | str, config_data: Dict[str, Any]) -> Optional[WifiBroadcastDetails]:
        target_id = UUID(str(broadcast_id))
        try:
            body = WifiBroadcastCreateOrUpdate.from_dict(config_data)
            return update_wifi_broadcast.sync(
                client=self.client, site_id=self.site_id, wifi_broadcast_id=target_id, body=body
            )
        except Exception as e:
            logger.error(f"Update failed for {target_id}: {e}")
            return None

    def delete_broadcast(self, broadcast_id: UUID | str, force: bool = False) -> bool:
        target_id = UUID(str(broadcast_id))
        logger.warning(f"DELETING Wi-Fi Broadcast: {target_id} (Force: {force})")
        try:
            delete_wifi_broadcast.sync_detailed(
                client=self.client, site_id=self.site_id, wifi_broadcast_id=target_id, force=force
            )
            return True
        except httpx.HTTPError as e:
            logger.error(f"Deletion failed for {target_id}: {e}")
            return False
