# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import currency_list_params, currency_convert_params, currency_calculate_vat_price_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.currency_list_response import CurrencyListResponse
from ..types.currency_convert_response import CurrencyConvertResponse
from ..types.currency_calculate_vat_price_response import CurrencyCalculateVatPriceResponse

__all__ = ["CurrencyResource", "AsyncCurrencyResource"]


class CurrencyResource(SyncAPIResource):
    """Currency exchange rates and conversion"""

    @cached_property
    def with_raw_response(self) -> CurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return CurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return CurrencyResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        from_: str | Omit = omit,
        to: Literal["GBP", "EUR"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyListResponse:
        """
        Returns a list of all currency conversion rates sourced from HMRC (GBP) and the
        European Central Bank (EUR).

        You can optionally filter by source and target currency.

        Args:
          from_: The 3-character currency code(s) to convert from (e.g. "USD", "CAD"). Can be a
              comma-separated list without spaces (e.g. "USD,CAD,AUD").

          to: The 3-character target currency code. Must be either "GBP" or "EUR".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/currency",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    currency_list_params.CurrencyListParams,
                ),
            ),
            cast_to=CurrencyListResponse,
        )

    def calculate_vat_price(
        self,
        *,
        price: float,
        tax_type: Literal["incl", "excl"],
        vat_rate: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyCalculateVatPriceResponse:
        """
        Calculate the inclusive and exclusive VAT price on a given amount and VAT rate.
        This is a standalone calculation that does not look up rates by country.

        Args:
          price: The price to calculate on. Must be a decimal with 2 decimal places.

          tax_type: Whether the provided price is inclusive or exclusive of VAT.

          vat_rate: A percentage VAT rate to use for the calculation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/currency/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "price": price,
                        "tax_type": tax_type,
                        "vat_rate": vat_rate,
                    },
                    currency_calculate_vat_price_params.CurrencyCalculateVatPriceParams,
                ),
            ),
            cast_to=CurrencyCalculateVatPriceResponse,
        )

    def convert(
        self,
        *,
        amount: float,
        from_: str,
        to: Literal["GBP", "EUR"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyConvertResponse:
        """
        Convert a foreign currency amount to either GBP or EUR using official exchange
        rates.

        GBP rates are from HMRC (updated on the 1st of every month). EUR rates are from
        the European Central Bank (updated around 16:00 CET on working days).

        Args:
          amount: The amount to convert. Must be a decimal with 2 decimal places (e.g. "39.99").

          from_: The 3-character source currency code (e.g. "USD", "CAD").

          to: The 3-character target currency code. Must be either "GBP" or "EUR".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/currency/convert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "amount": amount,
                        "from_": from_,
                        "to": to,
                    },
                    currency_convert_params.CurrencyConvertParams,
                ),
            ),
            cast_to=CurrencyConvertResponse,
        )


class AsyncCurrencyResource(AsyncAPIResource):
    """Currency exchange rates and conversion"""

    @cached_property
    def with_raw_response(self) -> AsyncCurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return AsyncCurrencyResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        from_: str | Omit = omit,
        to: Literal["GBP", "EUR"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyListResponse:
        """
        Returns a list of all currency conversion rates sourced from HMRC (GBP) and the
        European Central Bank (EUR).

        You can optionally filter by source and target currency.

        Args:
          from_: The 3-character currency code(s) to convert from (e.g. "USD", "CAD"). Can be a
              comma-separated list without spaces (e.g. "USD,CAD,AUD").

          to: The 3-character target currency code. Must be either "GBP" or "EUR".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/currency",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    currency_list_params.CurrencyListParams,
                ),
            ),
            cast_to=CurrencyListResponse,
        )

    async def calculate_vat_price(
        self,
        *,
        price: float,
        tax_type: Literal["incl", "excl"],
        vat_rate: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyCalculateVatPriceResponse:
        """
        Calculate the inclusive and exclusive VAT price on a given amount and VAT rate.
        This is a standalone calculation that does not look up rates by country.

        Args:
          price: The price to calculate on. Must be a decimal with 2 decimal places.

          tax_type: Whether the provided price is inclusive or exclusive of VAT.

          vat_rate: A percentage VAT rate to use for the calculation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/currency/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "price": price,
                        "tax_type": tax_type,
                        "vat_rate": vat_rate,
                    },
                    currency_calculate_vat_price_params.CurrencyCalculateVatPriceParams,
                ),
            ),
            cast_to=CurrencyCalculateVatPriceResponse,
        )

    async def convert(
        self,
        *,
        amount: float,
        from_: str,
        to: Literal["GBP", "EUR"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyConvertResponse:
        """
        Convert a foreign currency amount to either GBP or EUR using official exchange
        rates.

        GBP rates are from HMRC (updated on the 1st of every month). EUR rates are from
        the European Central Bank (updated around 16:00 CET on working days).

        Args:
          amount: The amount to convert. Must be a decimal with 2 decimal places (e.g. "39.99").

          from_: The 3-character source currency code (e.g. "USD", "CAD").

          to: The 3-character target currency code. Must be either "GBP" or "EUR".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/currency/convert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "amount": amount,
                        "from_": from_,
                        "to": to,
                    },
                    currency_convert_params.CurrencyConvertParams,
                ),
            ),
            cast_to=CurrencyConvertResponse,
        )


class CurrencyResourceWithRawResponse:
    def __init__(self, currency: CurrencyResource) -> None:
        self._currency = currency

        self.list = to_raw_response_wrapper(
            currency.list,
        )
        self.calculate_vat_price = to_raw_response_wrapper(
            currency.calculate_vat_price,
        )
        self.convert = to_raw_response_wrapper(
            currency.convert,
        )


class AsyncCurrencyResourceWithRawResponse:
    def __init__(self, currency: AsyncCurrencyResource) -> None:
        self._currency = currency

        self.list = async_to_raw_response_wrapper(
            currency.list,
        )
        self.calculate_vat_price = async_to_raw_response_wrapper(
            currency.calculate_vat_price,
        )
        self.convert = async_to_raw_response_wrapper(
            currency.convert,
        )


class CurrencyResourceWithStreamingResponse:
    def __init__(self, currency: CurrencyResource) -> None:
        self._currency = currency

        self.list = to_streamed_response_wrapper(
            currency.list,
        )
        self.calculate_vat_price = to_streamed_response_wrapper(
            currency.calculate_vat_price,
        )
        self.convert = to_streamed_response_wrapper(
            currency.convert,
        )


class AsyncCurrencyResourceWithStreamingResponse:
    def __init__(self, currency: AsyncCurrencyResource) -> None:
        self._currency = currency

        self.list = async_to_streamed_response_wrapper(
            currency.list,
        )
        self.calculate_vat_price = async_to_streamed_response_wrapper(
            currency.calculate_vat_price,
        )
        self.convert = async_to_streamed_response_wrapper(
            currency.convert,
        )
