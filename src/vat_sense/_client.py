# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import VatSenseError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import rates, usage, invoice, sandbox, currency, validate, countries
    from .resources.rates import RatesResource, AsyncRatesResource
    from .resources.usage import UsageResource, AsyncUsageResource
    from .resources.sandbox import SandboxResource, AsyncSandboxResource
    from .resources.currency import CurrencyResource, AsyncCurrencyResource
    from .resources.validate import ValidateResource, AsyncValidateResource
    from .resources.countries import CountriesResource, AsyncCountriesResource
    from .resources.invoice.invoice import InvoiceResource, AsyncInvoiceResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "VatSense",
    "AsyncVatSense",
    "Client",
    "AsyncClient",
]


class VatSense(SyncAPIClient):
    # client options
    username: str
    password: str

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous VatSense client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `VAT_SENSE_USERNAME`
        - `password` from `VAT_SENSE_PASSWORD`
        """
        if username is None:
            username = os.environ.get("VAT_SENSE_USERNAME")
        if username is None:
            raise VatSenseError(
                "The username client option must be set either by passing username to the client or by setting the VAT_SENSE_USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("VAT_SENSE_PASSWORD")
        if password is None:
            raise VatSenseError(
                "The password client option must be set either by passing password to the client or by setting the VAT_SENSE_PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("VAT_SENSE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.vatsense.com/1.0"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def rates(self) -> RatesResource:
        """VAT/GST rate lookups for countries worldwide"""
        from .resources.rates import RatesResource

        return RatesResource(self)

    @cached_property
    def countries(self) -> CountriesResource:
        """Country and province information"""
        from .resources.countries import CountriesResource

        return CountriesResource(self)

    @cached_property
    def validate(self) -> ValidateResource:
        """VAT and EORI number validation"""
        from .resources.validate import ValidateResource

        return ValidateResource(self)

    @cached_property
    def currency(self) -> CurrencyResource:
        """Currency exchange rates and conversion"""
        from .resources.currency import CurrencyResource

        return CurrencyResource(self)

    @cached_property
    def invoice(self) -> InvoiceResource:
        """VAT-compliant invoice management"""
        from .resources.invoice import InvoiceResource

        return InvoiceResource(self)

    @cached_property
    def usage(self) -> UsageResource:
        """API usage statistics"""
        from .resources.usage import UsageResource

        return UsageResource(self)

    @cached_property
    def sandbox(self) -> SandboxResource:
        """Temporary sandbox API keys for testing"""
        from .resources.sandbox import SandboxResource

        return SandboxResource(self)

    @cached_property
    def with_raw_response(self) -> VatSenseWithRawResponse:
        return VatSenseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VatSenseWithStreamedResponse:
        return VatSenseWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._basic_auth if security.get("basic_auth", False) else {}),
        }

    @property
    def _basic_auth(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncVatSense(AsyncAPIClient):
    # client options
    username: str
    password: str

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncVatSense client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `VAT_SENSE_USERNAME`
        - `password` from `VAT_SENSE_PASSWORD`
        """
        if username is None:
            username = os.environ.get("VAT_SENSE_USERNAME")
        if username is None:
            raise VatSenseError(
                "The username client option must be set either by passing username to the client or by setting the VAT_SENSE_USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("VAT_SENSE_PASSWORD")
        if password is None:
            raise VatSenseError(
                "The password client option must be set either by passing password to the client or by setting the VAT_SENSE_PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("VAT_SENSE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.vatsense.com/1.0"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def rates(self) -> AsyncRatesResource:
        """VAT/GST rate lookups for countries worldwide"""
        from .resources.rates import AsyncRatesResource

        return AsyncRatesResource(self)

    @cached_property
    def countries(self) -> AsyncCountriesResource:
        """Country and province information"""
        from .resources.countries import AsyncCountriesResource

        return AsyncCountriesResource(self)

    @cached_property
    def validate(self) -> AsyncValidateResource:
        """VAT and EORI number validation"""
        from .resources.validate import AsyncValidateResource

        return AsyncValidateResource(self)

    @cached_property
    def currency(self) -> AsyncCurrencyResource:
        """Currency exchange rates and conversion"""
        from .resources.currency import AsyncCurrencyResource

        return AsyncCurrencyResource(self)

    @cached_property
    def invoice(self) -> AsyncInvoiceResource:
        """VAT-compliant invoice management"""
        from .resources.invoice import AsyncInvoiceResource

        return AsyncInvoiceResource(self)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        """API usage statistics"""
        from .resources.usage import AsyncUsageResource

        return AsyncUsageResource(self)

    @cached_property
    def sandbox(self) -> AsyncSandboxResource:
        """Temporary sandbox API keys for testing"""
        from .resources.sandbox import AsyncSandboxResource

        return AsyncSandboxResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncVatSenseWithRawResponse:
        return AsyncVatSenseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVatSenseWithStreamedResponse:
        return AsyncVatSenseWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._basic_auth if security.get("basic_auth", False) else {}),
        }

    @property
    def _basic_auth(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class VatSenseWithRawResponse:
    _client: VatSense

    def __init__(self, client: VatSense) -> None:
        self._client = client

    @cached_property
    def rates(self) -> rates.RatesResourceWithRawResponse:
        """VAT/GST rate lookups for countries worldwide"""
        from .resources.rates import RatesResourceWithRawResponse

        return RatesResourceWithRawResponse(self._client.rates)

    @cached_property
    def countries(self) -> countries.CountriesResourceWithRawResponse:
        """Country and province information"""
        from .resources.countries import CountriesResourceWithRawResponse

        return CountriesResourceWithRawResponse(self._client.countries)

    @cached_property
    def validate(self) -> validate.ValidateResourceWithRawResponse:
        """VAT and EORI number validation"""
        from .resources.validate import ValidateResourceWithRawResponse

        return ValidateResourceWithRawResponse(self._client.validate)

    @cached_property
    def currency(self) -> currency.CurrencyResourceWithRawResponse:
        """Currency exchange rates and conversion"""
        from .resources.currency import CurrencyResourceWithRawResponse

        return CurrencyResourceWithRawResponse(self._client.currency)

    @cached_property
    def invoice(self) -> invoice.InvoiceResourceWithRawResponse:
        """VAT-compliant invoice management"""
        from .resources.invoice import InvoiceResourceWithRawResponse

        return InvoiceResourceWithRawResponse(self._client.invoice)

    @cached_property
    def usage(self) -> usage.UsageResourceWithRawResponse:
        """API usage statistics"""
        from .resources.usage import UsageResourceWithRawResponse

        return UsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def sandbox(self) -> sandbox.SandboxResourceWithRawResponse:
        """Temporary sandbox API keys for testing"""
        from .resources.sandbox import SandboxResourceWithRawResponse

        return SandboxResourceWithRawResponse(self._client.sandbox)


class AsyncVatSenseWithRawResponse:
    _client: AsyncVatSense

    def __init__(self, client: AsyncVatSense) -> None:
        self._client = client

    @cached_property
    def rates(self) -> rates.AsyncRatesResourceWithRawResponse:
        """VAT/GST rate lookups for countries worldwide"""
        from .resources.rates import AsyncRatesResourceWithRawResponse

        return AsyncRatesResourceWithRawResponse(self._client.rates)

    @cached_property
    def countries(self) -> countries.AsyncCountriesResourceWithRawResponse:
        """Country and province information"""
        from .resources.countries import AsyncCountriesResourceWithRawResponse

        return AsyncCountriesResourceWithRawResponse(self._client.countries)

    @cached_property
    def validate(self) -> validate.AsyncValidateResourceWithRawResponse:
        """VAT and EORI number validation"""
        from .resources.validate import AsyncValidateResourceWithRawResponse

        return AsyncValidateResourceWithRawResponse(self._client.validate)

    @cached_property
    def currency(self) -> currency.AsyncCurrencyResourceWithRawResponse:
        """Currency exchange rates and conversion"""
        from .resources.currency import AsyncCurrencyResourceWithRawResponse

        return AsyncCurrencyResourceWithRawResponse(self._client.currency)

    @cached_property
    def invoice(self) -> invoice.AsyncInvoiceResourceWithRawResponse:
        """VAT-compliant invoice management"""
        from .resources.invoice import AsyncInvoiceResourceWithRawResponse

        return AsyncInvoiceResourceWithRawResponse(self._client.invoice)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithRawResponse:
        """API usage statistics"""
        from .resources.usage import AsyncUsageResourceWithRawResponse

        return AsyncUsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def sandbox(self) -> sandbox.AsyncSandboxResourceWithRawResponse:
        """Temporary sandbox API keys for testing"""
        from .resources.sandbox import AsyncSandboxResourceWithRawResponse

        return AsyncSandboxResourceWithRawResponse(self._client.sandbox)


class VatSenseWithStreamedResponse:
    _client: VatSense

    def __init__(self, client: VatSense) -> None:
        self._client = client

    @cached_property
    def rates(self) -> rates.RatesResourceWithStreamingResponse:
        """VAT/GST rate lookups for countries worldwide"""
        from .resources.rates import RatesResourceWithStreamingResponse

        return RatesResourceWithStreamingResponse(self._client.rates)

    @cached_property
    def countries(self) -> countries.CountriesResourceWithStreamingResponse:
        """Country and province information"""
        from .resources.countries import CountriesResourceWithStreamingResponse

        return CountriesResourceWithStreamingResponse(self._client.countries)

    @cached_property
    def validate(self) -> validate.ValidateResourceWithStreamingResponse:
        """VAT and EORI number validation"""
        from .resources.validate import ValidateResourceWithStreamingResponse

        return ValidateResourceWithStreamingResponse(self._client.validate)

    @cached_property
    def currency(self) -> currency.CurrencyResourceWithStreamingResponse:
        """Currency exchange rates and conversion"""
        from .resources.currency import CurrencyResourceWithStreamingResponse

        return CurrencyResourceWithStreamingResponse(self._client.currency)

    @cached_property
    def invoice(self) -> invoice.InvoiceResourceWithStreamingResponse:
        """VAT-compliant invoice management"""
        from .resources.invoice import InvoiceResourceWithStreamingResponse

        return InvoiceResourceWithStreamingResponse(self._client.invoice)

    @cached_property
    def usage(self) -> usage.UsageResourceWithStreamingResponse:
        """API usage statistics"""
        from .resources.usage import UsageResourceWithStreamingResponse

        return UsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def sandbox(self) -> sandbox.SandboxResourceWithStreamingResponse:
        """Temporary sandbox API keys for testing"""
        from .resources.sandbox import SandboxResourceWithStreamingResponse

        return SandboxResourceWithStreamingResponse(self._client.sandbox)


class AsyncVatSenseWithStreamedResponse:
    _client: AsyncVatSense

    def __init__(self, client: AsyncVatSense) -> None:
        self._client = client

    @cached_property
    def rates(self) -> rates.AsyncRatesResourceWithStreamingResponse:
        """VAT/GST rate lookups for countries worldwide"""
        from .resources.rates import AsyncRatesResourceWithStreamingResponse

        return AsyncRatesResourceWithStreamingResponse(self._client.rates)

    @cached_property
    def countries(self) -> countries.AsyncCountriesResourceWithStreamingResponse:
        """Country and province information"""
        from .resources.countries import AsyncCountriesResourceWithStreamingResponse

        return AsyncCountriesResourceWithStreamingResponse(self._client.countries)

    @cached_property
    def validate(self) -> validate.AsyncValidateResourceWithStreamingResponse:
        """VAT and EORI number validation"""
        from .resources.validate import AsyncValidateResourceWithStreamingResponse

        return AsyncValidateResourceWithStreamingResponse(self._client.validate)

    @cached_property
    def currency(self) -> currency.AsyncCurrencyResourceWithStreamingResponse:
        """Currency exchange rates and conversion"""
        from .resources.currency import AsyncCurrencyResourceWithStreamingResponse

        return AsyncCurrencyResourceWithStreamingResponse(self._client.currency)

    @cached_property
    def invoice(self) -> invoice.AsyncInvoiceResourceWithStreamingResponse:
        """VAT-compliant invoice management"""
        from .resources.invoice import AsyncInvoiceResourceWithStreamingResponse

        return AsyncInvoiceResourceWithStreamingResponse(self._client.invoice)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithStreamingResponse:
        """API usage statistics"""
        from .resources.usage import AsyncUsageResourceWithStreamingResponse

        return AsyncUsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def sandbox(self) -> sandbox.AsyncSandboxResourceWithStreamingResponse:
        """Temporary sandbox API keys for testing"""
        from .resources.sandbox import AsyncSandboxResourceWithStreamingResponse

        return AsyncSandboxResourceWithStreamingResponse(self._client.sandbox)


Client = VatSense

AsyncClient = AsyncVatSense
