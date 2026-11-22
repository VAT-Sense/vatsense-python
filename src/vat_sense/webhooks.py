"""Checking the signature of VAT Sense webhook events.

Every event is a signed JSON ``POST`` with a ``VatSense-Signature`` header such as
``t=1793365200,v1=5257a8...``: ``v1`` is the hex HMAC-SHA256 of the timestamp, a
full stop and the raw request body, keyed with the endpoint's signing secret
(``whsec_...``). For 24 hours after a secret is rolled the header carries a second
``v1``, so any match is accepted.

    from vat_sense.webhooks import construct_event, WebhookSignatureError

    try:
        event = construct_event(request.body, request.headers["VatSense-Signature"], secret)
    except WebhookSignatureError:
        return 400
"""

from __future__ import annotations

import hmac
import json
import time
import hashlib
from typing import Any, Dict, List, Union, Optional

from ._exceptions import VatSenseError

__all__ = ["SIGNATURE_HEADER", "DEFAULT_TOLERANCE", "WebhookSignatureError", "verify_signature", "construct_event"]

SIGNATURE_HEADER = "VatSense-Signature"
"""The name of the header that carries the signature."""

DEFAULT_TOLERANCE = 300
"""Events whose timestamp is more than this many seconds from now are refused."""


class WebhookSignatureError(VatSenseError):
    """The event's signature is missing, malformed, too old or does not match."""


def _parse_header(header: str) -> "tuple[int, List[str]]":
    timestamp: Optional[int] = None
    signatures: List[str] = []
    for part in header.split(","):
        key, sep, value = part.strip().partition("=")
        if not sep:
            continue
        if key == "t":
            try:
                timestamp = int(value)
            except ValueError:
                raise WebhookSignatureError("The signature header's timestamp is not a number.") from None
        elif key == "v1" and value:
            signatures.append(value)
    if timestamp is None:
        raise WebhookSignatureError("The signature header has no timestamp.")
    if not signatures:
        raise WebhookSignatureError("The signature header has no v1 signature.")
    return timestamp, signatures


def verify_signature(
    payload: Union[str, bytes],
    header: Optional[str],
    secret: str,
    *,
    tolerance: Optional[int] = DEFAULT_TOLERANCE,
    now: Optional[int] = None,
) -> None:
    """Check an event's ``VatSense-Signature`` header against its raw body.

    Args:
      payload: The raw request body, exactly as received (not parsed and re-encoded).

      header: The value of the ``VatSense-Signature`` header.

      secret: The endpoint's signing secret, starting ``whsec_``.

      tolerance: Refuse events signed more than this many seconds ago (default 300).
          ``None`` skips the check.

      now: The current Unix time, for tests.

    Raises:
      WebhookSignatureError: when the header is missing or malformed, the event is too
          old, or no ``v1`` signature matches.
    """
    if not header:
        raise WebhookSignatureError("The VatSense-Signature header is missing.")
    if not secret:
        raise WebhookSignatureError("No signing secret was given.")
    body = payload.encode("utf-8") if isinstance(payload, str) else payload
    timestamp, signatures = _parse_header(header)

    current = int(time.time()) if now is None else now
    if tolerance is not None and abs(current - timestamp) > tolerance:
        raise WebhookSignatureError("The event's timestamp is outside the tolerance.")

    expected = hmac.new(
        secret.encode("utf-8"), str(timestamp).encode("ascii") + b"." + body, hashlib.sha256
    ).hexdigest()
    if not any(hmac.compare_digest(expected, signature) for signature in signatures):
        raise WebhookSignatureError("No signature matches the payload.")


def construct_event(
    payload: Union[str, bytes],
    header: Optional[str],
    secret: str,
    *,
    tolerance: Optional[int] = DEFAULT_TOLERANCE,
    now: Optional[int] = None,
) -> Dict[str, Any]:
    """Check the signature, then return the event (``id``, ``type``, ``created``, ``livemode``, ``data``)."""
    verify_signature(payload, header, secret, tolerance=tolerance, now=now)
    event: Any = json.loads(payload)
    if not isinstance(event, dict):
        raise WebhookSignatureError("The payload is not a JSON object.")
    return event  # type: ignore[return-value]
