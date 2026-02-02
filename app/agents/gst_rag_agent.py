from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser

from app.schemas.get_rag import GSTAnswer
from app.agents.gst_prompt import SYSTEM_PROMPT


class GSTRAGAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-latest",
            temperature=0,
        )
        self.parser = PydanticOutputParser(
            pydantic_object=GSTAnswer
        )

    def answer(self, query: str, context_chunks: list[str]) -> GSTAnswer:
        context = "\n\n".join(context_chunks)

        prompt = (
            SYSTEM_PROMPT
            + "\n\nContext:\n"
            + context
            + "\n\n"
            + self.parser.get_format_instructions()
            + "\n\nQuestion:\n"
            + query
        )

        response = self.llm.invoke(prompt)
        return self.parser.parse(response.content)
