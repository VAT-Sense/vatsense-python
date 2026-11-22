# Batches: bulk validation through `/batches` (November 2026).

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import batch_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.batch_response import BatchResponse, BatchListResponse, BatchDeleteResponse, BatchResultsResponse

__all__ = ["BatchesResource", "AsyncBatchesResource"]


class BatchesResource(SyncAPIResource):
    """Bulk validation: check many VAT numbers in one batch"""

    @cached_property
    def with_raw_response(self) -> BatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return BatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return BatchesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        numbers: SequenceNotStr[str] | Omit = omit,
        rows: Iterable[batch_create_params.Row] | Omit = omit,
        reference: str | Omit = omit,
        start: bool | Omit = omit,
        shortfall: Literal["wait", "pause", "overage"] | Omit = omit,
        auto_continue: bool | Omit = omit,
        consultation: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """
        Create a batch of VAT numbers and, by default, start checking it.

        Send exactly one of `numbers` or `rows`. Batch calls are free and work even
        when your requests are used up; each number the batch checks counts as one
        request. With a test key the batch is answered from the test numbers, is free
        and holds at most 1,000 numbers.

        Args:
          numbers: The VAT numbers to check, each with its 2-character country code.

          rows: Rows with `vat_number` and, for company matching, any of `country_code`,
              `company_name`, `address`, `street`, `address_line_2`, `postcode` and `city`.

          reference: Your own label for the batch, at most 255 characters.

          start: Defaults to true. False keeps a draft for 24 hours, to start with `start()`.

          shortfall: What to do when your requests do not cover the batch: `wait` (the
              default) starts nothing and returns the `quote`, `pause` checks what is
              covered and pauses the rest, `overage` runs into overage (it must already be
              on in the dashboard).

          auto_continue: Defaults to true. With `pause`, continue when your requests renew.

          consultation: Defaults to false. Send the requester VAT number from your
              account settings with each check.

          idempotency_key: Sent as the `Idempotency-Key` header, at most 64 characters. The
              same key again returns the batch already made.
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/batches",
            body=maybe_transform(
                {
                    "numbers": numbers,
                    "rows": rows,
                    "reference": reference,
                    "start": start,
                    "shortfall": shortfall,
                    "auto_continue": auto_continue,
                    "consultation": consultation,
                },
                batch_create_params.BatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["draft"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """
        List the account's batches, newest first.

        Args:
          page: The page, from 1.

          limit: Batches a page, 1 to 100 (default 25).

          status: `draft` lists the drafts not yet started instead.
        """
        return self._get(
            "/batches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page": page, "limit": limit, "status": status},
                    batch_create_params.BatchListParams,
                ),
            ),
            cast_to=BatchListResponse,
        )

    def retrieve(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """A batch and its progress. Poll until `status` is `complete`, or take the `batch.completed` webhook."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            path_template("/batches/{batch_id}", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    def delete(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchDeleteResponse:
        """Delete a draft. A batch that has started cannot be deleted (409)."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._delete(
            path_template("/batches/{batch_id}", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchDeleteResponse,
        )

    def start(
        self,
        batch_id: str,
        *,
        shortfall: Literal["wait", "pause", "overage"] | Omit = omit,
        auto_continue: bool | Omit = omit,
        consultation: bool | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """Start a draft, with the same options as `create()`."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._post(
            path_template("/batches/{batch_id}/start", batch_id=batch_id),
            body=maybe_transform(
                {"shortfall": shortfall, "auto_continue": auto_continue, "consultation": consultation},
                batch_create_params.BatchStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    def pause(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """Pause a running batch."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._post(
            path_template("/batches/{batch_id}/pause", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    def continue_(
        self,
        batch_id: str,
        *,
        shortfall: Literal["wait", "pause", "overage"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """Continue a paused batch. Send `shortfall="overage"` to run into overage."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._post(
            path_template("/batches/{batch_id}/continue", batch_id=batch_id),
            body=maybe_transform({"shortfall": shortfall}, batch_create_params.BatchContinueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    def complete(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """Mark a paused batch complete, leaving the rest unchecked."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._post(
            path_template("/batches/{batch_id}/complete", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    def results(
        self,
        batch_id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResultsResponse:
        """
        The batch's checked rows as JSON, in row order.

        Args:
          after: Return rows after this row number (default 0). Pass `next_after` from the
              last page while `has_more` is true.

          limit: Rows a page, 1 to 1,000 (default 100).
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            path_template("/batches/{batch_id}/results", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"after": after, "limit": limit}, batch_create_params.BatchResultsParams),
            ),
            cast_to=BatchResultsResponse,
        )

    def results_csv(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """The batch's CSV report, the same file the dashboard gives."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            path_template("/batches/{batch_id}/results.csv", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncBatchesResource(AsyncAPIResource):
    """Bulk validation: check many VAT numbers in one batch"""

    @cached_property
    def with_raw_response(self) -> AsyncBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return AsyncBatchesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        numbers: SequenceNotStr[str] | Omit = omit,
        rows: Iterable[batch_create_params.Row] | Omit = omit,
        reference: str | Omit = omit,
        start: bool | Omit = omit,
        shortfall: Literal["wait", "pause", "overage"] | Omit = omit,
        auto_continue: bool | Omit = omit,
        consultation: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """
        Create a batch of VAT numbers and, by default, start checking it.

        Send exactly one of `numbers` or `rows`. Batch calls are free and work even
        when your requests are used up; each number the batch checks counts as one
        request. With a test key the batch is answered from the test numbers, is free
        and holds at most 1,000 numbers.

        Args:
          numbers: The VAT numbers to check, each with its 2-character country code.

          rows: Rows with `vat_number` and, for company matching, any of `country_code`,
              `company_name`, `address`, `street`, `address_line_2`, `postcode` and `city`.

          reference: Your own label for the batch, at most 255 characters.

          start: Defaults to true. False keeps a draft for 24 hours, to start with `start()`.

          shortfall: What to do when your requests do not cover the batch: `wait` (the
              default) starts nothing and returns the `quote`, `pause` checks what is
              covered and pauses the rest, `overage` runs into overage (it must already be
              on in the dashboard).

          auto_continue: Defaults to true. With `pause`, continue when your requests renew.

          consultation: Defaults to false. Send the requester VAT number from your
              account settings with each check.

          idempotency_key: Sent as the `Idempotency-Key` header, at most 64 characters. The
              same key again returns the batch already made.
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/batches",
            body=await async_maybe_transform(
                {
                    "numbers": numbers,
                    "rows": rows,
                    "reference": reference,
                    "start": start,
                    "shortfall": shortfall,
                    "auto_continue": auto_continue,
                    "consultation": consultation,
                },
                batch_create_params.BatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["draft"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """
        List the account's batches, newest first.

        Args:
          page: The page, from 1.

          limit: Batches a page, 1 to 100 (default 25).

          status: `draft` lists the drafts not yet started instead.
        """
        return await self._get(
            "/batches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page, "limit": limit, "status": status},
                    batch_create_params.BatchListParams,
                ),
            ),
            cast_to=BatchListResponse,
        )

    async def retrieve(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """A batch and its progress. Poll until `status` is `complete`, or take the `batch.completed` webhook."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            path_template("/batches/{batch_id}", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    async def delete(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchDeleteResponse:
        """Delete a draft. A batch that has started cannot be deleted (409)."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._delete(
            path_template("/batches/{batch_id}", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchDeleteResponse,
        )

    async def start(
        self,
        batch_id: str,
        *,
        shortfall: Literal["wait", "pause", "overage"] | Omit = omit,
        auto_continue: bool | Omit = omit,
        consultation: bool | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """Start a draft, with the same options as `create()`."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._post(
            path_template("/batches/{batch_id}/start", batch_id=batch_id),
            body=await async_maybe_transform(
                {"shortfall": shortfall, "auto_continue": auto_continue, "consultation": consultation},
                batch_create_params.BatchStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    async def pause(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """Pause a running batch."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._post(
            path_template("/batches/{batch_id}/pause", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    async def continue_(
        self,
        batch_id: str,
        *,
        shortfall: Literal["wait", "pause", "overage"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """Continue a paused batch. Send `shortfall="overage"` to run into overage."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._post(
            path_template("/batches/{batch_id}/continue", batch_id=batch_id),
            body=await async_maybe_transform({"shortfall": shortfall}, batch_create_params.BatchContinueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    async def complete(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """Mark a paused batch complete, leaving the rest unchecked."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._post(
            path_template("/batches/{batch_id}/complete", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    async def results(
        self,
        batch_id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResultsResponse:
        """
        The batch's checked rows as JSON, in row order.

        Args:
          after: Return rows after this row number (default 0). Pass `next_after` from the
              last page while `has_more` is true.

          limit: Rows a page, 1 to 1,000 (default 100).
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            path_template("/batches/{batch_id}/results", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"after": after, "limit": limit}, batch_create_params.BatchResultsParams
                ),
            ),
            cast_to=BatchResultsResponse,
        )

    async def results_csv(
        self,
        batch_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """The batch's CSV report, the same file the dashboard gives."""
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            path_template("/batches/{batch_id}/results.csv", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class BatchesResourceWithRawResponse:
    def __init__(self, batches: BatchesResource) -> None:
        self._batches = batches

        self.create = to_raw_response_wrapper(
            batches.create,
        )
        self.list = to_raw_response_wrapper(
            batches.list,
        )
        self.retrieve = to_raw_response_wrapper(
            batches.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            batches.delete,
        )
        self.start = to_raw_response_wrapper(
            batches.start,
        )
        self.pause = to_raw_response_wrapper(
            batches.pause,
        )
        self.continue_ = to_raw_response_wrapper(
            batches.continue_,
        )
        self.complete = to_raw_response_wrapper(
            batches.complete,
        )
        self.results = to_raw_response_wrapper(
            batches.results,
        )
        self.results_csv = to_raw_response_wrapper(
            batches.results_csv,
        )


class AsyncBatchesResourceWithRawResponse:
    def __init__(self, batches: AsyncBatchesResource) -> None:
        self._batches = batches

        self.create = async_to_raw_response_wrapper(
            batches.create,
        )
        self.list = async_to_raw_response_wrapper(
            batches.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            batches.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            batches.delete,
        )
        self.start = async_to_raw_response_wrapper(
            batches.start,
        )
        self.pause = async_to_raw_response_wrapper(
            batches.pause,
        )
        self.continue_ = async_to_raw_response_wrapper(
            batches.continue_,
        )
        self.complete = async_to_raw_response_wrapper(
            batches.complete,
        )
        self.results = async_to_raw_response_wrapper(
            batches.results,
        )
        self.results_csv = async_to_raw_response_wrapper(
            batches.results_csv,
        )


class BatchesResourceWithStreamingResponse:
    def __init__(self, batches: BatchesResource) -> None:
        self._batches = batches

        self.create = to_streamed_response_wrapper(
            batches.create,
        )
        self.list = to_streamed_response_wrapper(
            batches.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            batches.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            batches.delete,
        )
        self.start = to_streamed_response_wrapper(
            batches.start,
        )
        self.pause = to_streamed_response_wrapper(
            batches.pause,
        )
        self.continue_ = to_streamed_response_wrapper(
            batches.continue_,
        )
        self.complete = to_streamed_response_wrapper(
            batches.complete,
        )
        self.results = to_streamed_response_wrapper(
            batches.results,
        )
        self.results_csv = to_streamed_response_wrapper(
            batches.results_csv,
        )


class AsyncBatchesResourceWithStreamingResponse:
    def __init__(self, batches: AsyncBatchesResource) -> None:
        self._batches = batches

        self.create = async_to_streamed_response_wrapper(
            batches.create,
        )
        self.list = async_to_streamed_response_wrapper(
            batches.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            batches.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            batches.delete,
        )
        self.start = async_to_streamed_response_wrapper(
            batches.start,
        )
        self.pause = async_to_streamed_response_wrapper(
            batches.pause,
        )
        self.continue_ = async_to_streamed_response_wrapper(
            batches.continue_,
        )
        self.complete = async_to_streamed_response_wrapper(
            batches.complete,
        )
        self.results = async_to_streamed_response_wrapper(
            batches.results,
        )
        self.results_csv = async_to_streamed_response_wrapper(
            batches.results_csv,
        )
