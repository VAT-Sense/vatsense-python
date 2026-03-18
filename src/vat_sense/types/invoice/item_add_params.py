# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .invoice_item_input_param import InvoiceItemInputParam

__all__ = ["ItemAddParams"]


class ItemAddParams(TypedDict, total=False):
    items: Required[Iterable[InvoiceItemInputParam]]
