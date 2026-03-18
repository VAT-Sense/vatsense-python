# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import country_list_params, country_list_provinces_params
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
from ..types.country_list_response import CountryListResponse
from ..types.country_list_provinces_response import CountryListProvincesResponse

__all__ = ["CountriesResource", "AsyncCountriesResource"]


class CountriesResource(SyncAPIResource):
    """Country and province information"""

    @cached_property
    def with_raw_response(self) -> CountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return CountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return CountriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        country_code: str | Omit = omit,
        ip_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryListResponse:
        """
        Returns a list of all countries, including whether they are subject to VAT/GST
        and whether they are subject to EU VAT. Each country is returned as a country
        object.

        You can optionally filter by country code or IP address.

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country_code": country_code,
                        "ip_address": ip_address,
                    },
                    country_list_params.CountryListParams,
                ),
            ),
            cast_to=CountryListResponse,
        )

    def list_provinces(
        self,
        *,
        country_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryListProvincesResponse:
        """
        Retrieve a list of all provinces within a given country.

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "CA").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/countries/provinces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"country_code": country_code}, country_list_provinces_params.CountryListProvincesParams
                ),
            ),
            cast_to=CountryListProvincesResponse,
        )


class AsyncCountriesResource(AsyncAPIResource):
    """Country and province information"""

    @cached_property
    def with_raw_response(self) -> AsyncCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return AsyncCountriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        country_code: str | Omit = omit,
        ip_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryListResponse:
        """
        Returns a list of all countries, including whether they are subject to VAT/GST
        and whether they are subject to EU VAT. Each country is returned as a country
        object.

        You can optionally filter by country code or IP address.

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "GB", "FR").

          ip_address: An IPv4 or IPv6 address. If provided, the country will be determined from the IP
              address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country_code": country_code,
                        "ip_address": ip_address,
                    },
                    country_list_params.CountryListParams,
                ),
            ),
            cast_to=CountryListResponse,
        )

    async def list_provinces(
        self,
        *,
        country_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryListProvincesResponse:
        """
        Retrieve a list of all provinces within a given country.

        Args:
          country_code: A 2-character ISO 3166-1 alpha-2 country code (e.g. "CA").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/countries/provinces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"country_code": country_code}, country_list_provinces_params.CountryListProvincesParams
                ),
            ),
            cast_to=CountryListProvincesResponse,
        )


class CountriesResourceWithRawResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.list = to_raw_response_wrapper(
            countries.list,
        )
        self.list_provinces = to_raw_response_wrapper(
            countries.list_provinces,
        )


class AsyncCountriesResourceWithRawResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.list = async_to_raw_response_wrapper(
            countries.list,
        )
        self.list_provinces = async_to_raw_response_wrapper(
            countries.list_provinces,
        )


class CountriesResourceWithStreamingResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.list = to_streamed_response_wrapper(
            countries.list,
        )
        self.list_provinces = to_streamed_response_wrapper(
            countries.list_provinces,
        )


class AsyncCountriesResourceWithStreamingResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.list = async_to_streamed_response_wrapper(
            countries.list,
        )
        self.list_provinces = async_to_streamed_response_wrapper(
            countries.list_provinces,
        )
