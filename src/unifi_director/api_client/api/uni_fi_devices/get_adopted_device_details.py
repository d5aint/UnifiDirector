from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.adopted_device_details import AdoptedDeviceDetails
from ...types import Response


def _get_kwargs(
    site_id: UUID,
    device_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sites/{site_id}/devices/{device_id}".format(
            site_id=quote(str(site_id), safe=""),
            device_id=quote(str(device_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AdoptedDeviceDetails | None:
    if response.status_code == 200:
        response_200 = AdoptedDeviceDetails.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AdoptedDeviceDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: UUID,
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AdoptedDeviceDetails]:
    """Get Adopted Device Details

     Retrieve detailed information about a specific adopted device, including firmware versioning, uplink
    state, details about device features and interfaces (ports, radios) and other key attributes.

    Args:
        site_id (UUID):
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdoptedDeviceDetails]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        device_id=device_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: UUID,
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AdoptedDeviceDetails | None:
    """Get Adopted Device Details

     Retrieve detailed information about a specific adopted device, including firmware versioning, uplink
    state, details about device features and interfaces (ports, radios) and other key attributes.

    Args:
        site_id (UUID):
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdoptedDeviceDetails
    """

    return sync_detailed(
        site_id=site_id,
        device_id=device_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AdoptedDeviceDetails]:
    """Get Adopted Device Details

     Retrieve detailed information about a specific adopted device, including firmware versioning, uplink
    state, details about device features and interfaces (ports, radios) and other key attributes.

    Args:
        site_id (UUID):
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdoptedDeviceDetails]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        device_id=device_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AdoptedDeviceDetails | None:
    """Get Adopted Device Details

     Retrieve detailed information about a specific adopted device, including firmware versioning, uplink
    state, details about device features and interfaces (ports, radios) and other key attributes.

    Args:
        site_id (UUID):
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdoptedDeviceDetails
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            device_id=device_id,
            client=client,
        )
    ).parsed
