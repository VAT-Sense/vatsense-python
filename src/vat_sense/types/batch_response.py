# Batches (November 2026).

from typing import List, Optional

from .batch import Batch
from .._models import BaseModel
from .batch_result import BatchResult

__all__ = [
    "BatchResponse",
    "BatchListResponse",
    "BatchListData",
    "BatchResultsResponse",
    "BatchResultsData",
    "BatchDeleteResponse",
    "BatchDeleteData",
]


class BatchResponse(BaseModel):
    code: int

    data: Batch

    success: bool


class BatchListData(BaseModel):
    data: List[Batch]

    has_more: bool

    limit: Optional[int] = None

    page: Optional[int] = None

    total: Optional[int] = None


class BatchListResponse(BaseModel):
    code: int

    data: BatchListData

    success: bool


class BatchResultsData(BaseModel):
    data: List[BatchResult]

    has_more: bool

    next_after: Optional[int] = None
    """Pass as `after` for the next page while `has_more` is true."""


class BatchResultsResponse(BaseModel):
    code: int

    data: BatchResultsData

    success: bool


class BatchDeleteData(BaseModel):
    id: str

    deleted: bool

    object: Optional[str] = None


class BatchDeleteResponse(BaseModel):
    code: int

    data: BatchDeleteData

    success: bool
