# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CurrencyListResponse", "Data"]


class Data(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The 3-character source currency code."""

    object: Optional[Literal["convert_rate"]] = None

    rate: Optional[float] = None
    """The exchange rate."""

    to: Optional[str] = None
    """The 3-character target currency code (GBP or EUR)."""


class CurrencyListResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[List[Data]] = None

    success: Optional[bool] = None
