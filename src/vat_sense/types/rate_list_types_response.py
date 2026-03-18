# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RateListTypesResponse"]


class RateListTypesResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[List[str]] = None

    success: Optional[bool] = None
