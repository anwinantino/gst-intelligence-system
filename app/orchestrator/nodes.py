from app.agents.gst_rag_agent import answer_gst_query

from app.orchestrator.state import OrchestratorState
from app.orchestrator.intent import classify_intent

from app.agents.invoice_nlp import InvoiceNLPSQLAgent
from app.agents.sql_builder import build_insert_plan
from app.db.executor import execute_sql_plan


# -------------------------
# 1️⃣ Intent Node
# -------------------------
def intent_node(state: OrchestratorState) -> OrchestratorState:
    state.intent = classify_intent(state.user_query)
    return state


# -------------------------
# 2️⃣ Invoice Node
# -------------------------
def invoice_node(state):
    agent = InvoiceNLPSQLAgent()

    # Parse invoice text → structured object
    invoice = agent.parse_invoice(state.user_query)

    # Build SQL execution plan
    plan = build_insert_plan(invoice)

    # 🔥 WRITE TO DATABASE (Phase 10)
    execute_sql_plan(plan)

    # Update orchestrator state
    state.invoice_result = {
        "status": "inserted",
        "invoice_number": invoice.invoice_number,
        "sql_statements": len(plan.statements),
    }

    return state


# -------------------------
# 3️⃣ GST Node
# -------------------------
def gst_node(state):
    """
    Executes GST RAG pipeline if intent is GST-related
    """
    result = answer_gst_query(state.user_query)

    state.gst_result = {
        "status": "answered",
        "answer": result["answer"],
        "sources": result["sources"],
    }

    return state



# -------------------------
# 4️⃣ Final Response Node
# -------------------------
def response_node(state):
    if state.invoice_result:
        state.final_response = (
            f"Invoice {state.invoice_result['invoice_number']} parsed successfully.\n"
            f"SQL statements generated: {state.invoice_result['sql_statements']}"
        )
        return state

    if state.gst_result:
        state.final_response = (
            state.gst_result["answer"]
            + "\n\nSOURCES:\n"
            + "\n".join(state.gst_result["sources"])
        )
        return state

    state.final_response = "No handler matched the query."
    return state
 


