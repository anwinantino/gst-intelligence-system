from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate

from app.core.config import settings
from app.orchestrator.schemas import IntentResult


_llm = ChatGoogleGenerativeAI(
    model=settings.google_model,
    temperature=0,
    google_api_key=settings.google_api_key,
)


_parser = PydanticOutputParser(pydantic_object=IntentResult)


_prompt = ChatPromptTemplate.from_template(
    """
You are an intent classifier for a GST intelligence system.

Classify the user query into ONE intent from:
- invoice_parse
- gst_query
- gst_calculation
- unknown

User query:
{query}

{format_instructions}
"""
)


def classify_intent(query: str) -> str:
    chain = _prompt | _llm | _parser
    result: IntentResult = chain.invoke(
        {
            "query": query,
            "format_instructions": _parser.get_format_instructions(),
        }
    )
    return result.intent
