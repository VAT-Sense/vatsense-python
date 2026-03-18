# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .invoice_conversion_input_param import InvoiceConversionInputParam
from .invoice.invoice_item_input_param import InvoiceItemInputParam

__all__ = ["InvoiceUpdateParams", "Business", "Customer"]


class InvoiceUpdateParams(TypedDict, total=False):
    business: Required[Business]

    currency_code: Required[str]
    """The 3-character currency code the invoice is billed in."""

    date: Required[str]
    """The date the invoice was issued (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS)."""

    items: Required[Iterable[InvoiceItemInputParam]]

    tax_point: Required[str]
    """The tax point or "time of supply" (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS)."""

    conversion: InvoiceConversionInputParam

    customer: Customer

    has_vat: bool
    """Whether the invoice is subject to VAT."""

    invoice_number: str
    """A unique invoice number.

    If not provided, defaults to an auto-incremented number.
    """

    is_copy: bool
    """Whether the invoice is a copy of a primary invoice."""

    is_reverse_charge: bool
    """Whether the invoice is zero-rated due to reverse charge."""

    notes: str
    """Any additional notes for the invoice."""

    pad_invoice_number: int
    """Pad the auto-generated invoice number with leading zeros to this length."""

    serial: str
    """A serial prepended to the auto-generated invoice number.

    Each unique serial has its own auto-increment range.
    """

    tax_type: Literal["incl", "excl"]
    """Whether item prices include or exclude VAT."""

    type: Literal["sale", "refund"]
    """The type of invoice."""

    zero_rated: bool
    """Whether the invoice has been zero-rated."""


class Business(TypedDict, total=False):
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


class Customer(TypedDict, total=False):
    name: Required[str]
    """The customer's trading name."""

    address: str

    company_number: str

    country_code: str

    email: str

    logo: str
    """URL to the customer logo (HTTPS only, .jpg/.png)."""

    vat_number: str
