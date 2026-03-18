# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .country import Country
from .._models import BaseModel

__all__ = ["CountryListResponse"]


class CountryListResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[List[Country]] = None

    success: Optional[bool] = None
