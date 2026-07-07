from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.integration_firewall_policy_ordering_dto import IntegrationFirewallPolicyOrderingDto
from ...types import UNSET, Response


def _get_kwargs(
    site_id: UUID,
    *,
    source_firewall_zone_id: UUID,
    destination_firewall_zone_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_source_firewall_zone_id = str(source_firewall_zone_id)
    params["sourceFirewallZoneId"] = json_source_firewall_zone_id

    json_destination_firewall_zone_id = str(destination_firewall_zone_id)
    params["destinationFirewallZoneId"] = json_destination_firewall_zone_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sites/{site_id}/firewall/policies/ordering".format(
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IntegrationFirewallPolicyOrderingDto | None:
    if response.status_code == 200:
        response_200 = IntegrationFirewallPolicyOrderingDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IntegrationFirewallPolicyOrderingDto]:
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
    source_firewall_zone_id: UUID,
    destination_firewall_zone_id: UUID,
) -> Response[IntegrationFirewallPolicyOrderingDto]:
    """Get User-Defined Firewall Policy Ordering

     Retrieve user-defined firewall policy ordering for a specific source/destination zone pair.

    Args:
        site_id (UUID):
        source_firewall_zone_id (UUID):
        destination_firewall_zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationFirewallPolicyOrderingDto]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        source_firewall_zone_id=source_firewall_zone_id,
        destination_firewall_zone_id=destination_firewall_zone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    source_firewall_zone_id: UUID,
    destination_firewall_zone_id: UUID,
) -> IntegrationFirewallPolicyOrderingDto | None:
    """Get User-Defined Firewall Policy Ordering

     Retrieve user-defined firewall policy ordering for a specific source/destination zone pair.

    Args:
        site_id (UUID):
        source_firewall_zone_id (UUID):
        destination_firewall_zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationFirewallPolicyOrderingDto
    """

    return sync_detailed(
        site_id=site_id,
        client=client,
        source_firewall_zone_id=source_firewall_zone_id,
        destination_firewall_zone_id=destination_firewall_zone_id,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    source_firewall_zone_id: UUID,
    destination_firewall_zone_id: UUID,
) -> Response[IntegrationFirewallPolicyOrderingDto]:
    """Get User-Defined Firewall Policy Ordering

     Retrieve user-defined firewall policy ordering for a specific source/destination zone pair.

    Args:
        site_id (UUID):
        source_firewall_zone_id (UUID):
        destination_firewall_zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationFirewallPolicyOrderingDto]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        source_firewall_zone_id=source_firewall_zone_id,
        destination_firewall_zone_id=destination_firewall_zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    source_firewall_zone_id: UUID,
    destination_firewall_zone_id: UUID,
) -> IntegrationFirewallPolicyOrderingDto | None:
    """Get User-Defined Firewall Policy Ordering

     Retrieve user-defined firewall policy ordering for a specific source/destination zone pair.

    Args:
        site_id (UUID):
        source_firewall_zone_id (UUID):
        destination_firewall_zone_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationFirewallPolicyOrderingDto
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            client=client,
            source_firewall_zone_id=source_firewall_zone_id,
            destination_firewall_zone_id=destination_firewall_zone_id,
        )
    ).parsed
