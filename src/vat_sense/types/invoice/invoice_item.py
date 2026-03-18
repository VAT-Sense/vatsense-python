# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InvoiceItem"]


class InvoiceItem(BaseModel):
    id: Optional[str] = None

    discount_rate: Optional[float] = None

    item: Optional[str] = None

    object: Optional[Literal["item"]] = None

    price_each: Optional[float] = None

    price_total: Optional[float] = None

    quantity: Optional[float] = None

    vat_rate: Optional[float] = None
