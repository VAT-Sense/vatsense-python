# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    limit: int
    """Number of invoices to return (default 10, max 100)."""

    offset: int
    """Number of invoices to skip (default 0)."""

    search: str
    """Search query to filter invoices."""
