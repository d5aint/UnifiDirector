"""UniFi DNS Policy Management Module."""

__version__ = "1.0.0"

import logging
from typing import Any, Iterator, Optional
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.errors import UnexpectedStatus
from ..api_client.models.dns_policy import DNSPolicy
from ..api_client.models.create_or_update_dns_policy import CreateOrUpdateDNSPolicy
from ..api_client.api.dns_policies import (
    create_dns_policy,
    delete_dns_policy,
    get_dns_policy,
    get_dns_policy_page,
    update_dns_policy,
)

logger = logging.getLogger(__name__)


class UnifiDnsManager:

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

    def list_policies(self, limit: int = 200) -> Iterator[DNSPolicy]:
        return self._paginate(get_dns_policy_page, site_id=self.site_id, limit=limit)

    def get_policy(self, dns_policy_id: UUID | str) -> Optional[DNSPolicy]:
        target_id = UUID(str(dns_policy_id))
        try:
            return get_dns_policy.sync(client=self.client, site_id=self.site_id, dns_policy_id=target_id)
        except httpx.HTTPError as e:
            logger.error(f"Failed to retrieve DNS policy {target_id}: {e}")
            return None

    def create_policy(self, data: dict) -> Optional[DNSPolicy]:
        try:
            body = CreateOrUpdateDNSPolicy.from_dict(data)
            return create_dns_policy.sync(client=self.client, site_id=self.site_id, body=body)
        except Exception as e:
            logger.error(f"DNS Policy creation failed: {e}")
            return None

    def update_policy(self, dns_policy_id: UUID | str, data: dict) -> Optional[DNSPolicy]:
        target_id = UUID(str(dns_policy_id))
        try:
            body = CreateOrUpdateDNSPolicy.from_dict(data)
            return update_dns_policy.sync(client=self.client, site_id=self.site_id, dns_policy_id=target_id, body=body)
        except Exception as e:
            logger.error(f"Update failed for DNS policy {target_id}: {e}")
            return None

    def delete_policy(self, dns_policy_id: UUID | str) -> bool:
        target_id = UUID(str(dns_policy_id))
        try:
            delete_dns_policy.sync_detailed(client=self.client, site_id=self.site_id, dns_policy_id=target_id)
            logger.info(f"Successfully deleted DNS policy: {target_id}")
            return True
        except httpx.HTTPError as e:
            logger.error(f"Deletion failed for DNS policy {target_id}: {e}")
            return False
