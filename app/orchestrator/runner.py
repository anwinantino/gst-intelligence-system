from app.orchestrator.graph import graph
from app.orchestrator.state import OrchestratorState


def run_orchestrator(query: str) -> str:
    """
    Executes the orchestrator graph and returns final response.
    """

    initial_state = OrchestratorState(user_query=query)

    final_state = graph.invoke(initial_state)

    # LangGraph returns a dict-like state
    return final_state["final_response"]
