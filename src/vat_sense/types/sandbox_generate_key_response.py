# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SandboxGenerateKeyResponse", "Data"]


class Data(BaseModel):
    allowed_endpoints: Optional[List[str]] = None

    expires_at: Optional[datetime] = None

    key: Optional[str] = None
    """The temporary sandbox API key."""

    requests_remaining: Optional[int] = None

    signup_url: Optional[str] = None


class SandboxGenerateKeyResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    success: Optional[bool] = None
