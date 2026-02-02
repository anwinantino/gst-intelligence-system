from langgraph.graph import StateGraph, END

from app.orchestrator.state import OrchestratorState
from app.orchestrator.nodes import (
    intent_node,
    invoice_node,
    gst_node,
    response_node,
)


def build_orchestrator_graph():
    """
    Final LangGraph orchestrator graph.
    """

    builder = StateGraph(OrchestratorState)

    # Node names MUST NOT match state keys
    builder.add_node("intent_router", intent_node)
    builder.add_node("invoice", invoice_node)
    builder.add_node("gst", gst_node)
    builder.add_node("response", response_node)

    builder.set_entry_point("intent_router")

    builder.add_conditional_edges(
        "intent_router",
        lambda state: state.intent,
        {
            "invoice_parse": "invoice",
            "gst_query": "gst",
            "gst_calculation": "invoice",
        },
    )

    builder.add_edge("invoice", "gst")
    builder.add_edge("gst", "response")
    builder.add_edge("response", END)

    return builder.compile()


# ✅ EXPORT
graph = build_orchestrator_graph()
