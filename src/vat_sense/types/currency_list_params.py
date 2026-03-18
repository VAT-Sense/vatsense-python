# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CurrencyListParams"]


class CurrencyListParams(TypedDict, total=False):
    from_: Annotated[str, PropertyInfo(alias="from")]
    """The 3-character currency code(s) to convert from (e.g.

    "USD", "CAD"). Can be a comma-separated list without spaces (e.g.
    "USD,CAD,AUD").
    """

    to: Literal["GBP", "EUR"]
    """The 3-character target currency code. Must be either "GBP" or "EUR"."""
