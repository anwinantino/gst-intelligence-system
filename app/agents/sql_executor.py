from sqlalchemy.orm import Session
from app.db.models import Invoice, InvoiceItem
from app.schemas.sql_output import SQLPlan


def execute_plan(plan: SQLPlan, db: Session):
    invoice_id = None

    for stmt in plan.statements:
        if stmt.table == "invoices":
            invoice = Invoice(**stmt.values)
            db.add(invoice)
            db.flush()
            invoice_id = invoice.id

        elif stmt.table == "invoice_items":
            item = InvoiceItem(
                invoice_id=invoice_id,
                **stmt.values
            )
            db.add(item)

    db.commit()
