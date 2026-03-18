# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .rate_with_tax_rate import RateWithTaxRate

__all__ = ["FindRate"]


class FindRate(BaseModel):
    code: Optional[int] = None

    data: Optional[RateWithTaxRate] = None

    success: Optional[bool] = None
