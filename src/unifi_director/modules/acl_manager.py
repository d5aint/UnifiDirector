"""UniFi Access Control List (ACL) Management Module."""

__version__ = "1.0.0"

import logging
from typing import Any, Iterator, List, Optional, Dict
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.errors import UnexpectedStatus
from ..api_client.models.acl_rule import ACLRule
from ..api_client.models.acl_rule_update import ACLRuleUpdate
from ..api_client.models.acl_rule_ordering import ACLRuleOrdering
from ..api_client.api.access_control_acl_rules import (
    create_acl_rule,
    delete_acl_rule,
    get_acl_rule,
    get_acl_rule_ordering,
    get_acl_rule_page,
    update_acl_rule,
    update_acl_rule_ordering,
)

logger = logging.getLogger(__name__)


class UnifiAclManager:

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

    def iter_rules(self, limit: int = 200) -> Iterator[ACLRule]:
        return self._paginate(get_acl_rule_page, site_id=self.site_id, limit=limit)

    def get_rule(self, acl_rule_id: UUID | str) -> Optional[ACLRule]:
        target_id = UUID(str(acl_rule_id))
        try:
            return get_acl_rule.sync(client=self.client, site_id=self.site_id, acl_rule_id=target_id)
        except httpx.HTTPError as e:
            logger.error(f"Failed to retrieve ACL rule {target_id}: {e}")
            return None

    def create_rule(self, rule_data: Dict[str, Any]) -> Optional[ACLRule]:
        try:
            body = ACLRuleUpdate.from_dict(rule_data)
            res = create_acl_rule.sync(client=self.client, site_id=self.site_id, body=body)
            logger.info(f"Successfully provisioned ACL rule: {rule_data.get('name')}")
            return res
        except Exception as e:
            logger.error(f"ACL Provisioning failed: {e}")
            return None

    def update_rule(self, acl_rule_id: UUID | str, rule_data: Dict[str, Any]) -> Optional[ACLRule]:
        target_id = UUID(str(acl_rule_id))
        try:
            body = ACLRuleUpdate.from_dict(rule_data)
            return update_acl_rule.sync(client=self.client, site_id=self.site_id, acl_rule_id=target_id, body=body)
        except Exception as e:
            logger.error(f"Update failed for ACL rule {target_id}: {e}")
            return None

    def delete_rule(self, acl_rule_id: UUID | str) -> bool:
        target_id = UUID(str(acl_rule_id))
        # WHY: Log deletions at WARNING so operators always have an audit trail even
        # without --debug; ACL deletions can affect production traffic immediately.
        logger.warning(f"DELETING ACL RULE: {target_id}")
        try:
            delete_acl_rule.sync_detailed(client=self.client, site_id=self.site_id, acl_rule_id=target_id)
            return True
        except httpx.HTTPError as e:
            logger.error(f"Deletion failed for {target_id}: {e}")
            return False

    def get_order(self) -> List[UUID]:
        try:
            res = get_acl_rule_ordering.sync(client=self.client, site_id=self.site_id)
            return getattr(res, "acl_rule_ids", [])
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch ACL ordering: {e}")
            return []

    def set_order(self, ordered_ids: List[str]) -> bool:
        try:
            body = ACLRuleOrdering.from_dict({"aclRuleIds": ordered_ids})
            update_acl_rule_ordering.sync(client=self.client, site_id=self.site_id, body=body)
            logger.info("ACL rule reordering committed to site.")
            return True
        except httpx.HTTPError as e:
            logger.error(f"Critical error committing ACL order: {e}")
            return False
