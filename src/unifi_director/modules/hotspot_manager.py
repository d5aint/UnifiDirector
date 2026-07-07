"""UniFi Hotspot Voucher Management Module."""

__version__ = "1.0.0"

import logging
from uuid import UUID

import httpx

from ..api_client.api.hotspot import (
    create_vouchers,
    delete_voucher,
    delete_vouchers,
    get_voucher,
    get_vouchers,
)
from ..api_client.client import Client
from ..api_client.models.hotspot_voucher_creation_request import (
    HotspotVoucherCreationRequest,
)
from ..api_client.types import UNSET
from ..registry import REGISTRY

logger = logging.getLogger(__name__)


class UnifiHotspotManager:

    def __init__(self, client: Client) -> None:
        self.client = client

    def list_vouchers(self, limit: int = 100, filter_: str | None = None):
        try:
            response = get_vouchers.sync(
                site_id=REGISTRY.SITE_ID,
                limit=limit,
                client=self.client,
                filter_=filter_ if filter_ is not None else UNSET,
            )
            if response:
                return getattr(response, "data", [])
            return []
        except httpx.HTTPError as e:
            logger.error(f"Network error listing vouchers: {e}")
            return []
        except Exception as e:
            logger.error(f"Error listing vouchers: {e}")
            return []

    def get_voucher(self, voucher_id: UUID):
        try:
            return get_voucher.sync(site_id=REGISTRY.SITE_ID, voucher_id=voucher_id, client=self.client)
        except httpx.HTTPError as e:
            logger.error(f"Network error getting voucher: {e}")
            return None
        except Exception as e:
            logger.error(f"Error getting voucher: {e}")
            return None

    def create_vouchers(
        self,
        name: str,
        time_limit_minutes: int,
        count: int = 1,
        authorized_guest_limit: int | None = None,
        data_usage_limit_mbytes: int | None = None,
        rx_rate_limit_kbps: int | None = None,
        tx_rate_limit_kbps: int | None = None,
    ):
        try:
            body = HotspotVoucherCreationRequest(
                name=name,
                time_limit_minutes=time_limit_minutes,
                count=count,
                authorized_guest_limit=authorized_guest_limit if authorized_guest_limit is not None else UNSET,
                data_usage_limit_m_bytes=data_usage_limit_mbytes if data_usage_limit_mbytes is not None else UNSET,
                rx_rate_limit_kbps=rx_rate_limit_kbps if rx_rate_limit_kbps is not None else UNSET,
                tx_rate_limit_kbps=tx_rate_limit_kbps if tx_rate_limit_kbps is not None else UNSET,
            )
            return create_vouchers.sync(site_id=REGISTRY.SITE_ID, body=body, client=self.client)
        except httpx.HTTPError as e:
            logger.error(f"Network error creating vouchers: {e}")
            return None
        except Exception as e:
            logger.error(f"Error creating vouchers: {e}")
            return None

    def delete_voucher(self, voucher_id: UUID):
        try:
            return delete_voucher.sync(site_id=REGISTRY.SITE_ID, voucher_id=voucher_id, client=self.client)
        except httpx.HTTPError as e:
            logger.error(f"Network error deleting voucher: {e}")
            return None
        except Exception as e:
            logger.error(f"Error deleting voucher: {e}")
            return None

    def delete_vouchers(self, filter_: str):
        # WHY: Bulk delete requires an explicit filter string to prevent accidental
        # deletion of all vouchers. The caller must pass a non-empty filter.
        try:
            return delete_vouchers.sync(site_id=REGISTRY.SITE_ID, filter_=filter_, client=self.client)
        except httpx.HTTPError as e:
            logger.error(f"Network error bulk-deleting vouchers: {e}")
            return None
        except Exception as e:
            logger.error(f"Error bulk-deleting vouchers: {e}")
            return None
