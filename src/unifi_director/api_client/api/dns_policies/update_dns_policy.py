from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_or_update_dns_policy import CreateOrUpdateDNSPolicy
from ...models.dns_policy import DNSPolicy
from ...types import Response


def _get_kwargs(
    site_id: UUID,
    dns_policy_id: UUID,
    *,
    body: CreateOrUpdateDNSPolicy,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/sites/{site_id}/dns/policies/{dns_policy_id}".format(
            site_id=quote(str(site_id), safe=""),
            dns_policy_id=quote(str(dns_policy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DNSPolicy | None:
    if response.status_code == 200:
        response_200 = DNSPolicy.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DNSPolicy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: UUID,
    dns_policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateDNSPolicy,
) -> Response[DNSPolicy]:
    """Update DNS Policy

     Update an existing DNS policy on a site.

    Args:
        site_id (UUID):
        dns_policy_id (UUID):
        body (CreateOrUpdateDNSPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSPolicy]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        dns_policy_id=dns_policy_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: UUID,
    dns_policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateDNSPolicy,
) -> DNSPolicy | None:
    """Update DNS Policy

     Update an existing DNS policy on a site.

    Args:
        site_id (UUID):
        dns_policy_id (UUID):
        body (CreateOrUpdateDNSPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSPolicy
    """

    return sync_detailed(
        site_id=site_id,
        dns_policy_id=dns_policy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    dns_policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateDNSPolicy,
) -> Response[DNSPolicy]:
    """Update DNS Policy

     Update an existing DNS policy on a site.

    Args:
        site_id (UUID):
        dns_policy_id (UUID):
        body (CreateOrUpdateDNSPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSPolicy]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        dns_policy_id=dns_policy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    dns_policy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateDNSPolicy,
) -> DNSPolicy | None:
    """Update DNS Policy

     Update an existing DNS policy on a site.

    Args:
        site_id (UUID):
        dns_policy_id (UUID):
        body (CreateOrUpdateDNSPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSPolicy
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            dns_policy_id=dns_policy_id,
            client=client,
            body=body,
        )
    ).parsed
