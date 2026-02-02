from typing import Dict
from pydantic import BaseModel, Field

class GSTCalculationInput(BaseModel):
    taxable_value: float = Field(..., gt=0)
    gst_rate: float = Field(..., ge=0, le=100)

    supplier_state: str
    recipient_state: str

class GSTCalculationResult(BaseModel):
    tax_type: str  # CGST_SGST or IGST

    cgst_rate: float = 0.0
    sgst_rate: float = 0.0
    igst_rate: float = 0.0

    cgst_amount: float = 0.0
    sgst_amount: float = 0.0
    igst_amount: float = 0.0

    total_tax: float
    total_amount: float

def calculate_gst(data: GSTCalculationInput) -> GSTCalculationResult:
    """
    Pure GST computation.
    No rules. No fetching. No guessing.
    """

    intra_state = data.supplier_state.lower() == data.recipient_state.lower()

    if intra_state:
        half_rate = data.gst_rate / 2

        cgst_amount = data.taxable_value * half_rate / 100
        sgst_amount = data.taxable_value * half_rate / 100

        total_tax = cgst_amount + sgst_amount

        return GSTCalculationResult(
            tax_type="CGST_SGST",
            cgst_rate=half_rate,
            sgst_rate=half_rate,
            cgst_amount=round(cgst_amount, 2),
            sgst_amount=round(sgst_amount, 2),
            total_tax=round(total_tax, 2),
            total_amount=round(data.taxable_value + total_tax, 2),
        )

    else:
        igst_amount = data.taxable_value * data.gst_rate / 100

        return GSTCalculationResult(
            tax_type="IGST",
            igst_rate=data.gst_rate,
            igst_amount=round(igst_amount, 2),
            total_tax=round(igst_amount, 2),
            total_amount=round(data.taxable_value + igst_amount, 2),
        )

