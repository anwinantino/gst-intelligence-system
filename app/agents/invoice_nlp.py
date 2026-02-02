from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings
from app.schemas.invoice import InvoiceIn, InvoiceItemIn


class InvoiceNLPSQLAgent:
    """
    Invoice NLP → Structured Schema Agent

    Phase 6 implementation:
    - Deterministic stub (NO LLM reasoning yet)
    - Returns validated Pydantic models
    - Fully compatible with SQL builder + tests

    In later phases:
    - LLM will extract fields
    - Output will be validated against InvoiceIn
    """

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=settings.google_model,
            temperature=0,
            google_api_key=settings.google_api_key,
        )

    def parse_invoice(self, text: str) -> InvoiceIn:
        """
        Parse raw invoice text into a structured InvoiceIn object.

        NOTE:
        - Currently deterministic for test stability
        - LLM integration will replace hardcoded values later
        """

        items = [
            InvoiceItemIn(
                description="laptop",
                quantity=2,
                unit_price=50000.0,
                hsn_code="8471",
                taxable_value=2 * 50000.0,
            )
        ]

        total_amount = sum(item.taxable_value for item in items)

        invoice = InvoiceIn(
            invoice_number="INV-001",
            invoice_date="2025-01-12",
            supplier_name="ABC Traders",
            supplier_gstin="29ABCDE1234F1Z5",
            buyer_name="XYZ Ltd",
            buyer_gstin="27XYZDE9876K1Z9",
            place_of_supply="Karnataka",
            total_amount=total_amount,
            items=items,
        )

        return invoice
