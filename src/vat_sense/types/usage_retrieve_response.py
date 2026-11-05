# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UsageRetrieveResponse", "Data", "DataRequests"]


class DataRequests(BaseModel):
    remaining: Optional[int] = None
    """Requests remaining before the limit is reached."""

    total: Optional[int] = None
    """
    Requests available in the current billing period (plan, request packs and,
    while overage is on, the overage allowed).
    """

    used: Optional[int] = None
    """Requests used so far in the current billing period."""


class Data(BaseModel):
    requests: Optional[DataRequests] = None


class UsageRetrieveResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    success: Optional[bool] = None
