# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["InvoiceConversionInput"]


class InvoiceConversionInput(BaseModel):
    currency_code: str
    """The 3-character currency code for the conversion."""

    rate: float
    """The rate of conversion."""
