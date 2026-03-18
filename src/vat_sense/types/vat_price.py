# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VatPrice"]


class VatPrice(BaseModel):
    object: Optional[Literal["vat_price"]] = None

    price: Optional[float] = None
    """The price provided."""

    price_excl_vat: Optional[float] = None
    """The calculated price exclusive of VAT."""

    price_incl_vat: Optional[float] = None
    """The calculated price inclusive of VAT."""

    tax_type: Optional[Literal["incl", "excl"]] = None
    """Whether the price is inclusive or exclusive of VAT."""

    vat: Optional[float] = None
    """The total VAT amount."""

    vat_rate: Optional[float] = None
    """The VAT rate percentage."""
