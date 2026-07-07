"""UniFi Device Management Orchestrator."""

__version__ = "1.0.0"

import json
import logging
from typing import Any, Iterator, List, Optional
from uuid import UUID

import httpx

from ..api_client.client import Client
from ..api_client.errors import UnexpectedStatus
from ..api_client.models.integration_device_adoption_request_dto import (
    IntegrationDeviceAdoptionRequestDto,
)
from ..api_client.models.device_action_request import DeviceActionRequest
from ..api_client.models.port_action_request import PortActionRequest
from ..api_client.api.uni_fi_devices import (
    adopt_device,
    execute_adopted_device_action,
    execute_port_action,
    get_adopted_device_details,
    get_adopted_device_latest_statistics,
    get_adopted_device_overview_page,
    get_pending_device_page,
    remove_device,
)

logger = logging.getLogger(__name__)


class UnifiDeviceManager:

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

    def list_pending(self) -> List[Any]:
        try:
            res = get_pending_device_page.sync(client=self.client)
            return getattr(res, "data", []) if res else []
        except httpx.HTTPError as e:
            logger.error(f"Pending discovery failed: {e}")
            return []

    def iter_adopted(self, limit: int = 200) -> Iterator[Any]:
        return self._paginate(get_adopted_device_overview_page, site_id=self.site_id, limit=limit)

    def adopt(self, mac: str, name: Optional[str] = None) -> bool:
        logger.info(f"Initiating adoption for: {mac}")
        data: dict[str, Any] = {"macAddress": mac}
        if name:
            data["name"] = name
        try:
            adopt_device.sync_detailed(
                client=self.client,
                site_id=self.site_id,
                body=IntegrationDeviceAdoptionRequestDto.from_dict(data),
            )
            return True
        except httpx.HTTPError as e:
            logger.error(f"Adoption failed: {e}")
            return False

    def decommission(self, device_id: UUID | str) -> bool:
        target_id = UUID(str(device_id))
        # WHY: Decommission removes the device from the site and factory-resets it;
        # log at WARNING so there is always an audit trail.
        logger.warning(f"DECOMMISSIONING device: {target_id}")
        try:
            remove_device.sync_detailed(client=self.client, site_id=self.site_id, device_id=target_id)
            return True
        except httpx.HTTPError as e:
            logger.error(f"Failed to decommission device {device_id}: {e}")
            return False

    def get_stats(self, device_id: UUID | str) -> Optional[Any]:
        target_id = UUID(str(device_id))
        try:
            res = get_adopted_device_latest_statistics.sync_detailed(
                client=self.client, site_id=self.site_id, device_id=target_id
            )
            if res and res.status_code == 200:
                try:
                    return json.loads(res.content)
                except json.JSONDecodeError as je:
                    logger.error(f"API returned invalid JSON for device stats: {je}")
                    return None
            return None
        except UnexpectedStatus as e:
            # WHY: The generated client raises UnexpectedStatus on 200 when the
            # response model was partially dropped during codegen; fall back to
            # raw JSON parsing rather than losing the data entirely.
            if e.status_code == 200:
                try:
                    return json.loads(e.content)
                except json.JSONDecodeError:
                    return None
            logger.error(f"Failed to fetch stats for {target_id}: {e}")
            return None
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch stats for {target_id}: {e}")
            return None

    def get_device_details(self, device_id: UUID | str) -> Optional[Any]:
        target_id = UUID(str(device_id))
        try:
            res = get_adopted_device_details.sync_detailed(
                client=self.client, site_id=self.site_id, device_id=target_id
            )
            if res and res.status_code == 200:
                try:
                    return json.loads(res.content)
                except json.JSONDecodeError as je:
                    logger.error(f"API returned invalid JSON for device details: {je}")
                    return None
            return None
        except UnexpectedStatus as e:
            if e.status_code == 200:
                try:
                    return json.loads(e.content)
                except json.JSONDecodeError:
                    return None
            logger.error(f"Failed to fetch details for device {target_id}: {e}")
            return None
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch details for device {target_id}: {e}")
            return None

    def device_action(self, device_id: UUID | str, action: str) -> bool:
        target_id = UUID(str(device_id))
        try:
            body = DeviceActionRequest.from_dict({"action": action.upper()})
            execute_adopted_device_action.sync_detailed(
                client=self.client, site_id=self.site_id, device_id=target_id, body=body
            )
            logger.info(f"Successfully executed {action} on device {device_id}.")
            return True
        except UnexpectedStatus as e:
            try:
                err_msg = json.loads(e.content).get("message", str(e))
            except json.JSONDecodeError:
                err_msg = str(e)
            logger.error(f"API rejected device action '{action}' on {target_id}: {err_msg}")
            return False
        except httpx.HTTPError as e:
            logger.error(f"Network error executing {action} on {target_id}: {e}")
            return False

    def port_action(self, device_id: UUID | str, port_idx: int, action: str) -> bool:
        target_id = UUID(str(device_id))
        try:
            body = PortActionRequest.from_dict({"action": action.upper()})
            execute_port_action.sync_detailed(
                client=self.client, site_id=self.site_id, device_id=target_id, port_idx=port_idx, body=body
            )
            logger.info(f"Successfully executed {action} on port {port_idx}.")
            return True
        except UnexpectedStatus as e:
            try:
                err_msg = json.loads(e.content).get("message", str(e))
            except json.JSONDecodeError:
                err_msg = str(e)
            logger.error(f"API rejected port action '{action}' on port {port_idx}: {err_msg}")
            return False
        except httpx.HTTPError as e:
            logger.error(f"Port action {action} on port {port_idx} failed: {e}")
            return False
