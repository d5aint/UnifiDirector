"""UniFi Site Management Module."""

__version__ = "1.0.0"

import logging
from typing import Any, Iterator

import httpx

from ..api_client.client import Client
from ..api_client.api.sites import get_site_overview_page

logger = logging.getLogger(__name__)


class UnifiSiteManager:

    def __init__(self, client: Client) -> None:
        self.client = client
        logger.debug(f"{self.__class__.__name__} initialized.")

    def iter_sites(self, limit: int = 200) -> Iterator[Any]:
        offset = 0
        while True:
            try:
                page = get_site_overview_page.sync(client=self.client, offset=offset, limit=limit)
                data = getattr(page, "data", None)
                if not data:
                    break
                yield from data
                if len(data) < limit:
                    break
                offset += limit
            except httpx.HTTPError as e:
                logger.error(f"Network error during site retrieval at offset {offset}: {e}")
                break
