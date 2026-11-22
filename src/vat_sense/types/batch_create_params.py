# Batches (November 2026).

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "BatchCreateParams",
    "Row",
    "BatchStartParams",
    "BatchContinueParams",
    "BatchListParams",
    "BatchResultsParams",
]


class Row(TypedDict, total=False):
    vat_number: Required[str]

    address: str

    address_line_2: str

    city: str

    company_name: str

    country_code: str

    postcode: str

    street: str


class BatchCreateParams(TypedDict, total=False):
    numbers: SequenceNotStr[str]

    rows: Iterable[Row]

    reference: str

    start: bool

    shortfall: Literal["wait", "pause", "overage"]

    auto_continue: bool

    consultation: bool


class BatchStartParams(TypedDict, total=False):
    shortfall: Literal["wait", "pause", "overage"]

    auto_continue: bool

    consultation: bool


class BatchContinueParams(TypedDict, total=False):
    shortfall: Literal["wait", "pause", "overage"]


class BatchListParams(TypedDict, total=False):
    limit: int

    page: int

    status: Literal["draft"]


class BatchResultsParams(TypedDict, total=False):
    after: int

    limit: int
