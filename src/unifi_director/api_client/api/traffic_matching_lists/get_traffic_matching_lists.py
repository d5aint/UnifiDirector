from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.traffic_matching_lists_page import TrafficMatchingListsPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_id: UUID,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sites/{site_id}/traffic-matching-lists".format(
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TrafficMatchingListsPage | None:
    if response.status_code == 200:
        response_200 = TrafficMatchingListsPage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TrafficMatchingListsPage]:
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
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> Response[TrafficMatchingListsPage]:
    """List Traffic Matching Lists

     Retrieve all traffic matching lists on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    </details>

    Args:
        site_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrafficMatchingListsPage]
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
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> TrafficMatchingListsPage | None:
    """List Traffic Matching Lists

     Retrieve all traffic matching lists on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    </details>

    Args:
        site_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrafficMatchingListsPage
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
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> Response[TrafficMatchingListsPage]:
    """List Traffic Matching Lists

     Retrieve all traffic matching lists on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    </details>

    Args:
        site_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrafficMatchingListsPage]
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
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> TrafficMatchingListsPage | None:
    """List Traffic Matching Lists

     Retrieve all traffic matching lists on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    </details>

    Args:
        site_id (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrafficMatchingListsPage
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
