# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .invoice_item import InvoiceItem

__all__ = ["ItemRetrieveResponse"]


class ItemRetrieveResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[InvoiceItem] = None

    success: Optional[bool] = None
