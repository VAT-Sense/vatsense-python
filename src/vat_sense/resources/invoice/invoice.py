# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .item import (
    ItemResource,
    AsyncItemResource,
    ItemResourceWithRawResponse,
    AsyncItemResourceWithRawResponse,
    ItemResourceWithStreamingResponse,
    AsyncItemResourceWithStreamingResponse,
)
from ...types import (
    invoice_list_params,
    invoice_create_params,
    invoice_update_params,
)
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
from ...types.invoice_response import InvoiceResponse
from ...types.invoice_list_response import InvoiceListResponse
from ...types.invoice_delete_response import InvoiceDeleteResponse
from ...types.invoice_business_input_param import InvoiceBusinessInputParam
from ...types.invoice_customer_input_param import InvoiceCustomerInputParam
from ...types.invoice_conversion_input_param import InvoiceConversionInputParam
from ...types.invoice.invoice_item_input_param import InvoiceItemInputParam

__all__ = ["InvoiceResource", "AsyncInvoiceResource"]


class InvoiceResource(SyncAPIResource):
    """VAT-compliant invoice management"""

    @cached_property
    def item(self) -> ItemResource:
        """VAT-compliant invoice management"""
        return ItemResource(self._client)

    @cached_property
    def with_raw_response(self) -> InvoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return InvoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return InvoiceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business: InvoiceBusinessInputParam,
        currency_code: str,
        date: str,
        items: Iterable[InvoiceItemInputParam],
        tax_point: str,
        conversion: InvoiceConversionInputParam | Omit = omit,
        customer: InvoiceCustomerInputParam | Omit = omit,
        has_vat: bool | Omit = omit,
        invoice_number: str | Omit = omit,
        is_copy: bool | Omit = omit,
        is_reverse_charge: bool | Omit = omit,
        notes: str | Omit = omit,
        pad_invoice_number: int | Omit = omit,
        serial: str | Omit = omit,
        tax_type: Literal["incl", "excl"] | Omit = omit,
        type: Literal["sale", "refund"] | Omit = omit,
        zero_rated: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """Create a new VAT-compliant invoice.

        VAT Sense will automatically calculate the
        totals based on the items provided.

        Not available with sandbox API keys.

        Args:
          currency_code: The 3-character currency code the invoice is billed in.

          date: The date the invoice was issued (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS).

          tax_point: The tax point or "time of supply" (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS).

          has_vat: Whether the invoice is subject to VAT.

          invoice_number: A unique invoice number. If not provided, defaults to an auto-incremented
              number.

          is_copy: Whether the invoice is a copy of a primary invoice.

          is_reverse_charge: Whether the invoice is zero-rated due to reverse charge.

          notes: Any additional notes for the invoice.

          pad_invoice_number: Pad the auto-generated invoice number with leading zeros to this length.

          serial: A serial prepended to the auto-generated invoice number. Each unique serial has
              its own auto-increment range.

          tax_type: Whether item prices include or exclude VAT.

          type: The type of invoice.

          zero_rated: Whether the invoice has been zero-rated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/invoice",
            body=maybe_transform(
                {
                    "business": business,
                    "currency_code": currency_code,
                    "date": date,
                    "items": items,
                    "tax_point": tax_point,
                    "conversion": conversion,
                    "customer": customer,
                    "has_vat": has_vat,
                    "invoice_number": invoice_number,
                    "is_copy": is_copy,
                    "is_reverse_charge": is_reverse_charge,
                    "notes": notes,
                    "pad_invoice_number": pad_invoice_number,
                    "serial": serial,
                    "tax_type": tax_type,
                    "type": type,
                    "zero_rated": zero_rated,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    def retrieve(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """
        Retrieve a specific invoice by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._get(
            f"/invoice/{invoice_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    def update(
        self,
        invoice_id: str,
        *,
        business: InvoiceBusinessInputParam,
        currency_code: str,
        date: str,
        items: Iterable[InvoiceItemInputParam],
        tax_point: str,
        conversion: InvoiceConversionInputParam | Omit = omit,
        customer: InvoiceCustomerInputParam | Omit = omit,
        has_vat: bool | Omit = omit,
        invoice_number: str | Omit = omit,
        is_copy: bool | Omit = omit,
        is_reverse_charge: bool | Omit = omit,
        notes: str | Omit = omit,
        pad_invoice_number: int | Omit = omit,
        serial: str | Omit = omit,
        tax_type: Literal["incl", "excl"] | Omit = omit,
        type: Literal["sale", "refund"] | Omit = omit,
        zero_rated: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """Update an existing invoice.

        Only the fields provided will be updated.

        Args:
          currency_code: The 3-character currency code the invoice is billed in.

          date: The date the invoice was issued (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS).

          tax_point: The tax point or "time of supply" (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS).

          has_vat: Whether the invoice is subject to VAT.

          invoice_number: A unique invoice number. If not provided, defaults to an auto-incremented
              number.

          is_copy: Whether the invoice is a copy of a primary invoice.

          is_reverse_charge: Whether the invoice is zero-rated due to reverse charge.

          notes: Any additional notes for the invoice.

          pad_invoice_number: Pad the auto-generated invoice number with leading zeros to this length.

          serial: A serial prepended to the auto-generated invoice number. Each unique serial has
              its own auto-increment range.

          tax_type: Whether item prices include or exclude VAT.

          type: The type of invoice.

          zero_rated: Whether the invoice has been zero-rated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._patch(
            f"/invoice/{invoice_id}",
            body=maybe_transform(
                {
                    "business": business,
                    "currency_code": currency_code,
                    "date": date,
                    "items": items,
                    "tax_point": tax_point,
                    "conversion": conversion,
                    "customer": customer,
                    "has_vat": has_vat,
                    "invoice_number": invoice_number,
                    "is_copy": is_copy,
                    "is_reverse_charge": is_reverse_charge,
                    "notes": notes,
                    "pad_invoice_number": pad_invoice_number,
                    "serial": serial,
                    "tax_type": tax_type,
                    "type": type,
                    "zero_rated": zero_rated,
                },
                invoice_update_params.InvoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceListResponse:
        """
        Retrieve a paginated list of all invoices.

        Args:
          limit: Number of invoices to return (default 10, max 100).

          offset: Number of invoices to skip (default 0).

          search: Search query to filter invoices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/invoice",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            cast_to=InvoiceListResponse,
        )

    def delete(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceDeleteResponse:
        """
        Permanently delete an invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._delete(
            f"/invoice/{invoice_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceDeleteResponse,
        )


class AsyncInvoiceResource(AsyncAPIResource):
    """VAT-compliant invoice management"""

    @cached_property
    def item(self) -> AsyncItemResource:
        """VAT-compliant invoice management"""
        return AsyncItemResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInvoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return AsyncInvoiceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business: InvoiceBusinessInputParam,
        currency_code: str,
        date: str,
        items: Iterable[InvoiceItemInputParam],
        tax_point: str,
        conversion: InvoiceConversionInputParam | Omit = omit,
        customer: InvoiceCustomerInputParam | Omit = omit,
        has_vat: bool | Omit = omit,
        invoice_number: str | Omit = omit,
        is_copy: bool | Omit = omit,
        is_reverse_charge: bool | Omit = omit,
        notes: str | Omit = omit,
        pad_invoice_number: int | Omit = omit,
        serial: str | Omit = omit,
        tax_type: Literal["incl", "excl"] | Omit = omit,
        type: Literal["sale", "refund"] | Omit = omit,
        zero_rated: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """Create a new VAT-compliant invoice.

        VAT Sense will automatically calculate the
        totals based on the items provided.

        Not available with sandbox API keys.

        Args:
          currency_code: The 3-character currency code the invoice is billed in.

          date: The date the invoice was issued (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS).

          tax_point: The tax point or "time of supply" (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS).

          has_vat: Whether the invoice is subject to VAT.

          invoice_number: A unique invoice number. If not provided, defaults to an auto-incremented
              number.

          is_copy: Whether the invoice is a copy of a primary invoice.

          is_reverse_charge: Whether the invoice is zero-rated due to reverse charge.

          notes: Any additional notes for the invoice.

          pad_invoice_number: Pad the auto-generated invoice number with leading zeros to this length.

          serial: A serial prepended to the auto-generated invoice number. Each unique serial has
              its own auto-increment range.

          tax_type: Whether item prices include or exclude VAT.

          type: The type of invoice.

          zero_rated: Whether the invoice has been zero-rated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/invoice",
            body=await async_maybe_transform(
                {
                    "business": business,
                    "currency_code": currency_code,
                    "date": date,
                    "items": items,
                    "tax_point": tax_point,
                    "conversion": conversion,
                    "customer": customer,
                    "has_vat": has_vat,
                    "invoice_number": invoice_number,
                    "is_copy": is_copy,
                    "is_reverse_charge": is_reverse_charge,
                    "notes": notes,
                    "pad_invoice_number": pad_invoice_number,
                    "serial": serial,
                    "tax_type": tax_type,
                    "type": type,
                    "zero_rated": zero_rated,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    async def retrieve(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """
        Retrieve a specific invoice by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._get(
            f"/invoice/{invoice_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    async def update(
        self,
        invoice_id: str,
        *,
        business: InvoiceBusinessInputParam,
        currency_code: str,
        date: str,
        items: Iterable[InvoiceItemInputParam],
        tax_point: str,
        conversion: InvoiceConversionInputParam | Omit = omit,
        customer: InvoiceCustomerInputParam | Omit = omit,
        has_vat: bool | Omit = omit,
        invoice_number: str | Omit = omit,
        is_copy: bool | Omit = omit,
        is_reverse_charge: bool | Omit = omit,
        notes: str | Omit = omit,
        pad_invoice_number: int | Omit = omit,
        serial: str | Omit = omit,
        tax_type: Literal["incl", "excl"] | Omit = omit,
        type: Literal["sale", "refund"] | Omit = omit,
        zero_rated: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceResponse:
        """Update an existing invoice.

        Only the fields provided will be updated.

        Args:
          currency_code: The 3-character currency code the invoice is billed in.

          date: The date the invoice was issued (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS).

          tax_point: The tax point or "time of supply" (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS).

          has_vat: Whether the invoice is subject to VAT.

          invoice_number: A unique invoice number. If not provided, defaults to an auto-incremented
              number.

          is_copy: Whether the invoice is a copy of a primary invoice.

          is_reverse_charge: Whether the invoice is zero-rated due to reverse charge.

          notes: Any additional notes for the invoice.

          pad_invoice_number: Pad the auto-generated invoice number with leading zeros to this length.

          serial: A serial prepended to the auto-generated invoice number. Each unique serial has
              its own auto-increment range.

          tax_type: Whether item prices include or exclude VAT.

          type: The type of invoice.

          zero_rated: Whether the invoice has been zero-rated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._patch(
            f"/invoice/{invoice_id}",
            body=await async_maybe_transform(
                {
                    "business": business,
                    "currency_code": currency_code,
                    "date": date,
                    "items": items,
                    "tax_point": tax_point,
                    "conversion": conversion,
                    "customer": customer,
                    "has_vat": has_vat,
                    "invoice_number": invoice_number,
                    "is_copy": is_copy,
                    "is_reverse_charge": is_reverse_charge,
                    "notes": notes,
                    "pad_invoice_number": pad_invoice_number,
                    "serial": serial,
                    "tax_type": tax_type,
                    "type": type,
                    "zero_rated": zero_rated,
                },
                invoice_update_params.InvoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceListResponse:
        """
        Retrieve a paginated list of all invoices.

        Args:
          limit: Number of invoices to return (default 10, max 100).

          offset: Number of invoices to skip (default 0).

          search: Search query to filter invoices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/invoice",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            cast_to=InvoiceListResponse,
        )

    async def delete(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceDeleteResponse:
        """
        Permanently delete an invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._delete(
            f"/invoice/{invoice_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceDeleteResponse,
        )


class InvoiceResourceWithRawResponse:
    def __init__(self, invoice: InvoiceResource) -> None:
        self._invoice = invoice

        self.create = to_raw_response_wrapper(
            invoice.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invoice.retrieve,
        )
        self.update = to_raw_response_wrapper(
            invoice.update,
        )
        self.list = to_raw_response_wrapper(
            invoice.list,
        )
        self.delete = to_raw_response_wrapper(
            invoice.delete,
        )

    @cached_property
    def item(self) -> ItemResourceWithRawResponse:
        """VAT-compliant invoice management"""
        return ItemResourceWithRawResponse(self._invoice.item)


class AsyncInvoiceResourceWithRawResponse:
    def __init__(self, invoice: AsyncInvoiceResource) -> None:
        self._invoice = invoice

        self.create = async_to_raw_response_wrapper(
            invoice.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invoice.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            invoice.update,
        )
        self.list = async_to_raw_response_wrapper(
            invoice.list,
        )
        self.delete = async_to_raw_response_wrapper(
            invoice.delete,
        )

    @cached_property
    def item(self) -> AsyncItemResourceWithRawResponse:
        """VAT-compliant invoice management"""
        return AsyncItemResourceWithRawResponse(self._invoice.item)


class InvoiceResourceWithStreamingResponse:
    def __init__(self, invoice: InvoiceResource) -> None:
        self._invoice = invoice

        self.create = to_streamed_response_wrapper(
            invoice.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invoice.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            invoice.update,
        )
        self.list = to_streamed_response_wrapper(
            invoice.list,
        )
        self.delete = to_streamed_response_wrapper(
            invoice.delete,
        )

    @cached_property
    def item(self) -> ItemResourceWithStreamingResponse:
        """VAT-compliant invoice management"""
        return ItemResourceWithStreamingResponse(self._invoice.item)


class AsyncInvoiceResourceWithStreamingResponse:
    def __init__(self, invoice: AsyncInvoiceResource) -> None:
        self._invoice = invoice

        self.create = async_to_streamed_response_wrapper(
            invoice.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invoice.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            invoice.update,
        )
        self.list = async_to_streamed_response_wrapper(
            invoice.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            invoice.delete,
        )

    @cached_property
    def item(self) -> AsyncItemResourceWithStreamingResponse:
        """VAT-compliant invoice management"""
        return AsyncItemResourceWithStreamingResponse(self._invoice.item)
