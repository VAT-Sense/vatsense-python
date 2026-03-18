# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvoiceItemInputParam"]


class InvoiceItemInputParam(TypedDict, total=False):
    item: Required[str]
    """The description of the line item."""

    price_each: Required[float]
    """The price per item. Must be a decimal with 2 decimal places."""

    quantity: Required[float]
    """The quantity of the item."""

    vat_rate: Required[float]
    """A percentage VAT rate for this item."""

    discount_rate: float
    """A percentage discount to apply to the price."""
