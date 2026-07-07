from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.voucher_deletion_results import VoucherDeletionResults
from ...types import UNSET, Response


def _get_kwargs(
    site_id: UUID,
    *,
    filter_: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/sites/{site_id}/hotspot/vouchers".format(
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> VoucherDeletionResults | None:
    if response.status_code == 200:
        response_200 = VoucherDeletionResults.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[VoucherDeletionResults]:
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
    filter_: str,
) -> Response[VoucherDeletionResults]:
    """Delete Vouchers

     Remove Hotspot vouchers based on the specified filter criteria.

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
        filter_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VoucherDeletionResults]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
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
    filter_: str,
) -> VoucherDeletionResults | None:
    """Delete Vouchers

     Remove Hotspot vouchers based on the specified filter criteria.

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
        filter_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VoucherDeletionResults
    """

    return sync_detailed(
        site_id=site_id,
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    filter_: str,
) -> Response[VoucherDeletionResults]:
    """Delete Vouchers

     Remove Hotspot vouchers based on the specified filter criteria.

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
        filter_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VoucherDeletionResults]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    filter_: str,
) -> VoucherDeletionResults | None:
    """Delete Vouchers

     Remove Hotspot vouchers based on the specified filter criteria.

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
        filter_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VoucherDeletionResults
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            client=client,
            filter_=filter_,
        )
    ).parsed
