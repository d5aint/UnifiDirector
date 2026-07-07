from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dpi_category_page import DPICategoryPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/v1/dpi/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DPICategoryPage | None:
    if response.status_code == 200:
        response_200 = DPICategoryPage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DPICategoryPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> Response[DPICategoryPage]:
    """List DPI Application Categories

     Returns predefined Deep Packet Inspection (DPI) application categories used for traffic
    identification and filtering.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`INTEGER`|`eq` `ne` `in` `notIn`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    </details>

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DPICategoryPage]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> DPICategoryPage | None:
    """List DPI Application Categories

     Returns predefined Deep Packet Inspection (DPI) application categories used for traffic
    identification and filtering.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`INTEGER`|`eq` `ne` `in` `notIn`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    </details>

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DPICategoryPage
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> Response[DPICategoryPage]:
    """List DPI Application Categories

     Returns predefined Deep Packet Inspection (DPI) application categories used for traffic
    identification and filtering.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`INTEGER`|`eq` `ne` `in` `notIn`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    </details>

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DPICategoryPage]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 25,
    filter_: str | Unset = UNSET,
) -> DPICategoryPage | None:
    """List DPI Application Categories

     Returns predefined Deep Packet Inspection (DPI) application categories used for traffic
    identification and filtering.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`id`|`INTEGER`|`eq` `ne` `in` `notIn`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    </details>

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 25.
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DPICategoryPage
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            filter_=filter_,
        )
    ).parsed
