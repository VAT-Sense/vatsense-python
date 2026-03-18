# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.invoice import item_add_params, item_update_params
from ...types.invoice_response import InvoiceResponse
from ...types.invoice.item_retrieve_response import ItemRetrieveResponse
from ...types.invoice.invoice_item_input_param import InvoiceItemInputParam

__all__ = ["ItemResource", "AsyncItemResource"]


class ItemResource(SyncAPIResource):
    """VAT-compliant invoice management"""

    @cached_property
    def with_raw_response(self) -> ItemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return ItemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return ItemResourceWithStreamingResponse(self)

    def retrieve(
        self,
        item_id: str,
        *,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemRetrieveResponse:
        """
        Retrieve a specific line item from an invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            f"/invoice/{invoice_id}/item/{item_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemRetrieveResponse,
        )

    def update(
        self,
        item_id: str,
        *,
        invoice_id: str,
        item: str,
        price_each: float,
        quantity: float,
        vat_rate: float,
        discount_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """
        Update a specific line item on an invoice.

        Args:
          item: The description of the line item.

          price_each: The price per item. Must be a decimal with 2 decimal places.

          quantity: The quantity of the item.

          vat_rate: A percentage VAT rate for this item.

          discount_rate: A percentage discount to apply to the price.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._patch(
            f"/invoice/{invoice_id}/item/{item_id}",
            body=maybe_transform(
                {
                    "item": item,
                    "price_each": price_each,
                    "quantity": quantity,
                    "vat_rate": vat_rate,
                    "discount_rate": discount_rate,
                },
                item_update_params.ItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    def delete(
        self,
        item_id: str,
        *,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """
        Remove a specific line item from an invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._delete(
            f"/invoice/{invoice_id}/item/{item_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    def add(
        self,
        invoice_id: str,
        *,
        items: Iterable[InvoiceItemInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """
        Add one or more line items to an existing invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._post(
            f"/invoice/{invoice_id}/item",
            body=maybe_transform({"items": items}, item_add_params.ItemAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )


class AsyncItemResource(AsyncAPIResource):
    """VAT-compliant invoice management"""

    @cached_property
    def with_raw_response(self) -> AsyncItemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return AsyncItemResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        item_id: str,
        *,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemRetrieveResponse:
        """
        Retrieve a specific line item from an invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            f"/invoice/{invoice_id}/item/{item_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemRetrieveResponse,
        )

    async def update(
        self,
        item_id: str,
        *,
        invoice_id: str,
        item: str,
        price_each: float,
        quantity: float,
        vat_rate: float,
        discount_rate: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """
        Update a specific line item on an invoice.

        Args:
          item: The description of the line item.

          price_each: The price per item. Must be a decimal with 2 decimal places.

          quantity: The quantity of the item.

          vat_rate: A percentage VAT rate for this item.

          discount_rate: A percentage discount to apply to the price.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._patch(
            f"/invoice/{invoice_id}/item/{item_id}",
            body=await async_maybe_transform(
                {
                    "item": item,
                    "price_each": price_each,
                    "quantity": quantity,
                    "vat_rate": vat_rate,
                    "discount_rate": discount_rate,
                },
                item_update_params.ItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    async def delete(
        self,
        item_id: str,
        *,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """
        Remove a specific line item from an invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._delete(
            f"/invoice/{invoice_id}/item/{item_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    async def add(
        self,
        invoice_id: str,
        *,
        items: Iterable[InvoiceItemInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """
        Add one or more line items to an existing invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._post(
            f"/invoice/{invoice_id}/item",
            body=await async_maybe_transform({"items": items}, item_add_params.ItemAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )


class ItemResourceWithRawResponse:
    def __init__(self, item: ItemResource) -> None:
        self._item = item

        self.retrieve = to_raw_response_wrapper(
            item.retrieve,
        )
        self.update = to_raw_response_wrapper(
            item.update,
        )
        self.delete = to_raw_response_wrapper(
            item.delete,
        )
        self.add = to_raw_response_wrapper(
            item.add,
        )


class AsyncItemResourceWithRawResponse:
    def __init__(self, item: AsyncItemResource) -> None:
        self._item = item

        self.retrieve = async_to_raw_response_wrapper(
            item.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            item.update,
        )
        self.delete = async_to_raw_response_wrapper(
            item.delete,
        )
        self.add = async_to_raw_response_wrapper(
            item.add,
        )


class ItemResourceWithStreamingResponse:
    def __init__(self, item: ItemResource) -> None:
        self._item = item

        self.retrieve = to_streamed_response_wrapper(
            item.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            item.update,
        )
        self.delete = to_streamed_response_wrapper(
            item.delete,
        )
        self.add = to_streamed_response_wrapper(
            item.add,
        )


class AsyncItemResourceWithStreamingResponse:
    def __init__(self, item: AsyncItemResource) -> None:
        self._item = item

        self.retrieve = async_to_streamed_response_wrapper(
            item.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            item.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            item.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            item.add,
        )
