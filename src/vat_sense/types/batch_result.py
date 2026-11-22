# Batches: one checked row of a batch (November 2026).

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["BatchResult", "BatchResultMatch", "BatchResultMatchFields"]


class BatchResultMatchFields(BaseModel):
    result: Optional[str] = None
    """`match`, `partial`, `no_match` or `not_applicable`."""

    score: Optional[int] = None

    sent: Optional[str] = None
    """The detail as it was sent."""

    vies: Optional[str] = None


class BatchResultMatch(BaseModel):
    fields: Optional[Dict[str, BatchResultMatchFields]] = None

    result: Optional[str] = None
    """`likely`, `possible`, `unlikely` or `not_applicable`."""

    score: Optional[int] = None


class BatchResult(BaseModel):
    row: int

    authority: Optional[str] = None

    checked_at: Optional[str] = None

    company_address: Optional[str] = None

    company_name: Optional[str] = None

    confirmation_number: Optional[str] = None

    consultation_number: Optional[str] = None

    country_code: Optional[str] = None

    country_uploaded: Optional[str] = None

    duplicate_of_row: Optional[int] = None

    match: Optional[BatchResultMatch] = None

    reason: Optional[str] = None

    repaired: Optional[bool] = None

    result: Optional[str] = None
    """The row's answer, such as `valid` or `invalid`; `pending` while it is being checked."""

    vat_number: Optional[str] = None
    """The number as it was checked."""

    vat_number_uploaded: Optional[str] = None
