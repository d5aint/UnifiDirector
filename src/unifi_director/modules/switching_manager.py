"""UniFi Switching Management Module — LAGs, MC-LAG domains, switch stacks (read-only)."""

__version__ = "1.0.0"

import logging
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.api.switching import (
    get_lag,
    get_lag_page,
    get_mc_lag_domain,
    get_mc_lag_domain_page,
    get_switch_stack,
    get_switch_stack_page,
)
from ..registry import REGISTRY

logger = logging.getLogger(__name__)


class UnifiSwitchingManager:

    def __init__(self, client: Client) -> None:
        self.client = client

    def list_lags(self, limit: int = 25):
        try:
            response = get_lag_page.sync(site_id=REGISTRY.SITE_ID, limit=limit, client=self.client)
            return getattr(response, "data", []) if response else []
        except httpx.HTTPError as e:
            logger.error(f"Network error listing LAGs: {e}")
            return []
        except Exception as e:
            logger.error(f"Error listing LAGs: {e}")
            return []

    def get_lag(self, lag_id: UUID):
        try:
            return get_lag.sync(site_id=REGISTRY.SITE_ID, lag_id=lag_id, client=self.client)
        except httpx.HTTPError as e:
            logger.error(f"Network error getting LAG: {e}")
            return None
        except Exception as e:
            logger.error(f"Error getting LAG: {e}")
            return None

    def list_stacks(self, limit: int = 25):
        try:
            response = get_switch_stack_page.sync(site_id=REGISTRY.SITE_ID, limit=limit, client=self.client)
            return getattr(response, "data", []) if response else []
        except httpx.HTTPError as e:
            logger.error(f"Network error listing switch stacks: {e}")
            return []
        except Exception as e:
            logger.error(f"Error listing switch stacks: {e}")
            return []

    def get_stack(self, stack_id: UUID):
        try:
            return get_switch_stack.sync(site_id=REGISTRY.SITE_ID, switch_stack_id=stack_id, client=self.client)
        except httpx.HTTPError as e:
            logger.error(f"Network error getting switch stack: {e}")
            return None
        except Exception as e:
            logger.error(f"Error getting switch stack: {e}")
            return None

    def list_mc_lag_domains(self, limit: int = 25):
        try:
            response = get_mc_lag_domain_page.sync(site_id=REGISTRY.SITE_ID, limit=limit, client=self.client)
            return getattr(response, "data", []) if response else []
        except httpx.HTTPError as e:
            logger.error(f"Network error listing MC-LAG domains: {e}")
            return []
        except Exception as e:
            logger.error(f"Error listing MC-LAG domains: {e}")
            return []

    def get_mc_lag_domain(self, domain_id: UUID):
        try:
            return get_mc_lag_domain.sync(
                site_id=REGISTRY.SITE_ID, mc_lag_domain_id=domain_id, client=self.client
            )
        except httpx.HTTPError as e:
            logger.error(f"Network error getting MC-LAG domain: {e}")
            return None
        except Exception as e:
            logger.error(f"Error getting MC-LAG domain: {e}")
            return None
