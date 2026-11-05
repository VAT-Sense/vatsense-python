# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ValidateCheckResponse",
    "Data",
    "DataCompany",
    "DataCompanyValidationCompany",
    "DataCompanyEoriValidationCompany",
    "DataMatch",
    "DataMatchFields",
]


class DataCompanyValidationCompany(BaseModel):
    company_address: Optional[str] = None

    company_name: Optional[str] = None

    country_code: Optional[str] = None

    vat_number: Optional[str] = None
    """The VAT number (without country code prefix)."""


class DataCompanyEoriValidationCompany(BaseModel):
    company_address: Optional[str] = None

    company_name: Optional[str] = None

    country_code: Optional[str] = None

    eori_number: Optional[str] = None
    """The EORI number (without country code prefix)."""


DataCompany: TypeAlias = Union[DataCompanyValidationCompany, DataCompanyEoriValidationCompany]


class DataMatchFields(BaseModel):
    result: Optional[Literal["match", "partial", "no_match", "not_applicable"]] = None

    score: Optional[int] = None

    vies: Optional[Literal["valid", "invalid", "not_processed"]] = None
    """
    VIES's own answer for that detail on a live EU check; null when VIES said
    nothing.
    """


class DataMatch(BaseModel):
    fields: Optional[Dict[str, DataMatchFields]] = None
    """
    One entry for each detail sent (company_name, address, street, postcode,
    city).
    """

    result: Optional[Literal["likely", "possible", "unlikely", "not_applicable"]] = None
    """
    likely (a score of 80 or more, and the name, if sent, is not a no_match),
    possible (50 to 79), unlikely (under 50), or not_applicable when nothing could
    be compared.
    """

    score: Optional[int] = None
    """The average of the details sent, with the name counting twice.

    null when not_applicable.
    """


class Data(BaseModel):
    company: Optional[DataCompany] = None

    consultation_number: Optional[str] = None
    """
    Official consultation number (only returned when requester_vat_number is
    provided).
    """

    match: Optional[DataMatch] = None
    """Only when a `match_` parameter was sent."""

    valid: Optional[bool] = None
    """Whether the VAT/EORI number is valid."""


class ValidateCheckResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    success: Optional[bool] = None
