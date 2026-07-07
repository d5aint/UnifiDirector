from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.integration_acl_rule_page_dto import IntegrationAclRulePageDto
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
        "url": "/v1/sites/{site_id}/acl-rules".format(
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IntegrationAclRulePageDto | None:
    if response.status_code == 200:
        response_200 = IntegrationAclRulePageDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IntegrationAclRulePageDto]:
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
) -> Response[IntegrationAclRulePageDto]:
    """List ACL Rules

     Retrieve a paginated list of all ACL rules on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`type`|`STRING`|`eq` `ne` `in` `notIn`|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`enabled`|`BOOLEAN`|`eq` `ne`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`description`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn` `like`|
    |`action`|`STRING`|`eq` `ne` `in` `notIn`|
    |`index`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`protocolFilter`|`SET(STRING)`|`isNull` `isNotNull` `contains` `containsAny` `containsAll`
    `containsExactly`|
    |`networkId`|`UUID`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`enforcingDeviceFilter.deviceIds`|`SET(UUID)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
    |`sourceFilter.type`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`sourceFilter.ipAddressesOrSubnets`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`sourceFilter.portFilter`|`SET(INTEGER)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`sourceFilter.networkIds`|`SET(UUID)`|`contains` `containsAny` `containsAll` `containsExactly`|
    |`sourceFilter.macAddresses`|`SET(STRING)`|`contains` `containsAny` `containsAll` `containsExactly`|
    |`sourceFilter.prefixLength`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in`
    `notIn`|
    |`destinationFilter.type`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`destinationFilter.ipAddressesOrSubnets`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.portFilter`|`SET(INTEGER)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`destinationFilter.networkIds`|`SET(UUID)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.macAddresses`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.prefixLength`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in`
    `notIn`|
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
        Response[IntegrationAclRulePageDto]
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
) -> IntegrationAclRulePageDto | None:
    """List ACL Rules

     Retrieve a paginated list of all ACL rules on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`type`|`STRING`|`eq` `ne` `in` `notIn`|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`enabled`|`BOOLEAN`|`eq` `ne`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`description`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn` `like`|
    |`action`|`STRING`|`eq` `ne` `in` `notIn`|
    |`index`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`protocolFilter`|`SET(STRING)`|`isNull` `isNotNull` `contains` `containsAny` `containsAll`
    `containsExactly`|
    |`networkId`|`UUID`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`enforcingDeviceFilter.deviceIds`|`SET(UUID)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
    |`sourceFilter.type`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`sourceFilter.ipAddressesOrSubnets`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`sourceFilter.portFilter`|`SET(INTEGER)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`sourceFilter.networkIds`|`SET(UUID)`|`contains` `containsAny` `containsAll` `containsExactly`|
    |`sourceFilter.macAddresses`|`SET(STRING)`|`contains` `containsAny` `containsAll` `containsExactly`|
    |`sourceFilter.prefixLength`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in`
    `notIn`|
    |`destinationFilter.type`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`destinationFilter.ipAddressesOrSubnets`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.portFilter`|`SET(INTEGER)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`destinationFilter.networkIds`|`SET(UUID)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.macAddresses`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.prefixLength`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in`
    `notIn`|
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
        IntegrationAclRulePageDto
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
) -> Response[IntegrationAclRulePageDto]:
    """List ACL Rules

     Retrieve a paginated list of all ACL rules on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`type`|`STRING`|`eq` `ne` `in` `notIn`|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`enabled`|`BOOLEAN`|`eq` `ne`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`description`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn` `like`|
    |`action`|`STRING`|`eq` `ne` `in` `notIn`|
    |`index`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`protocolFilter`|`SET(STRING)`|`isNull` `isNotNull` `contains` `containsAny` `containsAll`
    `containsExactly`|
    |`networkId`|`UUID`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`enforcingDeviceFilter.deviceIds`|`SET(UUID)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
    |`sourceFilter.type`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`sourceFilter.ipAddressesOrSubnets`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`sourceFilter.portFilter`|`SET(INTEGER)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`sourceFilter.networkIds`|`SET(UUID)`|`contains` `containsAny` `containsAll` `containsExactly`|
    |`sourceFilter.macAddresses`|`SET(STRING)`|`contains` `containsAny` `containsAll` `containsExactly`|
    |`sourceFilter.prefixLength`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in`
    `notIn`|
    |`destinationFilter.type`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`destinationFilter.ipAddressesOrSubnets`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.portFilter`|`SET(INTEGER)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`destinationFilter.networkIds`|`SET(UUID)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.macAddresses`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.prefixLength`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in`
    `notIn`|
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
        Response[IntegrationAclRulePageDto]
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
) -> IntegrationAclRulePageDto | None:
    """List ACL Rules

     Retrieve a paginated list of all ACL rules on a site.

    <details>
    <summary>Filterable properties (click to expand)</summary>

    |Name|Type|Allowed functions|
    |-|-|-|
    |`type`|`STRING`|`eq` `ne` `in` `notIn`|
    |`id`|`UUID`|`eq` `ne` `in` `notIn`|
    |`enabled`|`BOOLEAN`|`eq` `ne`|
    |`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
    |`description`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn` `like`|
    |`action`|`STRING`|`eq` `ne` `in` `notIn`|
    |`index`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
    |`protocolFilter`|`SET(STRING)`|`isNull` `isNotNull` `contains` `containsAny` `containsAll`
    `containsExactly`|
    |`networkId`|`UUID`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`enforcingDeviceFilter.deviceIds`|`SET(UUID)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
    |`sourceFilter.type`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`sourceFilter.ipAddressesOrSubnets`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`sourceFilter.portFilter`|`SET(INTEGER)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`sourceFilter.networkIds`|`SET(UUID)`|`contains` `containsAny` `containsAll` `containsExactly`|
    |`sourceFilter.macAddresses`|`SET(STRING)`|`contains` `containsAny` `containsAll` `containsExactly`|
    |`sourceFilter.prefixLength`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in`
    `notIn`|
    |`destinationFilter.type`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
    |`destinationFilter.ipAddressesOrSubnets`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.portFilter`|`SET(INTEGER)`|`isNull` `isNotNull` `contains` `containsAny`
    `containsAll` `containsExactly`|
    |`destinationFilter.networkIds`|`SET(UUID)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.macAddresses`|`SET(STRING)`|`contains` `containsAny` `containsAll`
    `containsExactly`|
    |`destinationFilter.prefixLength`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in`
    `notIn`|
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
        IntegrationAclRulePageDto
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
