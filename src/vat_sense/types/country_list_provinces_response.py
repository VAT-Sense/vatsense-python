# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CountryListProvincesResponse", "Data"]


class Data(BaseModel):
    country_code: Optional[str] = None

    object: Optional[Literal["province"]] = None

    province_code: Optional[str] = None

    province_name: Optional[str] = None


class CountryListProvincesResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[List[Data]] = None

    success: Optional[bool] = None
