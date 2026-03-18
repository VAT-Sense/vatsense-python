# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CountryListParams"]


class CountryListParams(TypedDict, total=False):
    country_code: str
    """A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR")."""

    ip_address: str
    """An IPv4 or IPv6 address.

    If provided, the country will be determined from the IP address.
    """
