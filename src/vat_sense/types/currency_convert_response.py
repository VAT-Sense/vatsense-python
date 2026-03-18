# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CurrencyConvertResponse", "Data"]


class Data(BaseModel):
    amount: Optional[float] = None
    """The original amount."""

    converted: Optional[float] = None
    """The converted amount."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    object: Optional[Literal["conversion"]] = None

    rate: Optional[float] = None
    """The exchange rate used."""

    to: Optional[str] = None


class CurrencyConvertResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    success: Optional[bool] = None
