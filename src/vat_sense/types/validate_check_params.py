# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ValidateCheckParams"]


class ValidateCheckParams(TypedDict, total=False):
    eori_number: str
    """The EORI number to validate.

    Must include the leading 2-character country code (e.g. "GB123456789123"). UK
    and EU only.
    """

    requester_vat_number: str
    """Your own VAT number.

    If supplied, the response will include a unique consultation number issued by
    the relevant authority (VIES or HMRC). Must include the leading 2-character
    country code.

    Note: GB requester numbers only work for GB validations; EU requester numbers
    only work for EU validations. Cross-region is not supported.
    """

    vat_number: str
    """The VAT number to validate.

    Must include the leading 2-character country code (e.g. "GB288305674",
    "FR12345678901").
    """
