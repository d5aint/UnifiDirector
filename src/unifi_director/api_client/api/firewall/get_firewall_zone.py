from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.firewall_zone import FirewallZone
from ...types import Response


def _get_kwargs(
    site_id: UUID,
    firewall_zone_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sites/{site_id}/firewall/zones/{firewall_zone_id}".format(
            site_id=quote(str(site_id), safe=""),
            firewall_zone_id=quote(str(firewall_zone_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FirewallZone | None:
    if response.status_code == 200:
        response_200 = FirewallZone.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FirewallZone]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: UUID,
    firewall_zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallZone]:
    """Get Firewall Zone

     Get a firewall zone on a site.

    Args:
        site_id (UUID):
        firewall_zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallZone]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        firewall_zone_id=firewall_zone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: UUID,
    firewall_zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallZone | None:
    """Get Firewall Zone

     Get a firewall zone on a site.

    Args:
        site_id (UUID):
        firewall_zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallZone
    """

    return sync_detailed(
        site_id=site_id,
        firewall_zone_id=firewall_zone_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    firewall_zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FirewallZone]:
    """Get Firewall Zone

     Get a firewall zone on a site.

    Args:
        site_id (UUID):
        firewall_zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirewallZone]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        firewall_zone_id=firewall_zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    firewall_zone_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FirewallZone | None:
    """Get Firewall Zone

     Get a firewall zone on a site.

    Args:
        site_id (UUID):
        firewall_zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirewallZone
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            firewall_zone_id=firewall_zone_id,
            client=client,
        )
    ).parsed
