# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["InvoiceDeleteResponse"]


class InvoiceDeleteResponse(BaseModel):
    code: int

    success: bool
