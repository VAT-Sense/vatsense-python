# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import validate_check_params
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
from ..types.validate_check_response import ValidateCheckResponse

__all__ = ["ValidateResource", "AsyncValidateResource"]


class ValidateResource(SyncAPIResource):
    """VAT and EORI number validation"""

    @cached_property
    def with_raw_response(self) -> ValidateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vat-sense-python#accessing-raw-response-data-eg-headers
        """
        return ValidateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vat-sense-python#with_streaming_response
        """
        return ValidateResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        eori_number: str | Omit = omit,
        requester_vat_number: str | Omit = omit,
        vat_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateCheckResponse:
        """
        Check whether a given VAT number or EORI number is valid against live government
        records.

        **VAT validation** checks against UK (HMRC), EU (VIES), Australia, Norway,
        Switzerland, South Africa, and Brazil records.

        **EORI validation** checks against UK and EU records only.

        If the external validation service is temporarily unavailable, the API returns a
        `412` error and the request does not count against your usage quota.

        Provide either `vat_number` or `eori_number`, but not both.

        Args:
          eori_number: The EORI number to validate. Must include the leading 2-character country code
              (e.g. "GB123456789123"). UK and EU only.

          requester_vat_number: Your own VAT number. If supplied, the response will include a unique
              consultation number issued by the relevant authority (VIES or HMRC). Must
              include the leading 2-character country code.

              Note: GB requester numbers only work for GB validations; EU requester numbers
              only work for EU validations. Cross-region is not supported.

          vat_number: The VAT number to validate. Must include the leading 2-character country code
              (e.g. "GB288305674", "FR12345678901").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/validate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eori_number": eori_number,
                        "requester_vat_number": requester_vat_number,
                        "vat_number": vat_number,
                    },
                    validate_check_params.ValidateCheckParams,
                ),
            ),
            cast_to=ValidateCheckResponse,
        )


class AsyncValidateResource(AsyncAPIResource):
    """VAT and EORI number validation"""

    @cached_property
    def with_raw_response(self) -> AsyncValidateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vat-sense-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValidateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vat-sense-python#with_streaming_response
        """
        return AsyncValidateResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        eori_number: str | Omit = omit,
        requester_vat_number: str | Omit = omit,
        vat_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateCheckResponse:
        """
        Check whether a given VAT number or EORI number is valid against live government
        records.

        **VAT validation** checks against UK (HMRC), EU (VIES), Australia, Norway,
        Switzerland, South Africa, and Brazil records.

        **EORI validation** checks against UK and EU records only.

        If the external validation service is temporarily unavailable, the API returns a
        `412` error and the request does not count against your usage quota.

        Provide either `vat_number` or `eori_number`, but not both.

        Args:
          eori_number: The EORI number to validate. Must include the leading 2-character country code
              (e.g. "GB123456789123"). UK and EU only.

          requester_vat_number: Your own VAT number. If supplied, the response will include a unique
              consultation number issued by the relevant authority (VIES or HMRC). Must
              include the leading 2-character country code.

              Note: GB requester numbers only work for GB validations; EU requester numbers
              only work for EU validations. Cross-region is not supported.

          vat_number: The VAT number to validate. Must include the leading 2-character country code
              (e.g. "GB288305674", "FR12345678901").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/validate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "eori_number": eori_number,
                        "requester_vat_number": requester_vat_number,
                        "vat_number": vat_number,
                    },
                    validate_check_params.ValidateCheckParams,
                ),
            ),
            cast_to=ValidateCheckResponse,
        )


class ValidateResourceWithRawResponse:
    def __init__(self, validate: ValidateResource) -> None:
        self._validate = validate

        self.check = to_raw_response_wrapper(
            validate.check,
        )


class AsyncValidateResourceWithRawResponse:
    def __init__(self, validate: AsyncValidateResource) -> None:
        self._validate = validate

        self.check = async_to_raw_response_wrapper(
            validate.check,
        )


class ValidateResourceWithStreamingResponse:
    def __init__(self, validate: ValidateResource) -> None:
        self._validate = validate

        self.check = to_streamed_response_wrapper(
            validate.check,
        )


class AsyncValidateResourceWithStreamingResponse:
    def __init__(self, validate: AsyncValidateResource) -> None:
        self._validate = validate

        self.check = async_to_streamed_response_wrapper(
            validate.check,
        )
