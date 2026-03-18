# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CurrencyCalculateVatPriceParams"]


class CurrencyCalculateVatPriceParams(TypedDict, total=False):
    price: Required[float]
    """The price to calculate on. Must be a decimal with 2 decimal places."""

    tax_type: Required[Literal["incl", "excl"]]
    """Whether the provided price is inclusive or exclusive of VAT."""

    vat_rate: Required[float]
    """A percentage VAT rate to use for the calculation."""
