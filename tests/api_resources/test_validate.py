# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vat_sense import VatSense, AsyncVatSense
from tests.utils import assert_matches_type
from vat_sense.types import ValidateCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check(self, client: VatSense) -> None:
        validate = client.validate.check()
        assert_matches_type(ValidateCheckResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_with_all_params(self, client: VatSense) -> None:
        validate = client.validate.check(
            eori_number="GB123456789123",
            requester_vat_number="GB288305674",
            vat_number="GB288305674",
        )
        assert_matches_type(ValidateCheckResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: VatSense) -> None:
        response = client.validate.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(ValidateCheckResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: VatSense) -> None:
        with client.validate.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(ValidateCheckResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValidate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncVatSense) -> None:
        validate = await async_client.validate.check()
        assert_matches_type(ValidateCheckResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_with_all_params(self, async_client: AsyncVatSense) -> None:
        validate = await async_client.validate.check(
            eori_number="GB123456789123",
            requester_vat_number="GB288305674",
            vat_number="GB288305674",
        )
        assert_matches_type(ValidateCheckResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncVatSense) -> None:
        response = await async_client.validate.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(ValidateCheckResponse, validate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncVatSense) -> None:
        async with async_client.validate.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(ValidateCheckResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True
