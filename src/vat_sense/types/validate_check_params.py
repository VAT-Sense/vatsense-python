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

    match_address: str
    """
    The whole address you hold, as one line, matched against the registered
    address.
    """

    match_city: str
    """The town or city you hold, looked for in the registered address."""

    match_company_name: str
    """The company name you hold, matched against the registered name.

    Legal forms such as Ltd or GmbH, accents, punctuation and word order are
    ignored. Sending any `match_` parameter adds `match` to the response; matching
    costs nothing extra.
    """

    match_postcode: str
    """The postcode you hold, looked for in the registered address.

    Spaces are ignored.
    """

    match_street: str
    """The street line you hold, looked for in the registered address."""

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
