# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .invoice_business_input_param import InvoiceBusinessInputParam
from .invoice_customer_input_param import InvoiceCustomerInputParam
from .invoice_conversion_input_param import InvoiceConversionInputParam
from .invoice.invoice_item_input_param import InvoiceItemInputParam

__all__ = ["InvoiceCreateParams"]


class InvoiceCreateParams(TypedDict, total=False):
    business: Required[InvoiceBusinessInputParam]

    currency_code: Required[str]
    """The 3-character currency code the invoice is billed in."""

    date: Required[str]
    """The date the invoice was issued (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS)."""

    items: Required[Iterable[InvoiceItemInputParam]]

    tax_point: Required[str]
    """The tax point or "time of supply" (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS)."""

    conversion: InvoiceConversionInputParam

    customer: InvoiceCustomerInputParam

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
