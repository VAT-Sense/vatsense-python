# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vat_sense import VatSense, AsyncVatSense
from tests.utils import assert_matches_type
from vat_sense.types import SandboxGenerateKeyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSandbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_key(self, client: VatSense) -> None:
        sandbox = client.sandbox.generate_key()
        assert_matches_type(SandboxGenerateKeyResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_key(self, client: VatSense) -> None:
        response = client.sandbox.with_raw_response.generate_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxGenerateKeyResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_key(self, client: VatSense) -> None:
        with client.sandbox.with_streaming_response.generate_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxGenerateKeyResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSandbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_key(self, async_client: AsyncVatSense) -> None:
        sandbox = await async_client.sandbox.generate_key()
        assert_matches_type(SandboxGenerateKeyResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_key(self, async_client: AsyncVatSense) -> None:
        response = await async_client.sandbox.with_raw_response.generate_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxGenerateKeyResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_key(self, async_client: AsyncVatSense) -> None:
        async with async_client.sandbox.with_streaming_response.generate_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxGenerateKeyResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True
