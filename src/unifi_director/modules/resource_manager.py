"""UniFi Supporting Resources Management Module (read-only global resources)."""

__version__ = "1.0.0"

import logging
from typing import Any, Iterator, List
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.errors import UnexpectedStatus
from ..api_client.api.supporting_resources import (
    get_countries,
    get_device_tag_page,
    get_dpi_application_categories,
    get_dpi_applications,
    get_radius_profile_overview_page,
    get_site_to_site_vpn_tunnel_page,
    get_vpn_server_page,
    get_wans_overview_page,
)

logger = logging.getLogger(__name__)


class UnifiResourceManager:

    def __init__(self, client: Client, site_id: UUID) -> None:
        self.client = client
        self.site_id = site_id
        logger.debug(f"{self.__class__.__name__} initialized.")

    def _paginate(self, api_func: Any, **kwargs: Any) -> Iterator[Any]:
        offset = 0
        limit = kwargs.pop("limit", 200)
        while True:
            try:
                page = api_func.sync(client=self.client, offset=offset, limit=limit, **kwargs)
                data = getattr(page, "data", None)
                if not data:
                    break
                yield from data
                if len(data) < limit:
                    break
                offset += limit
            except (httpx.HTTPError, UnexpectedStatus) as e:
                logger.error(f"Network error in {api_func.__name__} at offset {offset}: {e}")
                break

    def list_countries(self, limit: int = 200) -> Iterator[Any]:
        return self._paginate(get_countries, limit=limit)

    def list_wans(self, limit: int = 200) -> List[Any]:
        try:
            res = get_wans_overview_page.sync(client=self.client, site_id=self.site_id, limit=limit)
            return getattr(res, "data", []) if res else []
        except (httpx.HTTPError, UnexpectedStatus) as e:
            logger.error(f"Failed to fetch WANs: {e}")
            return []

    def iter_device_tags(self, limit: int = 200) -> Iterator[Any]:
        return self._paginate(get_device_tag_page, site_id=self.site_id, limit=limit)

    def iter_dpi_apps(self, limit: int = 200) -> Iterator[Any]:
        return self._paginate(get_dpi_applications, limit=limit)

    def list_dpi_categories(self) -> List[Any]:
        try:
            res = get_dpi_application_categories.sync(client=self.client)
            return getattr(res, "data", []) if res else []
        except (httpx.HTTPError, UnexpectedStatus) as e:
            logger.error(f"Failed to fetch DPI categories: {e}")
            return []

    def iter_radius_profiles(self, limit: int = 200) -> Iterator[Any]:
        return self._paginate(get_radius_profile_overview_page, site_id=self.site_id, limit=limit)

    def iter_vpn_tunnels(self, limit: int = 200) -> Iterator[Any]:
        return self._paginate(get_site_to_site_vpn_tunnel_page, site_id=self.site_id, limit=limit)

    def iter_vpn_servers(self, limit: int = 200) -> Iterator[Any]:
        return self._paginate(get_vpn_server_page, site_id=self.site_id, limit=limit)
