# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vat_sense import VatSense, AsyncVatSense
from tests.utils import assert_matches_type
from vat_sense.types import (
    InvoiceResponse,
    InvoiceListResponse,
    InvoiceDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: VatSense) -> None:
        invoice = client.invoice.create(
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VatSense) -> None:
        invoice = client.invoice.create(
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
                "bank_account": "bank_account",
                "company_number": "9839222",
                "email": "dev@stainless.com",
                "logo": "https://example.com",
                "phone": "phone",
                "website": "https://example.com",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                    "discount_rate": 40,
                }
            ],
            tax_point="2018-06-03 14:02:00",
            conversion={
                "currency_code": "GBP",
                "rate": 1.523,
            },
            customer={
                "name": "Demo Co.",
                "address": "65 Demo Road\nLondon\nSW1 3DE\nUnited Kingdom",
                "company_number": "5584922",
                "country_code": "country_code",
                "email": "dev@stainless.com",
                "logo": "https://example.com",
                "vat_number": "GB912343332",
            },
            has_vat=True,
            invoice_number="203",
            is_copy=True,
            is_reverse_charge=True,
            notes="notes",
            pad_invoice_number=2,
            serial="serial",
            tax_type="incl",
            type="sale",
            zero_rated=True,
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VatSense) -> None:
        response = client.invoice.with_raw_response.create(
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VatSense) -> None:
        with client.invoice.with_streaming_response.create(
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VatSense) -> None:
        invoice = client.invoice.retrieve(
            "in5aeae457cda2a",
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VatSense) -> None:
        response = client.invoice.with_raw_response.retrieve(
            "in5aeae457cda2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VatSense) -> None:
        with client.invoice.with_streaming_response.retrieve(
            "in5aeae457cda2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoice.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: VatSense) -> None:
        invoice = client.invoice.update(
            invoice_id="in5aeae457cda2a",
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VatSense) -> None:
        invoice = client.invoice.update(
            invoice_id="in5aeae457cda2a",
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
                "bank_account": "bank_account",
                "company_number": "9839222",
                "email": "dev@stainless.com",
                "logo": "https://example.com",
                "phone": "phone",
                "website": "https://example.com",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                    "discount_rate": 40,
                }
            ],
            tax_point="2018-06-03 14:02:00",
            conversion={
                "currency_code": "GBP",
                "rate": 1.523,
            },
            customer={
                "name": "Demo Co.",
                "address": "65 Demo Road\nLondon\nSW1 3DE\nUnited Kingdom",
                "company_number": "5584922",
                "country_code": "country_code",
                "email": "dev@stainless.com",
                "logo": "https://example.com",
                "vat_number": "GB912343332",
            },
            has_vat=True,
            invoice_number="203",
            is_copy=True,
            is_reverse_charge=True,
            notes="notes",
            pad_invoice_number=2,
            serial="serial",
            tax_type="incl",
            type="sale",
            zero_rated=True,
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VatSense) -> None:
        response = client.invoice.with_raw_response.update(
            invoice_id="in5aeae457cda2a",
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VatSense) -> None:
        with client.invoice.with_streaming_response.update(
            invoice_id="in5aeae457cda2a",
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoice.with_raw_response.update(
                invoice_id="",
                business={
                    "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                    "name": "VAT Sense",
                    "vat_number": "GB12345678",
                },
                currency_code="USD",
                date="2018-06-03 14:02:00",
                items=[
                    {
                        "item": "Standard payment plan",
                        "price_each": 19.99,
                        "quantity": 1,
                        "vat_rate": 20,
                    }
                ],
                tax_point="2018-06-03 14:02:00",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: VatSense) -> None:
        invoice = client.invoice.list()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VatSense) -> None:
        invoice = client.invoice.list(
            limit=1,
            offset=0,
            search="search",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VatSense) -> None:
        response = client.invoice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VatSense) -> None:
        with client.invoice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: VatSense) -> None:
        invoice = client.invoice.delete(
            "in5aeae457cda2a",
        )
        assert_matches_type(InvoiceDeleteResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: VatSense) -> None:
        response = client.invoice.with_raw_response.delete(
            "in5aeae457cda2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceDeleteResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: VatSense) -> None:
        with client.invoice.with_streaming_response.delete(
            "in5aeae457cda2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceDeleteResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: VatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoice.with_raw_response.delete(
                "",
            )


class TestAsyncInvoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVatSense) -> None:
        invoice = await async_client.invoice.create(
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVatSense) -> None:
        invoice = await async_client.invoice.create(
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
                "bank_account": "bank_account",
                "company_number": "9839222",
                "email": "dev@stainless.com",
                "logo": "https://example.com",
                "phone": "phone",
                "website": "https://example.com",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                    "discount_rate": 40,
                }
            ],
            tax_point="2018-06-03 14:02:00",
            conversion={
                "currency_code": "GBP",
                "rate": 1.523,
            },
            customer={
                "name": "Demo Co.",
                "address": "65 Demo Road\nLondon\nSW1 3DE\nUnited Kingdom",
                "company_number": "5584922",
                "country_code": "country_code",
                "email": "dev@stainless.com",
                "logo": "https://example.com",
                "vat_number": "GB912343332",
            },
            has_vat=True,
            invoice_number="203",
            is_copy=True,
            is_reverse_charge=True,
            notes="notes",
            pad_invoice_number=2,
            serial="serial",
            tax_type="incl",
            type="sale",
            zero_rated=True,
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.with_raw_response.create(
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.with_streaming_response.create(
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVatSense) -> None:
        invoice = await async_client.invoice.retrieve(
            "in5aeae457cda2a",
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.with_raw_response.retrieve(
            "in5aeae457cda2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.with_streaming_response.retrieve(
            "in5aeae457cda2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoice.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVatSense) -> None:
        invoice = await async_client.invoice.update(
            invoice_id="in5aeae457cda2a",
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVatSense) -> None:
        invoice = await async_client.invoice.update(
            invoice_id="in5aeae457cda2a",
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
                "bank_account": "bank_account",
                "company_number": "9839222",
                "email": "dev@stainless.com",
                "logo": "https://example.com",
                "phone": "phone",
                "website": "https://example.com",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                    "discount_rate": 40,
                }
            ],
            tax_point="2018-06-03 14:02:00",
            conversion={
                "currency_code": "GBP",
                "rate": 1.523,
            },
            customer={
                "name": "Demo Co.",
                "address": "65 Demo Road\nLondon\nSW1 3DE\nUnited Kingdom",
                "company_number": "5584922",
                "country_code": "country_code",
                "email": "dev@stainless.com",
                "logo": "https://example.com",
                "vat_number": "GB912343332",
            },
            has_vat=True,
            invoice_number="203",
            is_copy=True,
            is_reverse_charge=True,
            notes="notes",
            pad_invoice_number=2,
            serial="serial",
            tax_type="incl",
            type="sale",
            zero_rated=True,
        )
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.with_raw_response.update(
            invoice_id="in5aeae457cda2a",
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.with_streaming_response.update(
            invoice_id="in5aeae457cda2a",
            business={
                "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                "name": "VAT Sense",
                "vat_number": "GB12345678",
            },
            currency_code="USD",
            date="2018-06-03 14:02:00",
            items=[
                {
                    "item": "Standard payment plan",
                    "price_each": 19.99,
                    "quantity": 1,
                    "vat_rate": 20,
                }
            ],
            tax_point="2018-06-03 14:02:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoice.with_raw_response.update(
                invoice_id="",
                business={
                    "address": "123 Example Street\nLondon\nSW3 1GL\nUnited Kingdom",
                    "name": "VAT Sense",
                    "vat_number": "GB12345678",
                },
                currency_code="USD",
                date="2018-06-03 14:02:00",
                items=[
                    {
                        "item": "Standard payment plan",
                        "price_each": 19.99,
                        "quantity": 1,
                        "vat_rate": 20,
                    }
                ],
                tax_point="2018-06-03 14:02:00",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVatSense) -> None:
        invoice = await async_client.invoice.list()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVatSense) -> None:
        invoice = await async_client.invoice.list(
            limit=1,
            offset=0,
            search="search",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncVatSense) -> None:
        invoice = await async_client.invoice.delete(
            "in5aeae457cda2a",
        )
        assert_matches_type(InvoiceDeleteResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVatSense) -> None:
        response = await async_client.invoice.with_raw_response.delete(
            "in5aeae457cda2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceDeleteResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVatSense) -> None:
        async with async_client.invoice.with_streaming_response.delete(
            "in5aeae457cda2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceDeleteResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVatSense) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoice.with_raw_response.delete(
                "",
            )
