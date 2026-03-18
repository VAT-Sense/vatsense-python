# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tax_rate import TaxRate
from .vat_price import VatPrice

__all__ = ["RateCalculatePriceResponse", "Data"]


class Data(BaseModel):
    country_code: Optional[str] = None

    country_name: Optional[str] = None

    eu: Optional[bool] = None

    object: Optional[Literal["rate"]] = None

    tax_rate: Optional[TaxRate] = None

    vat_price: Optional[VatPrice] = None


class RateCalculatePriceResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    success: Optional[bool] = None
