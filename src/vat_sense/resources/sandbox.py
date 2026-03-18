# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sandbox_generate_key_response import SandboxGenerateKeyResponse

__all__ = ["SandboxResource", "AsyncSandboxResource"]


class SandboxResource(SyncAPIResource):
    """Temporary sandbox API keys for testing"""

    @cached_property
    def with_raw_response(self) -> SandboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return SandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return SandboxResourceWithStreamingResponse(self)

    def generate_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxGenerateKeyResponse:
        """Generate a temporary sandbox API key for testing.

        Sandbox keys have limited
        request allowances and restricted endpoint access (no invoice endpoints). Rate
        limited to 1 key per IP address per 6 hours.
        """
        return self._post(
            "/sandbox/key",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SandboxGenerateKeyResponse,
        )


class AsyncSandboxResource(AsyncAPIResource):
    """Temporary sandbox API keys for testing"""

    @cached_property
    def with_raw_response(self) -> AsyncSandboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAT-Sense/vatsense-python#with_streaming_response
        """
        return AsyncSandboxResourceWithStreamingResponse(self)

    async def generate_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxGenerateKeyResponse:
        """Generate a temporary sandbox API key for testing.

        Sandbox keys have limited
        request allowances and restricted endpoint access (no invoice endpoints). Rate
        limited to 1 key per IP address per 6 hours.
        """
        return await self._post(
            "/sandbox/key",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SandboxGenerateKeyResponse,
        )


class SandboxResourceWithRawResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

        self.generate_key = to_raw_response_wrapper(
            sandbox.generate_key,
        )


class AsyncSandboxResourceWithRawResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

        self.generate_key = async_to_raw_response_wrapper(
            sandbox.generate_key,
        )


class SandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

        self.generate_key = to_streamed_response_wrapper(
            sandbox.generate_key,
        )


class AsyncSandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

        self.generate_key = async_to_streamed_response_wrapper(
            sandbox.generate_key,
        )
