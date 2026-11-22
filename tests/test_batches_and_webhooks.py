# Checks for the API additions of late November 2026 (batches, consultation_optional,
# confirmation_number, webhook signatures), sent through a mocked transport.

from __future__ import annotations

import hmac
import json
import hashlib
from typing import Any, Dict

import httpx
import pytest
from respx import MockRouter

from vat_sense import VatSense, AsyncVatSense
from vat_sense.webhooks import WebhookSignatureError, construct_event, verify_signature

base_url = "http://127.0.0.1:4010"

batch: Dict[str, Any] = {
    "object": "batch",
    "id": "01JM0000000000000000000000",
    "number": 4,
    "status": "processing",
    "livemode": True,
    "rows": {"total": 2, "to_check": 2, "done": 1},
    "results": {"valid": 1, "invalid": 0},
    "quote": None,
    "dashboard_url": "https://vatsense.com/dashboard/bulk/01JM0000000000000000000000",
}


def envelope(data: Any, code: int = 200) -> Dict[str, Any]:
    return {"success": True, "code": code, "data": data}


@pytest.mark.respx(base_url=base_url)
def test_batch_create_sends_body_and_idempotency_key(respx_mock: MockRouter) -> None:
    route = respx_mock.post("/batches").mock(return_value=httpx.Response(201, json=envelope(batch, 201)))
    client = VatSense(base_url=base_url, username="user", password="key")
    created = client.batches.create(
        numbers=["GB288305674", "DE100000040"], reference="November", shortfall="pause", idempotency_key="nov-1"
    )
    request = route.calls.last.request
    assert request.headers["Idempotency-Key"] == "nov-1"
    assert json.loads(request.content) == {
        "numbers": ["GB288305674", "DE100000040"],
        "reference": "November",
        "shortfall": "pause",
    }
    assert created.data.id == batch["id"]
    assert created.data.rows is not None and created.data.rows.done == 1


@pytest.mark.respx(base_url=base_url)
def test_batch_create_with_rows(respx_mock: MockRouter) -> None:
    route = respx_mock.post("/batches").mock(return_value=httpx.Response(201, json=envelope(batch, 201)))
    client = VatSense(base_url=base_url, username="user", password="key")
    client.batches.create(rows=[{"vat_number": "GB288305674", "company_name": "Weio Ltd"}], start=False)
    body = json.loads(route.calls.last.request.content)
    assert body == {"rows": [{"vat_number": "GB288305674", "company_name": "Weio Ltd"}], "start": False}
    assert "Idempotency-Key" not in route.calls.last.request.headers


@pytest.mark.respx(base_url=base_url)
def test_batch_list_and_actions(respx_mock: MockRouter) -> None:
    listed = respx_mock.get("/batches").mock(
        return_value=httpx.Response(
            200, json=envelope({"data": [batch], "page": 2, "limit": 10, "total": 11, "has_more": False})
        )
    )
    paths = {
        "retrieve": respx_mock.get(f"/batches/{batch['id']}"),
        "start": respx_mock.post(f"/batches/{batch['id']}/start"),
        "pause": respx_mock.post(f"/batches/{batch['id']}/pause"),
        "continue": respx_mock.post(f"/batches/{batch['id']}/continue"),
        "complete": respx_mock.post(f"/batches/{batch['id']}/complete"),
    }
    for route in paths.values():
        route.mock(return_value=httpx.Response(200, json=envelope(batch)))
    deleted = respx_mock.delete(f"/batches/{batch['id']}").mock(
        return_value=httpx.Response(200, json=envelope({"object": "batch", "id": batch["id"], "deleted": True}))
    )

    client = VatSense(base_url=base_url, username="user", password="key")
    page = client.batches.list(page=2, limit=10)
    assert listed.calls.last.request.url.params["page"] == "2"
    assert page.data.total == 11 and page.data.data[0].id == batch["id"]

    client.batches.retrieve(batch["id"])
    client.batches.start(batch["id"], shortfall="overage")
    assert json.loads(paths["start"].calls.last.request.content) == {"shortfall": "overage"}
    client.batches.pause(batch["id"])
    client.batches.continue_(batch["id"], shortfall="overage")
    assert json.loads(paths["continue"].calls.last.request.content) == {"shortfall": "overage"}
    client.batches.complete(batch["id"])
    assert all(route.called for route in paths.values())
    assert client.batches.delete(batch["id"]).data.deleted is True
    assert deleted.called


@pytest.mark.respx(base_url=base_url)
def test_batch_results_json_and_csv(respx_mock: MockRouter) -> None:
    rows = respx_mock.get(f"/batches/{batch['id']}/results").mock(
        return_value=httpx.Response(
            200,
            json=envelope(
                {
                    "data": [{"row": 1, "vat_number": "GB288305674", "result": "valid", "confirmation_number": None}],
                    "has_more": True,
                    "next_after": 1,
                }
            ),
        )
    )
    respx_mock.get(f"/batches/{batch['id']}/results.csv").mock(
        return_value=httpx.Response(200, text="row,vat_number\n1,GB288305674\n", headers={"Content-Type": "text/csv"})
    )
    client = VatSense(base_url=base_url, username="user", password="key")
    page = client.batches.results(batch["id"], after=0, limit=1)
    assert rows.calls.last.request.url.params["limit"] == "1"
    assert page.data.has_more and page.data.next_after == 1
    assert page.data.data[0].result == "valid"
    assert client.batches.results_csv(batch["id"]).startswith("row,vat_number")


@pytest.mark.respx(base_url=base_url)
async def test_async_batch_create(respx_mock: MockRouter) -> None:
    route = respx_mock.post("/batches").mock(return_value=httpx.Response(201, json=envelope(batch, 201)))
    client = AsyncVatSense(base_url=base_url, username="user", password="key")
    created = await client.batches.create(numbers=["GB288305674"])
    assert json.loads(route.calls.last.request.content) == {"numbers": ["GB288305674"]}
    assert created.data.livemode is True


def test_batch_id_must_not_be_empty() -> None:
    client = VatSense(base_url=base_url, username="user", password="key")
    with pytest.raises(ValueError):
        client.batches.retrieve("")


@pytest.mark.respx(base_url=base_url)
def test_validate_consultation_optional_and_confirmation_number(respx_mock: MockRouter) -> None:
    route = respx_mock.get("/validate").mock(
        return_value=httpx.Response(
            200, json=envelope({"valid": True, "confirmation_number": "VSC-ABC", "consultation_number": None})
        )
    )
    client = VatSense(base_url=base_url, username="user", password="key")
    result = client.validate.check(
        vat_number="FR40303265045", requester_vat_number="GB288305674", consultation_optional=True
    )
    assert route.calls.last.request.url.params["consultation_optional"] == "true"
    assert result.data is not None and result.data.confirmation_number == "VSC-ABC"


secret = "whsec_test_secret"
payload = (
    '{"id":"evt_1","type":"batch.completed","created":1793365200,"livemode":true,"data":{"object":{"object":"batch"}}}'
)


def sign(timestamp: int, body: str, key: str = secret) -> str:
    return hmac.new(key.encode(), f"{timestamp}.{body}".encode(), hashlib.sha256).hexdigest()


def test_webhook_signature_accepts_a_good_event() -> None:
    header = f"t=1793365200,v1={sign(1793365200, payload)}"
    event = construct_event(payload, header, secret, now=1793365260)
    assert event["type"] == "batch.completed"
    verify_signature(payload.encode(), header, secret, now=1793365260)


def test_webhook_signature_accepts_the_old_secret_during_a_roll() -> None:
    header = f"t=1793365200,v1={sign(1793365200, payload, 'whsec_new')},v1={sign(1793365200, payload)}"
    verify_signature(payload, header, secret, now=1793365200)


@pytest.mark.parametrize(
    "header,now",
    [
        (None, 1793365200),
        ("", 1793365200),
        ("v1=abc", 1793365200),
        ("t=1793365200", 1793365200),
        ("t=soon,v1=abc", 1793365200),
        (f"t=1793365200,v1={sign(1793365200, payload, 'whsec_other')}", 1793365200),
        (f"t=1793365200,v1={sign(1793365200, payload)}", 1793365200 + 301),
    ],
)
def test_webhook_signature_refuses_bad_events(header: Any, now: int) -> None:
    with pytest.raises(WebhookSignatureError):
        verify_signature(payload, header, secret, now=now)


def test_webhook_signature_refuses_a_changed_body() -> None:
    header = f"t=1793365200,v1={sign(1793365200, payload)}"
    with pytest.raises(WebhookSignatureError):
        verify_signature(payload.replace("true", "false"), header, secret, now=1793365200)
