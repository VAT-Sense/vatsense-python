# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .invoice.invoice import Invoice

__all__ = ["InvoiceListResponse"]


class InvoiceListResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[List[Invoice]] = None

    success: Optional[bool] = None
