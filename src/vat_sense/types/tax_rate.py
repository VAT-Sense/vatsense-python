# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TaxRate"]


class TaxRate(BaseModel):
    class_: Optional[str] = FieldInfo(alias="class", default=None)
    """The rate class (e.g. "standard", "reduced", "zero")."""

    description: Optional[str] = None
    """A description of what goods/services this rate applies to."""

    object: Optional[Literal["tax_rate"]] = None

    rate: Optional[float] = None
    """The tax rate percentage."""

    types: Union[str, bool, None] = None
    """
    Comma-separated list of product types this rate applies to, or false if it
    applies generally.
    """
