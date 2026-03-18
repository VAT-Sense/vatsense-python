# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvoiceBusinessInputParam"]


class InvoiceBusinessInputParam(TypedDict, total=False):
    address: Required[str]
    """Your business trading address."""

    name: Required[str]
    """Your business trading name."""

    vat_number: Required[str]
    """Your business VAT number."""

    bank_account: str

    company_number: str
    """Your business company number."""

    email: str

    logo: str
    """URL to your company logo (HTTPS only, .svg/.jpg/.png).

    Recommended 240px by 60px.
    """

    phone: str

    website: str
