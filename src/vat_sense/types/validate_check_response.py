# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "ValidateCheckResponse",
    "Data",
    "DataCompany",
    "DataCompanyValidationCompany",
    "DataCompanyEoriValidationCompany",
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


class Data(BaseModel):
    company: Optional[DataCompany] = None

    consultation_number: Optional[str] = None
    """
    Official consultation number (only returned when requester_vat_number is
    provided).
    """

    valid: Optional[bool] = None
    """Whether the VAT/EORI number is valid."""


class ValidateCheckResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    success: Optional[bool] = None
