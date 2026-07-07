from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_or_update_traffic_matching_list import CreateOrUpdateTrafficMatchingList
from ...models.traffic_matching_list import TrafficMatchingList
from ...types import Response


def _get_kwargs(
    site_id: UUID,
    traffic_matching_list_id: UUID,
    *,
    body: CreateOrUpdateTrafficMatchingList,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/sites/{site_id}/traffic-matching-lists/{traffic_matching_list_id}".format(
            site_id=quote(str(site_id), safe=""),
            traffic_matching_list_id=quote(str(traffic_matching_list_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TrafficMatchingList | None:
    if response.status_code == 200:
        response_200 = TrafficMatchingList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TrafficMatchingList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: UUID,
    traffic_matching_list_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateTrafficMatchingList,
) -> Response[TrafficMatchingList]:
    """Update Traffic Matching List

     Update an exist traffic matching list on a site.

    Args:
        site_id (UUID):
        traffic_matching_list_id (UUID):
        body (CreateOrUpdateTrafficMatchingList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrafficMatchingList]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        traffic_matching_list_id=traffic_matching_list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: UUID,
    traffic_matching_list_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateTrafficMatchingList,
) -> TrafficMatchingList | None:
    """Update Traffic Matching List

     Update an exist traffic matching list on a site.

    Args:
        site_id (UUID):
        traffic_matching_list_id (UUID):
        body (CreateOrUpdateTrafficMatchingList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrafficMatchingList
    """

    return sync_detailed(
        site_id=site_id,
        traffic_matching_list_id=traffic_matching_list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    traffic_matching_list_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateTrafficMatchingList,
) -> Response[TrafficMatchingList]:
    """Update Traffic Matching List

     Update an exist traffic matching list on a site.

    Args:
        site_id (UUID):
        traffic_matching_list_id (UUID):
        body (CreateOrUpdateTrafficMatchingList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrafficMatchingList]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        traffic_matching_list_id=traffic_matching_list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    traffic_matching_list_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateTrafficMatchingList,
) -> TrafficMatchingList | None:
    """Update Traffic Matching List

     Update an exist traffic matching list on a site.

    Args:
        site_id (UUID):
        traffic_matching_list_id (UUID):
        body (CreateOrUpdateTrafficMatchingList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrafficMatchingList
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            traffic_matching_list_id=traffic_matching_list_id,
            client=client,
            body=body,
        )
    ).parsed
