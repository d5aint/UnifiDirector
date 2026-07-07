from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.integration_dns_policy_page_dto import IntegrationDnsPolicyPageDto
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
        "url": "/v1/sites/{site_id}/dns/policies".format(
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IntegrationDnsPolicyPageDto | None:
    if response.status_code == 200:
        response_200 = IntegrationDnsPolicyPageDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IntegrationDnsPolicyPageDto]:
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
) -> Response[IntegrationDnsPolicyPageDto]:
    """List DNS Policies

     Retrieve a paginated list of all DNS policies on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`type`|`STRING`|`eq` `ne` `in` `notIn`|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`enabled`|`BOOLEAN`|`eq` `ne`|
    |`domain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipv4Address`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipv6Address`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`targetDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`mailServerDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`text`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`serverDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipAddress`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ttlSeconds`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`priority`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`service`|`STRING`|`eq` `ne` `in` `notIn`|
    |`protocol`|`STRING`|`eq` `ne` `in` `notIn`|
    |`port`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`weight`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
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
        Response[IntegrationDnsPolicyPageDto]
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
) -> IntegrationDnsPolicyPageDto | None:
    """List DNS Policies

     Retrieve a paginated list of all DNS policies on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`type`|`STRING`|`eq` `ne` `in` `notIn`|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`enabled`|`BOOLEAN`|`eq` `ne`|
    |`domain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipv4Address`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipv6Address`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`targetDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`mailServerDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`text`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`serverDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipAddress`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ttlSeconds`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`priority`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`service`|`STRING`|`eq` `ne` `in` `notIn`|
    |`protocol`|`STRING`|`eq` `ne` `in` `notIn`|
    |`port`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`weight`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
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
        IntegrationDnsPolicyPageDto
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
) -> Response[IntegrationDnsPolicyPageDto]:
    """List DNS Policies

     Retrieve a paginated list of all DNS policies on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`type`|`STRING`|`eq` `ne` `in` `notIn`|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`enabled`|`BOOLEAN`|`eq` `ne`|
    |`domain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipv4Address`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipv6Address`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`targetDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`mailServerDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`text`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`serverDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipAddress`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ttlSeconds`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`priority`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`service`|`STRING`|`eq` `ne` `in` `notIn`|
    |`protocol`|`STRING`|`eq` `ne` `in` `notIn`|
    |`port`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`weight`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
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
        Response[IntegrationDnsPolicyPageDto]
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
) -> IntegrationDnsPolicyPageDto | None:
    """List DNS Policies

     Retrieve a paginated list of all DNS policies on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`type`|`STRING`|`eq` `ne` `in` `notIn`|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`enabled`|`BOOLEAN`|`eq` `ne`|
    |`domain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipv4Address`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipv6Address`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`targetDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`mailServerDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`text`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`serverDomain`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ipAddress`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`ttlSeconds`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`priority`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`service`|`STRING`|`eq` `ne` `in` `notIn`|
    |`protocol`|`STRING`|`eq` `ne` `in` `notIn`|
    |`port`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`weight`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
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
        IntegrationDnsPolicyPageDto
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
