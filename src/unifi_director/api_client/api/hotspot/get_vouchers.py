from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hotspot_voucher_detail_page import HotspotVoucherDetailPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_id: UUID,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sites/{site_id}/hotspot/vouchers".format(
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HotspotVoucherDetailPage | None:
    if response.status_code == 200:
        response_200 = HotspotVoucherDetailPage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HotspotVoucherDetailPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
) -> Response[HotspotVoucherDetailPage]:
    """List Vouchers

     Retrieve a paginated list of Hotspot vouchers.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`createdAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`code`|`STRING`|`eq` `ne` `in` `notIn`|
    |`authorizedGuestLimit`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`authorizedGuestCount`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`activatedAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`expiresAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`expired`|`BOOLEAN`|`eq` `ne`|
    |`timeLimitMinutes`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`dataUsageLimitMBytes`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`rxRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`txRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    </details>

    Args:
        site_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HotspotVoucherDetailPage]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        offset=offset,
        limit=limit,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
) -> HotspotVoucherDetailPage | None:
    """List Vouchers

     Retrieve a paginated list of Hotspot vouchers.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`createdAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`code`|`STRING`|`eq` `ne` `in` `notIn`|
    |`authorizedGuestLimit`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`authorizedGuestCount`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`activatedAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`expiresAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`expired`|`BOOLEAN`|`eq` `ne`|
    |`timeLimitMinutes`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`dataUsageLimitMBytes`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`rxRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`txRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    </details>

    Args:
        site_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HotspotVoucherDetailPage
    """

    return sync_detailed(
        site_id=site_id,
        client=client,
        offset=offset,
        limit=limit,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
) -> Response[HotspotVoucherDetailPage]:
    """List Vouchers

     Retrieve a paginated list of Hotspot vouchers.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`createdAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`code`|`STRING`|`eq` `ne` `in` `notIn`|
    |`authorizedGuestLimit`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`authorizedGuestCount`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`activatedAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`expiresAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`expired`|`BOOLEAN`|`eq` `ne`|
    |`timeLimitMinutes`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`dataUsageLimitMBytes`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`rxRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`txRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    </details>

    Args:
        site_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HotspotVoucherDetailPage]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        offset=offset,
        limit=limit,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
) -> HotspotVoucherDetailPage | None:
    """List Vouchers

     Retrieve a paginated list of Hotspot vouchers.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`createdAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`code`|`STRING`|`eq` `ne` `in` `notIn`|
    |`authorizedGuestLimit`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`authorizedGuestCount`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`activatedAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`expiresAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`expired`|`BOOLEAN`|`eq` `ne`|
    |`timeLimitMinutes`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
    |`dataUsageLimitMBytes`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`rxRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    |`txRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
    </details>

    Args:
        site_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HotspotVoucherDetailPage
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            client=client,
            offset=offset,
            limit=limit,
            filter_=filter_,
        )
    ).parsed
