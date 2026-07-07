from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_id: UUID,
    wifi_broadcast_id: UUID,
    *,
    force: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/sites/{site_id}/wifi/broadcasts/{wifi_broadcast_id}".format(
            site_id=quote(str(site_id), safe=""),
            wifi_broadcast_id=quote(str(wifi_broadcast_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: UUID,
    wifi_broadcast_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = False,
) -> Response[Any]:
    """Delete Wifi Broadcast

     Delete an existing Wifi Broadcast from the specified site.

    Args:
        site_id (UUID):
        wifi_broadcast_id (UUID):
        force (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        wifi_broadcast_id=wifi_broadcast_id,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    site_id: UUID,
    wifi_broadcast_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = False,
) -> Response[Any]:
    """Delete Wifi Broadcast

     Delete an existing Wifi Broadcast from the specified site.

    Args:
        site_id (UUID):
        wifi_broadcast_id (UUID):
        force (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        wifi_broadcast_id=wifi_broadcast_id,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
