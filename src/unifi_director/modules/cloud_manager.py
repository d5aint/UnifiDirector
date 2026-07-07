"""UniFi Cloud Site Manager Module — telemetry and ISP metrics via api.ui.com."""

__version__ = "1.0.0"

import logging
from typing import Any, cast

import httpx

from ..client_factory import get_cloud_client

logger = logging.getLogger(__name__)


class UnifiCloudManager:
    """Connects to Cloud Site Manager endpoints (api.ui.com), not the local proxy."""

    def __init__(self) -> None:
        self.client = get_cloud_client()
        logger.debug(f"{self.__class__.__name__} initialized.")

    def __enter__(self) -> "UnifiCloudManager":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        # WHY: Explicitly close the httpx client to release the connection pool;
        # cloud_manager is used as a context manager so cleanup is guaranteed.
        self.client.close()
        logger.debug(f"{self.__class__.__name__} resources released and closed.")

    def _handle_request(self, method: str, endpoint: str, **kwargs: Any) -> Any | None:
        path = f"/ea{endpoint}"
        try:
            response = self.client.request(method, path, **kwargs)
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After", "unknown")
                logger.error(f"Cloud API Rate Limit Exceeded. Retry after: {retry_after}s")
                return None
            response.raise_for_status()
            return response.json().get("data", [])
        except httpx.HTTPError as e:
            full_url = f"{self.client.base_url}{path.lstrip('/')}"
            logger.error(f"Cloud API request failed at {full_url}: {e}")
            return None

    def get_cloud_hosts(self) -> list[dict[str, Any]]:
        """Return all UniFi OS Consoles visible to the cloud account."""
        result = self._handle_request("GET", "/hosts")
        return result if result else []

    def get_isp_metrics(self, site_id: str | None = None) -> list[dict[str, Any]]:
        """Return 24-hour ISP metrics (latency, packet loss, throughput), optionally filtered by site."""
        params = {"duration": "24h"}
        metrics = self._handle_request("GET", "/isp-metrics/5m", params=params)
        if not metrics:
            return []
        if site_id:
            return [m for m in metrics if m.get("siteId") == str(site_id)]
        return cast(list[dict[str, Any]], metrics)
