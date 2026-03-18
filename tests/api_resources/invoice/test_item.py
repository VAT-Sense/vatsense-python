# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vat_sense import VatSense, AsyncVatSense
from tests.utils import assert_matches_type
from vat_sense.types import InvoiceResponse
from vat_sense.types.invoice import ItemRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VatSense) -> None:
        item = client.invoice.item.retrieve(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        )
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VatSense) -> None:
        response = client.invoice.item.with_raw_response.retrieve(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VatSense) -> None:
        with client.invoice.item.with_streaming_response.retrieve(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemRetrieveResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoice.item.with_raw_response.retrieve(
                item_id="ii5aeae457ce201",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.invoice.item.with_raw_response.retrieve(
                item_id="",
                invoice_id="in5aeae457cda2a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: VatSense) -> None:
        item = client.invoice.item.update(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
            item="Standard payment plan",
            price_each=19.99,
            quantity=1,
            vat_rate=20,
        )
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VatSense) -> None:
        item = client.invoice.item.update(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
            item="Standard payment plan",
            price_each=19.99,
            quantity=1,
            vat_rate=20,
            discount_rate=40,
        )
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VatSense) -> None:
        response = client.invoice.item.with_raw_response.update(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
            item="Standard payment plan",
            price_each=19.99,
            quantity=1,
            vat_rate=20,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VatSense) -> None:
        with client.invoice.item.with_streaming_response.update(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
            item="Standard payment plan",
            price_each=19.99,
            quantity=1,
            vat_rate=20,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(InvoiceResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoice.item.with_raw_response.update(
                item_id="ii5aeae457ce201",
                invoice_id="",
                item="Standard payment plan",
                price_each=19.99,
                quantity=1,
                vat_rate=20,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.invoice.item.with_raw_response.update(
                item_id="",
                invoice_id="in5aeae457cda2a",
                item="Standard payment plan",
                price_each=19.99,
                quantity=1,
                vat_rate=20,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: VatSense) -> None:
        item = client.invoice.item.delete(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        )
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: VatSense) -> None:
        response = client.invoice.item.with_raw_response.delete(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: VatSense) -> None:
        with client.invoice.item.with_streaming_response.delete(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(InvoiceResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: VatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoice.item.with_raw_response.delete(
                item_id="ii5aeae457ce201",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.invoice.item.with_raw_response.delete(
                item_id="",
                invoice_id="in5aeae457cda2a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: VatSense) -> None:
        item = client.invoice.item.add(
            invoice_id="in5aeae457cda2a",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
        )
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: VatSense) -> None:
        response = client.invoice.item.with_raw_response.add(
            invoice_id="in5aeae457cda2a",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: VatSense) -> None:
        with client.invoice.item.with_streaming_response.add(
            invoice_id="in5aeae457cda2a",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(InvoiceResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: VatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoice.item.with_raw_response.add(
                invoice_id="",
                items=[
                    {
                        "item": "Standard payment plan",
                        "price_each": 19.99,
                        "quantity": 1,
                        "vat_rate": 20,
                    }
                ],
            )


class TestAsyncItem:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVatSense) -> None:
        item = await async_client.invoice.item.retrieve(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        )
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.item.with_raw_response.retrieve(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemRetrieveResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.item.with_streaming_response.retrieve(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemRetrieveResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoice.item.with_raw_response.retrieve(
                item_id="ii5aeae457ce201",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.invoice.item.with_raw_response.retrieve(
                item_id="",
                invoice_id="in5aeae457cda2a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVatSense) -> None:
        item = await async_client.invoice.item.update(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
            item="Standard payment plan",
            price_each=19.99,
            quantity=1,
            vat_rate=20,
        )
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVatSense) -> None:
        item = await async_client.invoice.item.update(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
            item="Standard payment plan",
            price_each=19.99,
            quantity=1,
            vat_rate=20,
            discount_rate=40,
        )
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.item.with_raw_response.update(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
            item="Standard payment plan",
            price_each=19.99,
            quantity=1,
            vat_rate=20,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.item.with_streaming_response.update(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
            item="Standard payment plan",
            price_each=19.99,
            quantity=1,
            vat_rate=20,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(InvoiceResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoice.item.with_raw_response.update(
                item_id="ii5aeae457ce201",
                invoice_id="",
                item="Standard payment plan",
                price_each=19.99,
                quantity=1,
                vat_rate=20,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.invoice.item.with_raw_response.update(
                item_id="",
                invoice_id="in5aeae457cda2a",
                item="Standard payment plan",
                price_each=19.99,
                quantity=1,
                vat_rate=20,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncVatSense) -> None:
        item = await async_client.invoice.item.delete(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        )
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.item.with_raw_response.delete(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.item.with_streaming_response.delete(
            item_id="ii5aeae457ce201",
            invoice_id="in5aeae457cda2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(InvoiceResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoice.item.with_raw_response.delete(
                item_id="ii5aeae457ce201",
                invoice_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.invoice.item.with_raw_response.delete(
                item_id="",
                invoice_id="in5aeae457cda2a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncVatSense) -> None:
        item = await async_client.invoice.item.add(
            invoice_id="in5aeae457cda2a",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
        )
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.item.with_raw_response.add(
            invoice_id="in5aeae457cda2a",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(InvoiceResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.item.with_streaming_response.add(
            invoice_id="in5aeae457cda2a",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(InvoiceResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncVatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoice.item.with_raw_response.add(
                invoice_id="",
                items=[
                    {
                        "item": "Standard payment plan",
                        "price_each": 19.99,
                        "quantity": 1,
                        "vat_rate": 20,
                    }
                ],
            )
