# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvoiceCustomerInputParam"]


class InvoiceCustomerInputParam(TypedDict, total=False):
    name: Required[str]
    """The customer's trading name."""

    address: str

    company_number: str

    country_code: str

    email: str

    logo: str
    """URL to the customer logo (HTTPS only, .jpg/.png)."""

    vat_number: str
