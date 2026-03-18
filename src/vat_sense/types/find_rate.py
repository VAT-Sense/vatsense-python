# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tax_rate import TaxRate

__all__ = ["FindRate", "Data"]


class Data(BaseModel):
    country_code: Optional[str] = None

    country_name: Optional[str] = None

    eu: Optional[bool] = None

    object: Optional[Literal["rate"]] = None

    tax_rate: Optional[TaxRate] = None


class FindRate(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    success: Optional[bool] = None
