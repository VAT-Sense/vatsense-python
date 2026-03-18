# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import rate_find_params, rate_list_params, rate_details_params, rate_calculate_price_params
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
from ..types.find_rate import FindRate
from ..types.rate_list_response import RateListResponse
from ..types.rate_list_types_response import RateListTypesResponse
from ..types.rate_calculate_price_response import RateCalculatePriceResponse

__all__ = ["RatesResource", "AsyncRatesResource"]


class RatesResource(SyncAPIResource):
    """VAT/GST rate lookups for countries worldwide"""

    @cached_property
    def with_raw_response(self) -> RatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return RatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return RatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        country_code: str | Omit = omit,
        eu: bool | Omit = omit,
        ip_address: str | Omit = omit,
        period: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RateListResponse:
        """
        Returns a list of VAT/GST rates for all countries, sorted alphabetically by
        country code. Each rate is returned as a rate object containing the standard
        rate and any other applicable rates.

        You can optionally filter by country code, IP address, or EU membership.

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          eu: Filter results by EU membership. Use 1 for EU countries only, 0 for non-EU only.

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          period: A historical date to retrieve rates for (format "YYYY-MM-DD HH:MM:SS"). Must be
              a past date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country_code": country_code,
                        "eu": eu,
                        "ip_address": ip_address,
                        "period": period,
                    },
                    rate_list_params.RateListParams,
                ),
            ),
            cast_to=RateListResponse,
        )

    def calculate_price(
        self,
        *,
        price: float,
        tax_type: Literal["incl", "excl"],
        country_code: str | Omit = omit,
        eu: bool | Omit = omit,
        ip_address: str | Omit = omit,
        province_code: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RateCalculatePriceResponse:
        """
        Combines the functionality of the "Find a tax rate" and "VAT price calculation"
        endpoints to return the particular VAT price for an applicable VAT rate.
        Requires both a location (country_code or ip_address) and a price to calculate.

        Args:
          price: The price to calculate on. Must be a decimal with 2 decimal places (e.g.
              "30.00", "59.95").

          tax_type: Whether the provided price is inclusive or exclusive of VAT.

          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          eu: Filter results by EU membership. Use 1 for EU countries only, 0 for non-EU only.

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          province_code: A 2-character province code (e.g. "NU", "NT"). If providing a province code, you
              must also provide the relevant country_code.

          type: The product type to find the applicable rate for. See the /rates/types endpoint
              for a full list of valid values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rates/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "price": price,
                        "tax_type": tax_type,
                        "country_code": country_code,
                        "eu": eu,
                        "ip_address": ip_address,
                        "province_code": province_code,
                        "type": type,
                    },
                    rate_calculate_price_params.RateCalculatePriceParams,
                ),
            ),
            cast_to=RateCalculatePriceResponse,
        )

    def details(
        self,
        *,
        country_code: str | Omit = omit,
        eu: bool | Omit = omit,
        ip_address: str | Omit = omit,
        period: Union[str, datetime] | Omit = omit,
        province_code: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRate:
        """
        Get detailed tax rate information for a location, including all applicable rate
        classes (standard, reduced, zero, etc.).

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          eu: Filter results by EU membership. Use 1 for EU countries only, 0 for non-EU only.

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          period: A historical date to retrieve rates for (format "YYYY-MM-DD HH:MM:SS"). Must be
              a past date.

          province_code: A 2-character province code (e.g. "NU", "NT"). If providing a province code, you
              must also provide the relevant country_code.

          type: The product type to find the applicable rate for. See the /rates/types endpoint
              for a full list of valid values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rates/tax_rate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country_code": country_code,
                        "eu": eu,
                        "ip_address": ip_address,
                        "period": period,
                        "province_code": province_code,
                        "type": type,
                    },
                    rate_details_params.RateDetailsParams,
                ),
            ),
            cast_to=FindRate,
        )

    def find(
        self,
        *,
        country_code: str | Omit = omit,
        eu: bool | Omit = omit,
        ip_address: str | Omit = omit,
        period: Union[str, datetime] | Omit = omit,
        province_code: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRate:
        """
        A handy endpoint for finding a rate that applies to a particular country and
        optional product type, based on country code or IP address.

        If no type is provided, or no specific rate is applied to the given type, then
        the standard rate will be returned if the country is subject to tax.

        If the country is not subject to VAT/GST then an error response will be
        returned, indicating no tax applies.

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          eu: Filter results by EU membership. Use 1 for EU countries only, 0 for non-EU only.

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          period: A historical date to retrieve rates for (format "YYYY-MM-DD HH:MM:SS"). Must be
              a past date.

          province_code: A 2-character province code (e.g. "NU", "NT"). If providing a province code, you
              must also provide the relevant country_code.

          type: The product type to find the applicable rate for. See the /rates/types endpoint
              for a full list of valid values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rates/rate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country_code": country_code,
                        "eu": eu,
                        "ip_address": ip_address,
                        "period": period,
                        "province_code": province_code,
                        "type": type,
                    },
                    rate_find_params.RateFindParams,
                ),
            ),
            cast_to=FindRate,
        )

    def list_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RateListTypesResponse:
        """
        Returns a list of all available product types that can be used to filter tax
        rates.
        """
        return self._get(
            "/rates/types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateListTypesResponse,
        )


class AsyncRatesResource(AsyncAPIResource):
    """VAT/GST rate lookups for countries worldwide"""

    @cached_property
    def with_raw_response(self) -> AsyncRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return AsyncRatesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        country_code: str | Omit = omit,
        eu: bool | Omit = omit,
        ip_address: str | Omit = omit,
        period: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RateListResponse:
        """
        Returns a list of VAT/GST rates for all countries, sorted alphabetically by
        country code. Each rate is returned as a rate object containing the standard
        rate and any other applicable rates.

        You can optionally filter by country code, IP address, or EU membership.

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          eu: Filter results by EU membership. Use 1 for EU countries only, 0 for non-EU only.

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          period: A historical date to retrieve rates for (format "YYYY-MM-DD HH:MM:SS"). Must be
              a past date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country_code": country_code,
                        "eu": eu,
                        "ip_address": ip_address,
                        "period": period,
                    },
                    rate_list_params.RateListParams,
                ),
            ),
            cast_to=RateListResponse,
        )

    async def calculate_price(
        self,
        *,
        price: float,
        tax_type: Literal["incl", "excl"],
        country_code: str | Omit = omit,
        eu: bool | Omit = omit,
        ip_address: str | Omit = omit,
        province_code: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RateCalculatePriceResponse:
        """
        Combines the functionality of the "Find a tax rate" and "VAT price calculation"
        endpoints to return the particular VAT price for an applicable VAT rate.
        Requires both a location (country_code or ip_address) and a price to calculate.

        Args:
          price: The price to calculate on. Must be a decimal with 2 decimal places (e.g.
              "30.00", "59.95").

          tax_type: Whether the provided price is inclusive or exclusive of VAT.

          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          eu: Filter results by EU membership. Use 1 for EU countries only, 0 for non-EU only.

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          province_code: A 2-character province code (e.g. "NU", "NT"). If providing a province code, you
              must also provide the relevant country_code.

          type: The product type to find the applicable rate for. See the /rates/types endpoint
              for a full list of valid values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rates/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "price": price,
                        "tax_type": tax_type,
                        "country_code": country_code,
                        "eu": eu,
                        "ip_address": ip_address,
                        "province_code": province_code,
                        "type": type,
                    },
                    rate_calculate_price_params.RateCalculatePriceParams,
                ),
            ),
            cast_to=RateCalculatePriceResponse,
        )

    async def details(
        self,
        *,
        country_code: str | Omit = omit,
        eu: bool | Omit = omit,
        ip_address: str | Omit = omit,
        period: Union[str, datetime] | Omit = omit,
        province_code: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRate:
        """
        Get detailed tax rate information for a location, including all applicable rate
        classes (standard, reduced, zero, etc.).

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          eu: Filter results by EU membership. Use 1 for EU countries only, 0 for non-EU only.

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          period: A historical date to retrieve rates for (format "YYYY-MM-DD HH:MM:SS"). Must be
              a past date.

          province_code: A 2-character province code (e.g. "NU", "NT"). If providing a province code, you
              must also provide the relevant country_code.

          type: The product type to find the applicable rate for. See the /rates/types endpoint
              for a full list of valid values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rates/tax_rate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country_code": country_code,
                        "eu": eu,
                        "ip_address": ip_address,
                        "period": period,
                        "province_code": province_code,
                        "type": type,
                    },
                    rate_details_params.RateDetailsParams,
                ),
            ),
            cast_to=FindRate,
        )

    async def find(
        self,
        *,
        country_code: str | Omit = omit,
        eu: bool | Omit = omit,
        ip_address: str | Omit = omit,
        period: Union[str, datetime] | Omit = omit,
        province_code: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRate:
        """
        A handy endpoint for finding a rate that applies to a particular country and
        optional product type, based on country code or IP address.

        If no type is provided, or no specific rate is applied to the given type, then
        the standard rate will be returned if the country is subject to tax.

        If the country is not subject to VAT/GST then an error response will be
        returned, indicating no tax applies.

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          eu: Filter results by EU membership. Use 1 for EU countries only, 0 for non-EU only.

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          period: A historical date to retrieve rates for (format "YYYY-MM-DD HH:MM:SS"). Must be
              a past date.

          province_code: A 2-character province code (e.g. "NU", "NT"). If providing a province code, you
              must also provide the relevant country_code.

          type: The product type to find the applicable rate for. See the /rates/types endpoint
              for a full list of valid values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rates/rate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country_code": country_code,
                        "eu": eu,
                        "ip_address": ip_address,
                        "period": period,
                        "province_code": province_code,
                        "type": type,
                    },
                    rate_find_params.RateFindParams,
                ),
            ),
            cast_to=FindRate,
        )

    async def list_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RateListTypesResponse:
        """
        Returns a list of all available product types that can be used to filter tax
        rates.
        """
        return await self._get(
            "/rates/types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateListTypesResponse,
        )


class RatesResourceWithRawResponse:
    def __init__(self, rates: RatesResource) -> None:
        self._rates = rates

        self.list = to_raw_response_wrapper(
            rates.list,
        )
        self.calculate_price = to_raw_response_wrapper(
            rates.calculate_price,
        )
        self.details = to_raw_response_wrapper(
            rates.details,
        )
        self.find = to_raw_response_wrapper(
            rates.find,
        )
        self.list_types = to_raw_response_wrapper(
            rates.list_types,
        )


class AsyncRatesResourceWithRawResponse:
    def __init__(self, rates: AsyncRatesResource) -> None:
        self._rates = rates

        self.list = async_to_raw_response_wrapper(
            rates.list,
        )
        self.calculate_price = async_to_raw_response_wrapper(
            rates.calculate_price,
        )
        self.details = async_to_raw_response_wrapper(
            rates.details,
        )
        self.find = async_to_raw_response_wrapper(
            rates.find,
        )
        self.list_types = async_to_raw_response_wrapper(
            rates.list_types,
        )


class RatesResourceWithStreamingResponse:
    def __init__(self, rates: RatesResource) -> None:
        self._rates = rates

        self.list = to_streamed_response_wrapper(
            rates.list,
        )
        self.calculate_price = to_streamed_response_wrapper(
            rates.calculate_price,
        )
        self.details = to_streamed_response_wrapper(
            rates.details,
        )
        self.find = to_streamed_response_wrapper(
            rates.find,
        )
        self.list_types = to_streamed_response_wrapper(
            rates.list_types,
        )


class AsyncRatesResourceWithStreamingResponse:
    def __init__(self, rates: AsyncRatesResource) -> None:
        self._rates = rates

        self.list = async_to_streamed_response_wrapper(
            rates.list,
        )
        self.calculate_price = async_to_streamed_response_wrapper(
            rates.calculate_price,
        )
        self.details = async_to_streamed_response_wrapper(
            rates.details,
        )
        self.find = async_to_streamed_response_wrapper(
            rates.find,
        )
        self.list_types = async_to_streamed_response_wrapper(
            rates.list_types,
        )
