# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CurrencyConvertParams"]


class CurrencyConvertParams(TypedDict, total=False):
    amount: Required[str]
    """The amount to convert.

    Must be a string with exactly 2 decimal places (e.g. "39.99").
    """

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """The 3-character source currency code (e.g. "USD", "CAD")."""

    to: Required[Literal["GBP", "EUR"]]
    """The 3-character target currency code. Must be either "GBP" or "EUR"."""
