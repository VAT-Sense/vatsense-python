# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvoiceConversionInputParam"]


class InvoiceConversionInputParam(TypedDict, total=False):
    currency_code: Required[str]
    """The 3-character currency code for the conversion."""

    rate: Required[float]
    """The rate of conversion."""
