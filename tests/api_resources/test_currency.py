# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vat_sense import VatSense, AsyncVatSense
from tests.utils import assert_matches_type
from vat_sense.types import (
    CurrencyListResponse,
    CurrencyConvertResponse,
    CurrencyCalculateVatPriceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrency:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: VatSense) -> None:
        currency = client.currency.list()
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VatSense) -> None:
        currency = client.currency.list(
            from_="USD,CAD,AUD",
            to="GBP",
        )
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VatSense) -> None:
        response = client.currency.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VatSense) -> None:
        with client.currency.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencyListResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_vat_price(self, client: VatSense) -> None:
        currency = client.currency.calculate_vat_price(
            price=20,
            tax_type="excl",
            vat_rate=5,
        )
        assert_matches_type(CurrencyCalculateVatPriceResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calculate_vat_price(self, client: VatSense) -> None:
        response = client.currency.with_raw_response.calculate_vat_price(
            price=20,
            tax_type="excl",
            vat_rate=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencyCalculateVatPriceResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calculate_vat_price(self, client: VatSense) -> None:
        with client.currency.with_streaming_response.calculate_vat_price(
            price=20,
            tax_type="excl",
            vat_rate=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencyCalculateVatPriceResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_convert(self, client: VatSense) -> None:
        currency = client.currency.convert(
            amount=39.99,
            from_="USD",
            to="GBP",
        )
        assert_matches_type(CurrencyConvertResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_convert(self, client: VatSense) -> None:
        response = client.currency.with_raw_response.convert(
            amount=39.99,
            from_="USD",
            to="GBP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencyConvertResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_convert(self, client: VatSense) -> None:
        with client.currency.with_streaming_response.convert(
            amount=39.99,
            from_="USD",
            to="GBP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencyConvertResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCurrency:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVatSense) -> None:
        currency = await async_client.currency.list()
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVatSense) -> None:
        currency = await async_client.currency.list(
            from_="USD,CAD,AUD",
            to="GBP",
        )
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVatSense) -> None:
        response = await async_client.currency.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVatSense) -> None:
        async with async_client.currency.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencyListResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_vat_price(self, async_client: AsyncVatSense) -> None:
        currency = await async_client.currency.calculate_vat_price(
            price=20,
            tax_type="excl",
            vat_rate=5,
        )
        assert_matches_type(CurrencyCalculateVatPriceResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calculate_vat_price(self, async_client: AsyncVatSense) -> None:
        response = await async_client.currency.with_raw_response.calculate_vat_price(
            price=20,
            tax_type="excl",
            vat_rate=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencyCalculateVatPriceResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calculate_vat_price(self, async_client: AsyncVatSense) -> None:
        async with async_client.currency.with_streaming_response.calculate_vat_price(
            price=20,
            tax_type="excl",
            vat_rate=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencyCalculateVatPriceResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_convert(self, async_client: AsyncVatSense) -> None:
        currency = await async_client.currency.convert(
            amount=39.99,
            from_="USD",
            to="GBP",
        )
        assert_matches_type(CurrencyConvertResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_convert(self, async_client: AsyncVatSense) -> None:
        response = await async_client.currency.with_raw_response.convert(
            amount=39.99,
            from_="USD",
            to="GBP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencyConvertResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_convert(self, async_client: AsyncVatSense) -> None:
        async with async_client.currency.with_streaming_response.convert(
            amount=39.99,
            from_="USD",
            to="GBP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencyConvertResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True
