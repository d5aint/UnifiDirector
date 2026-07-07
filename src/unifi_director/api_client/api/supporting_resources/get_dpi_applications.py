from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dpi_application_page import DPIApplicationPage
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
        "url": "/v1/dpi/applications",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DPIApplicationPage | None:
    if response.status_code == 200:
        response_200 = DPIApplicationPage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DPIApplicationPage]:
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
) -> Response[DPIApplicationPage]:
    """List DPI Applications

     Lists DPI-recognized applications grouped under categories. Useful for firewall or traffic analytics
    integration.

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
        Response[DPIApplicationPage]
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
) -> DPIApplicationPage | None:
    """List DPI Applications

     Lists DPI-recognized applications grouped under categories. Useful for firewall or traffic analytics
    integration.

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
        DPIApplicationPage
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
) -> Response[DPIApplicationPage]:
    """List DPI Applications

     Lists DPI-recognized applications grouped under categories. Useful for firewall or traffic analytics
    integration.

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
        Response[DPIApplicationPage]
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
) -> DPIApplicationPage | None:
    """List DPI Applications

     Lists DPI-recognized applications grouped under categories. Useful for firewall or traffic analytics
    integration.

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
        DPIApplicationPage
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            filter_=filter_,
        )
    ).parsed
