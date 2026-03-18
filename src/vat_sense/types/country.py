# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Country"]


class Country(BaseModel):
    country_code: Optional[str] = None
    """2-character ISO 3166-1 alpha-2 country code."""

    country_name: Optional[str] = None

    eu: Optional[bool] = None
    """Whether the country is subject to EU VAT."""

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    object: Optional[Literal["country"]] = None

    vat: Optional[bool] = None
    """Whether the country is subject to VAT/GST."""
