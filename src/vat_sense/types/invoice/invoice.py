# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .invoice_item import InvoiceItem
from ..invoice_conversion_input import InvoiceConversionInput

__all__ = ["Invoice", "Business", "Customer", "Totals"]


class Business(BaseModel):
    address: Optional[str] = None

    company_number: Optional[str] = None

    logo: Optional[str] = None

    name: Optional[str] = None

    vat_number: Optional[str] = None


class Customer(BaseModel):
    address: Optional[str] = None

    company_number: Optional[str] = None

    logo: Optional[str] = None

    name: Optional[str] = None

    vat_number: Optional[str] = None


class Totals(BaseModel):
    discount: Optional[float] = None
    """Total discount amount."""

    subtotal: Optional[float] = None
    """Total before VAT."""

    total: Optional[float] = None
    """Grand total."""

    vat: Optional[float] = None
    """Total VAT amount."""


class Invoice(BaseModel):
    id: Optional[str] = None

    business: Optional[Business] = None

    conversion: Optional[InvoiceConversionInput] = None

    created: Optional[datetime] = None

    currency_code: Optional[str] = None

    customer: Optional[Customer] = None

    date: Optional[str] = None

    has_vat: Optional[bool] = None

    invoice_number: Optional[str] = None

    invoice_url: Optional[str] = None
    """Unique URL to view the invoice. Append "/pdf" to download a PDF copy."""

    is_copy: Optional[bool] = None

    is_reverse_charge: Optional[bool] = None

    items: Optional[List[InvoiceItem]] = None

    notes: Optional[str] = None

    num_items: Optional[int] = None

    object: Optional[Literal["invoice"]] = None

    tax_point: Optional[str] = None

    tax_type: Optional[Literal["incl", "excl"]] = None

    totals: Optional[Totals] = None

    type: Optional[Literal["sale", "refund"]] = None

    updated: Optional[datetime] = None

    zero_rated: Optional[bool] = None
