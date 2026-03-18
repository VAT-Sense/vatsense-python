# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .country import Country
from .._models import BaseModel

__all__ = ["CountryListResponse", "SingleCountryResponse"]


class SingleCountryResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Country] = None

    success: Optional[bool] = None


CountryListResponse: TypeAlias = Union[CountryListResponse, SingleCountryResponse]
