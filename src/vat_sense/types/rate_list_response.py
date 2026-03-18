# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .rate import Rate
from .._models import BaseModel

__all__ = ["RateListResponse"]


class RateListResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[List[Rate]] = None

    success: Optional[bool] = None
