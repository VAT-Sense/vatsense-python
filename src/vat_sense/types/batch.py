# Batches: bulk validation through `/batches` (November 2026).

from typing import Optional

from .._models import BaseModel

__all__ = ["Batch", "BatchRows", "BatchResults", "BatchQuote"]


class BatchRows(BaseModel):
    done: Optional[int] = None
    """Rows checked so far."""

    to_check: Optional[int] = None
    """Rows that will be sent for checking (duplicates and unsupported rows are not)."""

    total: Optional[int] = None
    """Rows in the batch."""


class BatchResults(BaseModel):
    duplicate: Optional[int] = None

    invalid: Optional[int] = None

    not_checked: Optional[int] = None

    repaired: Optional[int] = None

    retrying: Optional[int] = None

    unsupported: Optional[int] = None

    valid: Optional[int] = None


class BatchQuote(BaseModel):
    covered: Optional[bool] = None
    """Whether the requests left cover the batch."""

    overage_on: Optional[bool] = None

    renews_at: Optional[str] = None

    requests_left: Optional[int] = None

    requests_needed: Optional[int] = None

    shortfall: Optional[int] = None


class Batch(BaseModel):
    id: str
    """The batch's 26-character id."""

    object: Optional[str] = None
    """Always `batch`."""

    auto_continue: Optional[bool] = None

    consultation: Optional[bool] = None

    created_at: Optional[str] = None
    """UTC, ISO 8601, as are all the times."""

    dashboard_url: Optional[str] = None
    """The batch's page in the dashboard; null for a test batch."""

    estimated_finish_at: Optional[str] = None

    expires_at: Optional[str] = None

    finished_at: Optional[str] = None

    livemode: Optional[bool] = None
    """False for a test batch, made with a test key."""

    number: Optional[int] = None

    pause_reason: Optional[str] = None

    quote: Optional[BatchQuote] = None
    """For drafts and paused batches."""

    reference: Optional[str] = None

    requests_used: Optional[int] = None

    results: Optional[BatchResults] = None

    rows: Optional[BatchRows] = None

    source: Optional[str] = None

    started_at: Optional[str] = None

    status: Optional[str] = None
    """`draft`, `queued`, `processing`, `paused`, `complete` or `expired`."""

    trial: Optional[bool] = None

    uses_overage: Optional[bool] = None
