from pydantic import BaseModel
from typing import List


class InvoiceItemIn(BaseModel):
    description: str
    quantity: int
    unit_price: float
    hsn_code: str
    taxable_value: float   # ✅ ADD THIS


class InvoiceIn(BaseModel):
    invoice_number: str
    invoice_date: str
    supplier_name: str
    supplier_gstin: str
    buyer_name: str
    buyer_gstin: str
    place_of_supply: str
    total_amount: float
    items: List[InvoiceItemIn]
