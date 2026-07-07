"""UniFi Firewall & Zone Management Module."""

__version__ = "1.0.0"

import logging
from typing import Any, Iterator, List, Optional, Dict
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.errors import UnexpectedStatus
from ..api_client.models.firewall_policy import FirewallPolicy
from ..api_client.models.firewall_zone import FirewallZone
from ..api_client.models.patch_firewall_policy import PatchFirewallPolicy
from ..api_client.models.create_or_update_firewall_zone import CreateOrUpdateFirewallZone
from ..api_client.models.create_or_update_firewall_policy import CreateOrUpdateFirewallPolicy
from ..api_client.models.integration_firewall_policy_ordering_dto import (
    IntegrationFirewallPolicyOrderingDto,
)
from ..api_client.api.firewall import (
    create_firewall_policy,
    create_firewall_zone,
    delete_firewall_policy,
    delete_firewall_zone,
    get_firewall_policies,
    get_firewall_policy,
    get_firewall_policy_ordering,
    get_firewall_zone,
    get_firewall_zones,
    patch_firewall_policy,
    update_firewall_policy,
    update_firewall_policy_ordering,
    update_firewall_zone,
)

logger = logging.getLogger(__name__)


class UnifiFirewallManager:

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

    def list_zones(self, limit: int = 200, exclude_system: bool = True) -> List[Any]:
        try:
            res = get_firewall_zones.sync(client=self.client, site_id=self.site_id, limit=limit)
            zones = getattr(res, "data", []) if res else []
            if exclude_system:
                zones = [z for z in zones if "system" not in getattr(z.metadata, "origin", "user").lower()]
            return zones
        except UnexpectedStatus as e:
            if e.status_code == 400:
                # WHY: A 400 here means Zone-Based Firewall is not activated on this
                # console; treat as empty rather than an error so audit commands don't abort.
                logger.warning("Zone-Based Firewall is not configured on this console. Skipping zones.")
                return []
            logger.error(f"Zone retrieval error: {e}")
            return []
        except httpx.HTTPError as e:
            logger.error(f"Zone retrieval error: {e}")
            return []

    def get_zone(self, zone_id: UUID | str) -> Optional[FirewallZone]:
        target_id = UUID(str(zone_id))
        try:
            return get_firewall_zone.sync(client=self.client, site_id=self.site_id, firewall_zone_id=target_id)
        except httpx.HTTPError as e:
            logger.error(f"Failed to retrieve zone {target_id}: {e}")
            return None

    def create_zone(self, name: str, network_ids: List[str]) -> Optional[Any]:
        try:
            body = CreateOrUpdateFirewallZone.from_dict({"name": name, "networkIds": network_ids})
            return create_firewall_zone.sync(client=self.client, site_id=self.site_id, body=body)
        except Exception as e:
            logger.error(f"Failed to create zone '{name}': {e}")
            return None

    def update_zone(self, zone_id: UUID | str, name: str, network_ids: List[str]) -> Optional[FirewallZone]:
        target_id = UUID(str(zone_id))
        try:
            body = CreateOrUpdateFirewallZone.from_dict({"name": name, "networkIds": network_ids})
            return update_firewall_zone.sync(
                client=self.client, site_id=self.site_id, firewall_zone_id=target_id, body=body
            )
        except Exception as e:
            logger.error(f"Failed to update zone {target_id}: {e}")
            return None

    def delete_zone(self, zone_id: UUID | str) -> bool:
        target_id = UUID(str(zone_id))
        logger.warning(f"DELETING firewall zone: {target_id}")
        try:
            delete_firewall_zone.sync_detailed(client=self.client, site_id=self.site_id, firewall_zone_id=target_id)
            return True
        except httpx.HTTPError as e:
            logger.error(f"Failed to delete zone {target_id}: {e}")
            return False

    def list_policies(self, limit: int = 200, exclude_system: bool = True) -> List[FirewallPolicy]:
        try:
            res = get_firewall_policies.sync(client=self.client, site_id=self.site_id, limit=limit)
            policies = getattr(res, "data", []) if res else []
            if exclude_system:
                policies = [p for p in policies if "system" not in getattr(p.metadata, "origin", "user").lower()]
            return policies
        except UnexpectedStatus as e:
            if e.status_code == 400:
                logger.warning("Zone-Based Firewall is not configured on this console. Skipping policies.")
                return []
            logger.error(f"Policy retrieval error: {e}")
            return []
        except httpx.HTTPError as e:
            logger.error(f"Policy retrieval error: {e}")
            return []

    def get_policy(self, policy_id: UUID | str) -> Optional[FirewallPolicy]:
        try:
            return get_firewall_policy.sync(
                client=self.client, site_id=self.site_id, firewall_policy_id=UUID(str(policy_id))
            )
        except httpx.HTTPError as e:
            logger.error(f"Failed to retrieve policy {policy_id}: {e}")
            return None

    def create_policy(self, config_data: Dict[str, Any]) -> Optional[FirewallPolicy]:
        try:
            body = CreateOrUpdateFirewallPolicy.from_dict(config_data)
            return create_firewall_policy.sync(client=self.client, site_id=self.site_id, body=body)
        except Exception as e:
            logger.error(f"Failed to create policy: {e}")
            return None

    def update_policy(self, policy_id: UUID | str, config_data: Dict[str, Any]) -> Optional[FirewallPolicy]:
        target_id = UUID(str(policy_id))
        try:
            body = CreateOrUpdateFirewallPolicy.from_dict(config_data)
            return update_firewall_policy.sync(
                client=self.client, site_id=self.site_id, firewall_policy_id=target_id, body=body
            )
        except Exception as e:
            logger.error(f"Failed to update policy {target_id}: {e}")
            return None

    def delete_policy(self, policy_id: UUID | str) -> bool:
        target_id = UUID(str(policy_id))
        logger.warning(f"DELETING firewall policy: {target_id}")
        try:
            delete_firewall_policy.sync_detailed(client=self.client, site_id=self.site_id, firewall_policy_id=target_id)
            return True
        except httpx.HTTPError as e:
            logger.error(f"Failed to delete policy {target_id}: {e}")
            return False

    def toggle_policy(self, policy_id: UUID | str, enabled: bool) -> bool:
        target_id = UUID(str(policy_id))
        try:
            patch_firewall_policy.sync(
                client=self.client,
                site_id=self.site_id,
                firewall_policy_id=target_id,
                body=PatchFirewallPolicy.from_dict({"enabled": enabled}),
            )
            return True
        except httpx.HTTPError:
            return False

    def get_current_order(self, source_zone_id: UUID | str, dest_zone_id: UUID | str) -> List[str]:
        try:
            res = get_firewall_policy_ordering.sync(
                client=self.client,
                site_id=self.site_id,
                source_firewall_zone_id=UUID(str(source_zone_id)),
                destination_firewall_zone_id=UUID(str(dest_zone_id)),
            )
            return (
                getattr(getattr(res, "ordered_firewall_policy_ids", None), "before_system_defined", []) if res else []
            )
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch policy order: {e}")
            return []

    def set_rule_order(
        self, source_zone_id: UUID | str, dest_zone_id: UUID | str, ordered_ids: List[str]
    ) -> bool:
        try:
            body = IntegrationFirewallPolicyOrderingDto.from_dict(
                {"orderedFirewallPolicyIds": {"beforeSystemDefined": ordered_ids, "afterSystemDefined": []}}
            )
            update_firewall_policy_ordering.sync(
                client=self.client,
                site_id=self.site_id,
                source_firewall_zone_id=UUID(str(source_zone_id)),
                destination_firewall_zone_id=UUID(str(dest_zone_id)),
                body=body,
            )
            logger.info("Firewall reordering successful.")
            return True
        except httpx.HTTPError as e:
            logger.error(f"Critical error reordering firewall: {e}")
            return False
