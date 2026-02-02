from app.schemas.sql_output import SQLPlan, SQLStatement
from app.schemas.invoice import InvoiceIn


def build_insert_plan(invoice: InvoiceIn) -> SQLPlan:
    statements = []

    statements.append(
        SQLStatement(
            table="invoices",
            operation="insert",
            values={
                "invoice_number": invoice.invoice_number,
                "supplier_name": invoice.supplier_name,
                "supplier_gstin": invoice.supplier_gstin,
                "buyer_name": invoice.buyer_name,
                "buyer_gstin": invoice.buyer_gstin,
                "invoice_date": invoice.invoice_date,
                "place_of_supply": invoice.place_of_supply,
                "total_amount": invoice.total_amount,
            },
        )
    )

    for item in invoice.items:
        statements.append(
            SQLStatement(
                table="invoice_items",
                operation="insert",
                values={
                    "description": item.description,
                    "hsn_code": item.hsn_code,
                    "quantity": item.quantity,
                    "unit_price": item.unit_price,
                    "taxable_value": item.taxable_value,
                },
            )
        )

    return SQLPlan(statements=statements)
