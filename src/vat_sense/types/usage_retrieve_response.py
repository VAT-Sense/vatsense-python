# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UsageRetrieveResponse", "Data", "DataRequests"]


class DataRequests(BaseModel):
    remaining: Optional[int] = None
    """Requests remaining before the limit is reached."""

    total: Optional[int] = None
    """Total requests allowed on your plan."""

    used: Optional[int] = None
    """Requests used in the last 30 days."""


class Data(BaseModel):
    requests: Optional[DataRequests] = None


class UsageRetrieveResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    success: Optional[bool] = None
