from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings
from app.rag.retriever import retrieve_gst_context
from app.schemas.gst_answer import GSTAnswer


SYSTEM_PROMPT = """
You are a GST law expert.

Answer the question using ONLY the provided GST document excerpts.

Rules:
- Do NOT hallucinate tax rates or rules.
- If the documents contain relevant legal, procedural, or rate-related information,
  summarize it clearly in plain English.
- You may paraphrase.
- Cite document pages used.
- Only say "Not found in GST documents" if the excerpts are completely unrelated
  to the question.
"""


class GSTRAGAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=settings.google_model,
            temperature=0,
            google_api_key=settings.google_api_key,
        )

    def answer(self, query: str) -> GSTAnswer:
        contexts = retrieve_gst_context(query)

        if not contexts:
            return GSTAnswer(
                answer="Not found in GST documents.",
                sources=[],
            )

        context_text = "\n\n".join(
            f"(Page {c['page']}) {c['text']}" for c in contexts
        )

        prompt = f"""
{SYSTEM_PROMPT}

CONTEXT:
{context_text}

QUESTION:
{query}

ANSWER:
"""

        response = self.llm.invoke(prompt).content.strip()

        sources = [
            f"GST Document Page {c['page']}" for c in contexts if c.get("page") is not None
        ]

        return GSTAnswer(
            answer=response,
            sources=list(set(sources)),
        )
    
def answer_gst_query(query: str) -> dict:
    """
    Functional wrapper for orchestrator.
    Keeps orchestrator decoupled from class implementation.
    """
    agent = GSTRAGAgent()
    result = agent.answer(query)

    return {
        "answer": result.answer,
        "sources": result.sources,
    }