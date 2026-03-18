# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .invoice.invoice import Invoice

__all__ = ["InvoiceResponse"]


class InvoiceResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Invoice] = None

    success: Optional[bool] = None
