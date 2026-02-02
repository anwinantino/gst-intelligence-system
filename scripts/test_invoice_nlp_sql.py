from app.agents.invoice_nlp import InvoiceNLPSQLAgent
from app.agents.sql_builder import build_insert_plan

def main():
    text = """
    Invoice INV-009 dated 2025-02-01.
    Supplier: ABC Traders, GSTIN 29ABCDE1234F1Z5
    Buyer: XYZ Ltd, GSTIN 27XYZDE9876K1Z9
    Sold 3 laptops at 45000 each.
    Place of supply: Karnataka.
    """

    agent = InvoiceNLPSQLAgent()
    invoice = agent.parse_invoice(text)

    print("\n===== PARSED INVOICE =====")
    print(invoice.model_dump())

    plan = build_insert_plan(invoice)

    print("\n===== GENERATED SQL PLAN =====")
    for stmt in plan.statements:
        print(stmt.dict())

if __name__ == "__main__":
    main()
