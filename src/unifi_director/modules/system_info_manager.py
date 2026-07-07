"""UniFi System Information Management Module."""

__version__ = "1.0.0"

import logging
from typing import Optional

import httpx

from ..api_client.client import Client
from ..api_client.models.application_info import ApplicationInfo
from ..api_client.api.application_info import get_info

logger = logging.getLogger(__name__)


class UnifiInfoManager:

    def __init__(self, client: Client) -> None:
        self.client = client
        logger.debug(f"{self.__class__.__name__} initialized.")

    def get_system_info(self) -> Optional[ApplicationInfo]:
        try:
            response = get_info.sync(client=self.client)
            if response:
                app_version = getattr(response, "application_version", "Unknown")
                logger.debug(f"Successfully retrieved info for version: {app_version}")
                return response
            logger.error("API returned an empty response for system info.")
            return None
        except httpx.HTTPError as e:
            logger.error(f"Network error during system info retrieval: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return None
