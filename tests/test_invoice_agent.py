from app.agents.invoice_nlp_agent import InvoiceNLPSQLAgent
from app.agents.sql_builder import build_insert_plan


def test_invoice_parsing():
    text = """
    Invoice INV-001 dated 2025-01-12.
    Supplier: ABC Traders, GSTIN 29ABCDE1234F1Z5
    Buyer: XYZ Ltd, GSTIN 27XYZDE9876K1Z9
    Sold 2 laptops at 50000 each.
    Place of supply: Karnataka.
    """

    agent = InvoiceNLPSQLAgent()
    invoice = agent.parse_invoice(text)

    plan = build_insert_plan(invoice)

    assert plan.statements[0].table == "invoices"