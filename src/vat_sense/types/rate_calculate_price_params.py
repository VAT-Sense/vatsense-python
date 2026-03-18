# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RateCalculatePriceParams"]


class RateCalculatePriceParams(TypedDict, total=False):
    price: Required[str]
    """The price to calculate on.

    Must be a string with exactly 2 decimal places (e.g. "30.00", "59.95").
    """

    tax_type: Required[Literal["incl", "excl"]]
    """Whether the provided price is inclusive or exclusive of VAT."""

    country_code: str
    """A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR")."""

    eu: bool
    """Filter results by EU membership.

    Use 1 for EU countries only, 0 for non-EU only.
    """

    ip_address: str
    """An IPv4 or IPv6 address.

    If provided, the country will be determined from the IP address.
    """

    province_code: str
    """A 2-character province code (e.g.

    "NU", "NT"). If providing a province code, you must also provide the relevant
    country_code.
    """

    type: str
    """The product type to find the applicable rate for.

    See the /rates/types endpoint for a full list of valid values.
    """
