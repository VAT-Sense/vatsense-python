# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tax_rate import TaxRate

__all__ = ["Rate", "Other"]


class Other(TaxRate):
    province: Optional[str] = None
    """The province this rate applies to, if applicable."""


class Rate(BaseModel):
    country_code: Optional[str] = None
    """2-character ISO 3166-1 alpha-2 country code."""

    country_name: Optional[str] = None

    eu: Optional[bool] = None
    """Whether the country is an EU member."""

    object: Optional[Literal["rate"]] = None

    other: Optional[List[Other]] = None
    """A list of other tax rates. Null if no additional rates exist."""

    standard: Optional[TaxRate] = None
