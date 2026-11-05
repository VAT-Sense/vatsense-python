# Checks for the API additions of November 2026, sent through a mocked transport.

from __future__ import annotations

import json
from typing import Any, Dict

import httpx
import pytest
from respx import MockRouter

from vat_sense import VatSense, AsyncVatSense

base_url = "http://127.0.0.1:4010"
ok: Dict[str, Any] = {"success": True, "code": 200, "data": {}}

invoice_args: Dict[str, Any] = dict(
    business={"name": "VAT Sense", "address": "London", "vat_number": "GB12345678"},
    currency_code="GBP",
    date="2026-11-05",
    tax_point="2026-11-05",
    items=[{"item": "Plan", "price_each": 10, "quantity": 1, "vat_rate": 20}],
)


@pytest.mark.respx(base_url=base_url)
def test_invoice_create_sends_idempotency_key_header(respx_mock: MockRouter) -> None:
    route = respx_mock.post("/invoice").mock(return_value=httpx.Response(200, json=ok))
    client = VatSense(base_url=base_url, username="user", password="key")
    client.invoice.create(
        **invoice_args, type="refund", original_invoice_id="in5aeae457cda2a", idempotency_key="order-203"
    )
    request = route.calls.last.request
    assert request.headers["Idempotency-Key"] == "order-203"
    body = json.loads(request.content)
    assert body["original_invoice_id"] == "in5aeae457cda2a"
    assert "idempotency_key" not in body and "Idempotency-Key" not in body


@pytest.mark.respx(base_url=base_url)
def test_invoice_create_without_key_sends_no_header(respx_mock: MockRouter) -> None:
    route = respx_mock.post("/invoice").mock(return_value=httpx.Response(200, json=ok))
    client = VatSense(base_url=base_url, username="user", password="key")
    client.invoice.create(**invoice_args)
    assert "Idempotency-Key" not in route.calls.last.request.headers


@pytest.mark.respx(base_url=base_url)
async def test_async_invoice_create_sends_idempotency_key_header(respx_mock: MockRouter) -> None:
    route = respx_mock.post("/invoice").mock(return_value=httpx.Response(200, json=ok))
    client = AsyncVatSense(base_url=base_url, username="user", password="key")
    await client.invoice.create(**invoice_args, idempotency_key="order-204")
    assert route.calls.last.request.headers["Idempotency-Key"] == "order-204"


@pytest.mark.respx(base_url=base_url)
def test_validate_sends_match_params_and_parses_match(respx_mock: MockRouter) -> None:
    route = respx_mock.get("/validate").mock(
        return_value=httpx.Response(
            200,
            json={
                "success": True,
                "code": 200,
                "data": {
                    "valid": True,
                    "match": {
                        "result": "likely",
                        "score": 90,
                        "fields": {"company_name": {"result": "match", "score": 100, "vies": None}},
                    },
                },
            },
        )
    )
    client = VatSense(base_url=base_url, username="user", password="key")
    result = client.validate.check(vat_number="GB288305674", match_company_name="Weio Ltd", match_postcode="SW3 1GL")
    params = route.calls.last.request.url.params
    assert params["match_company_name"] == "Weio Ltd"
    assert params["match_postcode"] == "SW3 1GL"
    assert result.data is not None and result.data.match is not None
    assert result.data.match.result == "likely"
    assert result.data.match.fields is not None
    assert result.data.match.fields["company_name"].score == 100


@pytest.mark.respx(base_url=base_url)
def test_rates_list_sends_provinces(respx_mock: MockRouter) -> None:
    route = respx_mock.get("/rates").mock(return_value=httpx.Response(200, json=ok))
    client = VatSense(base_url=base_url, username="user", password="key")
    client.rates.list(provinces=False)
    assert route.calls.last.request.url.params["provinces"] == "false"
