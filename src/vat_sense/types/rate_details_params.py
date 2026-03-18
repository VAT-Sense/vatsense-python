# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RateDetailsParams"]


class RateDetailsParams(TypedDict, total=False):
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

    period: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """A historical date to retrieve rates for (format "YYYY-MM-DD HH:MM:SS").

    Must be a past date.
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
