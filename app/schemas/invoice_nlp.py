from pydantic import BaseModel, Field
from typing import List
from datetime import date
from decimal import Decimal


class InvoiceItemIn(BaseModel):
    description: str
    hsn_code: str
    quantity: Decimal
    unit_price: Decimal
    taxable_value: Decimal


class InvoiceIn(BaseModel):
    invoice_number: str
    invoice_date: date

    supplier_name: str
    supplier_gstin: str

    buyer_name: str
    buyer_gstin: str | None

    place_of_supply: str
    total_amount: Decimal

    items: List[InvoiceItemIn]
