# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .vat_price import VatPrice

__all__ = ["CurrencyCalculateVatPriceResponse"]


class CurrencyCalculateVatPriceResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[VatPrice] = None

    success: Optional[bool] = None
