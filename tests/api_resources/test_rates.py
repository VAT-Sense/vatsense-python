# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vat_sense import VatSense, AsyncVatSense
from tests.utils import assert_matches_type
from vat_sense.types import (
    FindRate,
    RateListResponse,
    RateListTypesResponse,
    RateCalculatePriceResponse,
)
from vat_sense._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: VatSense) -> None:
        rate = client.rates.list()
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VatSense) -> None:
        rate = client.rates.list(
            country_code="GB",
            eu=True,
            ip_address="86.27.166.97",
            period=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VatSense) -> None:
        response = client.rates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VatSense) -> None:
        with client.rates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateListResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_price(self, client: VatSense) -> None:
        rate = client.rates.calculate_price(
            price=20,
            tax_type="excl",
        )
        assert_matches_type(RateCalculatePriceResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_price_with_all_params(self, client: VatSense) -> None:
        rate = client.rates.calculate_price(
            price=20,
            tax_type="excl",
            country_code="GB",
            eu=True,
            ip_address="86.27.166.97",
            province_code="ON",
            type="ebooks",
        )
        assert_matches_type(RateCalculatePriceResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calculate_price(self, client: VatSense) -> None:
        response = client.rates.with_raw_response.calculate_price(
            price=20,
            tax_type="excl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateCalculatePriceResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calculate_price(self, client: VatSense) -> None:
        with client.rates.with_streaming_response.calculate_price(
            price=20,
            tax_type="excl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateCalculatePriceResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_details(self, client: VatSense) -> None:
        rate = client.rates.details()
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_details_with_all_params(self, client: VatSense) -> None:
        rate = client.rates.details(
            country_code="GB",
            eu=True,
            ip_address="86.27.166.97",
            period=parse_datetime("2019-12-27T18:11:19.117Z"),
            province_code="ON",
            type="ebooks",
        )
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_details(self, client: VatSense) -> None:
        response = client.rates.with_raw_response.details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_details(self, client: VatSense) -> None:
        with client.rates.with_streaming_response.details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(FindRate, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find(self, client: VatSense) -> None:
        rate = client.rates.find()
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_with_all_params(self, client: VatSense) -> None:
        rate = client.rates.find(
            country_code="GB",
            eu=True,
            ip_address="86.27.166.97",
            period=parse_datetime("2019-12-27T18:11:19.117Z"),
            province_code="ON",
            type="ebooks",
        )
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find(self, client: VatSense) -> None:
        response = client.rates.with_raw_response.find()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find(self, client: VatSense) -> None:
        with client.rates.with_streaming_response.find() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(FindRate, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_types(self, client: VatSense) -> None:
        rate = client.rates.list_types()
        assert_matches_type(RateListTypesResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_types(self, client: VatSense) -> None:
        response = client.rates.with_raw_response.list_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateListTypesResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_types(self, client: VatSense) -> None:
        with client.rates.with_streaming_response.list_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateListTypesResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.list()
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.list(
            country_code="GB",
            eu=True,
            ip_address="86.27.166.97",
            period=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVatSense) -> None:
        response = await async_client.rates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateListResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVatSense) -> None:
        async with async_client.rates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateListResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_price(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.calculate_price(
            price=20,
            tax_type="excl",
        )
        assert_matches_type(RateCalculatePriceResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_price_with_all_params(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.calculate_price(
            price=20,
            tax_type="excl",
            country_code="GB",
            eu=True,
            ip_address="86.27.166.97",
            province_code="ON",
            type="ebooks",
        )
        assert_matches_type(RateCalculatePriceResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calculate_price(self, async_client: AsyncVatSense) -> None:
        response = await async_client.rates.with_raw_response.calculate_price(
            price=20,
            tax_type="excl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateCalculatePriceResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calculate_price(self, async_client: AsyncVatSense) -> None:
        async with async_client.rates.with_streaming_response.calculate_price(
            price=20,
            tax_type="excl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateCalculatePriceResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_details(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.details()
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_details_with_all_params(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.details(
            country_code="GB",
            eu=True,
            ip_address="86.27.166.97",
            period=parse_datetime("2019-12-27T18:11:19.117Z"),
            province_code="ON",
            type="ebooks",
        )
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_details(self, async_client: AsyncVatSense) -> None:
        response = await async_client.rates.with_raw_response.details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_details(self, async_client: AsyncVatSense) -> None:
        async with async_client.rates.with_streaming_response.details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(FindRate, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.find()
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_with_all_params(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.find(
            country_code="GB",
            eu=True,
            ip_address="86.27.166.97",
            period=parse_datetime("2019-12-27T18:11:19.117Z"),
            province_code="ON",
            type="ebooks",
        )
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find(self, async_client: AsyncVatSense) -> None:
        response = await async_client.rates.with_raw_response.find()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(FindRate, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find(self, async_client: AsyncVatSense) -> None:
        async with async_client.rates.with_streaming_response.find() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(FindRate, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_types(self, async_client: AsyncVatSense) -> None:
        rate = await async_client.rates.list_types()
        assert_matches_type(RateListTypesResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_types(self, async_client: AsyncVatSense) -> None:
        response = await async_client.rates.with_raw_response.list_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateListTypesResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_types(self, async_client: AsyncVatSense) -> None:
        async with async_client.rates.with_streaming_response.list_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateListTypesResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True
