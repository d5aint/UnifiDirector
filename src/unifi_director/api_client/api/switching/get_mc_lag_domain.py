from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.integration_mc_lag_domain_dto import IntegrationMcLagDomainDto
from ...types import Response


def _get_kwargs(
    site_id: UUID,
    mc_lag_domain_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sites/{site_id}/switching/mc-lag-domains/{mc_lag_domain_id}".format(
            site_id=quote(str(site_id), safe=""),
            mc_lag_domain_id=quote(str(mc_lag_domain_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IntegrationMcLagDomainDto | None:
    if response.status_code == 200:
        response_200 = IntegrationMcLagDomainDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IntegrationMcLagDomainDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: UUID,
    mc_lag_domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[IntegrationMcLagDomainDto]:
    """Get MC-LAG Domain

     Retrieve MC-LAG Domain details.

    Args:
        site_id (UUID):
        mc_lag_domain_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationMcLagDomainDto]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        mc_lag_domain_id=mc_lag_domain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: UUID,
    mc_lag_domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> IntegrationMcLagDomainDto | None:
    """Get MC-LAG Domain

     Retrieve MC-LAG Domain details.

    Args:
        site_id (UUID):
        mc_lag_domain_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationMcLagDomainDto
    """

    return sync_detailed(
        site_id=site_id,
        mc_lag_domain_id=mc_lag_domain_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    site_id: UUID,
    mc_lag_domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[IntegrationMcLagDomainDto]:
    """Get MC-LAG Domain

     Retrieve MC-LAG Domain details.

    Args:
        site_id (UUID):
        mc_lag_domain_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationMcLagDomainDto]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        mc_lag_domain_id=mc_lag_domain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: UUID,
    mc_lag_domain_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> IntegrationMcLagDomainDto | None:
    """Get MC-LAG Domain

     Retrieve MC-LAG Domain details.

    Args:
        site_id (UUID):
        mc_lag_domain_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationMcLagDomainDto
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            mc_lag_domain_id=mc_lag_domain_id,
            client=client,
        )
    ).parsed
