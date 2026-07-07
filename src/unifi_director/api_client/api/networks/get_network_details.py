from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.network_details import NetworkDetails
from ...types import Response


def _get_kwargs(
    site_id: UUID,
    network_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sites/{site_id}/networks/{network_id}".format(
            site_id=quote(str(site_id), safe=""),
            network_id=quote(str(network_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> NetworkDetails | None:
    if response.status_code == 200:
        response_200 = NetworkDetails.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[NetworkDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: UUID,
    network_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[NetworkDetails]:
    """Get Network Details

     Retrieve detailed information about a specific network.

    Args:
        site_id (UUID):
        network_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkDetails]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        network_id=network_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: UUID,
    network_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> NetworkDetails | None:
    """Get Network Details

     Retrieve detailed information about a specific network.

    Args:
        site_id (UUID):
        network_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkDetails
    """

    return sync_detailed(
        site_id=site_id,
        network_id=network_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    network_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[NetworkDetails]:
    """Get Network Details

     Retrieve detailed information about a specific network.

    Args:
        site_id (UUID):
        network_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkDetails]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        network_id=network_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    network_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> NetworkDetails | None:
    """Get Network Details

     Retrieve detailed information about a specific network.

    Args:
        site_id (UUID):
        network_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkDetails
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            network_id=network_id,
            client=client,
        )
    ).parsed
