"""UniFi Connected Client Management Module."""

__version__ = "1.0.0"

import logging
from typing import Any, Iterator, Optional
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.models.client_details import ClientDetails
from ..api_client.models.client_action_request import ClientActionRequest
from ..api_client.api.clients import (
    execute_connected_client_action,
    get_connected_client_details,
    get_connected_client_overview_page,
)

logger = logging.getLogger(__name__)

_ALLOWED_ACTIONS = frozenset({"RECONNECT", "BLOCK", "UNBLOCK", "AUTHORIZE", "UNAUTHORIZE"})


class UnifiClientManager:

    def __init__(self, client: Client, site_id: UUID) -> None:
        self.client = client
        self.site_id = site_id
        logger.debug(f"{self.__class__.__name__} initialized.")

    def iter_clients(self, limit: int = 200) -> Iterator[Any]:
        offset = 0
        while True:
            try:
                page = get_connected_client_overview_page.sync(
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
                logger.error(f"Failed to fetch client page at offset {offset}: {e}")
                break

    def get_client(self, client_id: str) -> Optional[ClientDetails]:
        try:
            return get_connected_client_details.sync(
                client=self.client, site_id=self.site_id, client_id=UUID(str(client_id))
            )
        except ValueError:
            logger.error(f"Invalid UUID format provided for client: {client_id}")
            return None
        except httpx.HTTPError as e:
            logger.error(f"Error fetching details for client {client_id}: {e}")
            return None

    def trigger_action(self, client_id: str, action_type: str) -> bool:
        action_type = action_type.upper()

        if action_type not in _ALLOWED_ACTIONS:
            logger.error(f"Action '{action_type}' is not in the allowed whitelist: {_ALLOWED_ACTIONS}")
            return False

        if action_type == "BLOCK":
            # WHY: Warn on BLOCK specifically — it drops all traffic for the client
            # immediately and can be hard to diagnose if triggered accidentally.
            logger.warning(f"BLOCK action requested for {client_id}. This will drop traffic.")

        try:
            body = ClientActionRequest.from_dict({"action": action_type})
            execute_connected_client_action.sync(
                client=self.client, site_id=self.site_id, client_id=UUID(str(client_id)), body=body
            )
            logger.info(f"Action {action_type} sent successfully to {client_id}")
            return True
        except ValueError:
            logger.error(f"Invalid UUID format provided for client: {client_id}")
            return False
        except httpx.HTTPError as e:
            logger.error(f"Failed to execute {action_type} on {client_id}: {e}")
            return False
