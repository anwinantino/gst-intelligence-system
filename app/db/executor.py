from sqlalchemy import text
from app.db.session import SessionLocal
from app.agents.sql_builder import SQLPlan


def execute_sql_plan(plan: SQLPlan) -> None:
    """
    Executes a SQLPlan in a single transaction.
    Handles invoice -> invoice_items foreign key correctly.
    """

    session = SessionLocal()

    try:
        invoice_id = None

        for stmt in plan.statements:
            # 1️⃣ Insert invoice FIRST
            if stmt.table == "invoices" and stmt.operation == "insert":
                columns = ", ".join(stmt.values.keys())
                placeholders = ", ".join(f":{k}" for k in stmt.values.keys())

                sql = f"""
                INSERT INTO invoices ({columns})
                VALUES ({placeholders})
                """

                result = session.execute(text(sql), stmt.values)

                # 🔥 Capture generated invoice ID
                invoice_id = result.lastrowid

            # 2️⃣ Insert invoice items with FK
            elif stmt.table == "invoice_items" and stmt.operation == "insert":
                if invoice_id is None:
                    raise RuntimeError("Invoice ID not available for invoice_items")

                values = dict(stmt.values)
                values["invoice_id"] = invoice_id

                columns = ", ".join(values.keys())
                placeholders = ", ".join(f":{k}" for k in values.keys())

                sql = f"""
                INSERT INTO invoice_items ({columns})
                VALUES ({placeholders})
                """

                session.execute(text(sql), values)

        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()
