# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .rate import Rate
from .._models import BaseModel

__all__ = ["RateListResponse", "SingleRateResponse"]


class SingleRateResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Rate] = None

    success: Optional[bool] = None


RateListResponse: TypeAlias = Union[RateListResponse, SingleRateResponse]
