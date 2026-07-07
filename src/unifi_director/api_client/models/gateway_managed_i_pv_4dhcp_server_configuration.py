from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_address_range import IPAddressRange
    from ..models.pxe_configuration import PXEConfiguration


T = TypeVar("T", bound="GatewayManagedIPv4DHCPServerConfiguration")


@_attrs_define
class GatewayManagedIPv4DHCPServerConfiguration:
    """
    Attributes:
        mode (str):
        ip_address_range (IPAddressRange):
        lease_time_seconds (int): The lease time in seconds for addresses in this range.
        ping_conflict_detection_enabled (bool):
        gateway_ip_address_override (str | Unset): Gateway IP address provided to DHCP clients. If null, the default
            gateway will be assigned.
        dns_server_ip_addresses_override (list[str] | Unset): List of DNS servers assigned to client devices by the DHCP
            server. If none are specified, they will be selected automatically.
        domain_name (str | Unset): Domain name that can be used to access network in the browser.
        pxe_configuration (PXEConfiguration | Unset):
        ntp_server_ip_addresses (list[str] | Unset): Network Time Protocol (NTP) server IP addresses.
        option_43_value (str | Unset): Custom DHCP option (43) â€” the value MUST be the UniFi Network application's
            host IP address.
        tftp_server_address (str | Unset): Trivial File Transfer Protocol (TFTP) server address â€” accepts a hostname,
            URL or IP address.
        time_offset_seconds (int | Unset): Time offset in seconds from UTC.
        wpad_url (str | Unset): Web Proxy Auto-Discovery (WPAD) URL.
        wins_server_ip_addresses (list[str] | Unset): Windows Internet Name Service (WINS) server IP addresses.
    """

    mode: str
    ip_address_range: IPAddressRange
    lease_time_seconds: int
    ping_conflict_detection_enabled: bool
    gateway_ip_address_override: str | Unset = UNSET
    dns_server_ip_addresses_override: list[str] | Unset = UNSET
    domain_name: str | Unset = UNSET
    pxe_configuration: PXEConfiguration | Unset = UNSET
    ntp_server_ip_addresses: list[str] | Unset = UNSET
    option_43_value: str | Unset = UNSET
    tftp_server_address: str | Unset = UNSET
    time_offset_seconds: int | Unset = UNSET
    wpad_url: str | Unset = UNSET
    wins_server_ip_addresses: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        ip_address_range = self.ip_address_range.to_dict()

        lease_time_seconds = self.lease_time_seconds

        ping_conflict_detection_enabled = self.ping_conflict_detection_enabled

        gateway_ip_address_override = self.gateway_ip_address_override

        dns_server_ip_addresses_override: list[str] | Unset = UNSET
        if not isinstance(self.dns_server_ip_addresses_override, Unset):
            dns_server_ip_addresses_override = self.dns_server_ip_addresses_override

        domain_name = self.domain_name

        pxe_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pxe_configuration, Unset):
            pxe_configuration = self.pxe_configuration.to_dict()

        ntp_server_ip_addresses: list[str] | Unset = UNSET
        if not isinstance(self.ntp_server_ip_addresses, Unset):
            ntp_server_ip_addresses = self.ntp_server_ip_addresses

        option_43_value = self.option_43_value

        tftp_server_address = self.tftp_server_address

        time_offset_seconds = self.time_offset_seconds

        wpad_url = self.wpad_url

        wins_server_ip_addresses: list[str] | Unset = UNSET
        if not isinstance(self.wins_server_ip_addresses, Unset):
            wins_server_ip_addresses = self.wins_server_ip_addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "ipAddressRange": ip_address_range,
                "leaseTimeSeconds": lease_time_seconds,
                "pingConflictDetectionEnabled": ping_conflict_detection_enabled,
            }
        )
        if gateway_ip_address_override is not UNSET:
            field_dict["gatewayIpAddressOverride"] = gateway_ip_address_override
        if dns_server_ip_addresses_override is not UNSET:
            field_dict["dnsServerIpAddressesOverride"] = dns_server_ip_addresses_override
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if pxe_configuration is not UNSET:
            field_dict["pxeConfiguration"] = pxe_configuration
        if ntp_server_ip_addresses is not UNSET:
            field_dict["ntpServerIpAddresses"] = ntp_server_ip_addresses
        if option_43_value is not UNSET:
            field_dict["option43Value"] = option_43_value
        if tftp_server_address is not UNSET:
            field_dict["tftpServerAddress"] = tftp_server_address
        if time_offset_seconds is not UNSET:
            field_dict["timeOffsetSeconds"] = time_offset_seconds
        if wpad_url is not UNSET:
            field_dict["wpadUrl"] = wpad_url
        if wins_server_ip_addresses is not UNSET:
            field_dict["winsServerIpAddresses"] = wins_server_ip_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_address_range import IPAddressRange
        from ..models.pxe_configuration import PXEConfiguration

        d = dict(src_dict)
        mode = d.pop("mode")

        ip_address_range = IPAddressRange.from_dict(d.pop("ipAddressRange"))

        lease_time_seconds = d.pop("leaseTimeSeconds")

        ping_conflict_detection_enabled = d.pop("pingConflictDetectionEnabled")

        gateway_ip_address_override = d.pop("gatewayIpAddressOverride", UNSET)

        dns_server_ip_addresses_override = cast(list[str], d.pop("dnsServerIpAddressesOverride", UNSET))

        domain_name = d.pop("domainName", UNSET)

        _pxe_configuration = d.pop("pxeConfiguration", UNSET)
        pxe_configuration: PXEConfiguration | Unset
        if isinstance(_pxe_configuration, Unset):
            pxe_configuration = UNSET
        else:
            pxe_configuration = PXEConfiguration.from_dict(_pxe_configuration)

        ntp_server_ip_addresses = cast(list[str], d.pop("ntpServerIpAddresses", UNSET))

        option_43_value = d.pop("option43Value", UNSET)

        tftp_server_address = d.pop("tftpServerAddress", UNSET)

        time_offset_seconds = d.pop("timeOffsetSeconds", UNSET)

        wpad_url = d.pop("wpadUrl", UNSET)

        wins_server_ip_addresses = cast(list[str], d.pop("winsServerIpAddresses", UNSET))

        gateway_managed_i_pv_4dhcp_server_configuration = cls(
            mode=mode,
            ip_address_range=ip_address_range,
            lease_time_seconds=lease_time_seconds,
            ping_conflict_detection_enabled=ping_conflict_detection_enabled,
            gateway_ip_address_override=gateway_ip_address_override,
            dns_server_ip_addresses_override=dns_server_ip_addresses_override,
            domain_name=domain_name,
            pxe_configuration=pxe_configuration,
            ntp_server_ip_addresses=ntp_server_ip_addresses,
            option_43_value=option_43_value,
            tftp_server_address=tftp_server_address,
            time_offset_seconds=time_offset_seconds,
            wpad_url=wpad_url,
            wins_server_ip_addresses=wins_server_ip_addresses,
        )

        gateway_managed_i_pv_4dhcp_server_configuration.additional_properties = d
        return gateway_managed_i_pv_4dhcp_server_configuration

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
