from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser

from app.schemas.invoice_nlp import InvoiceIn
from app.agents.prompt import SYSTEM_PROMPT


class InvoiceNLPSQLAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-latest",
            temperature=0,
        )
        self.parser = PydanticOutputParser(pydantic_object=InvoiceIn)

    def parse_invoice(self, text: str) -> InvoiceIn:
        prompt = (
            SYSTEM_PROMPT
            + "\n\n"
            + self.parser.get_format_instructions()
            + "\n\nInvoice Text:\n"
            + text
        )

        response = self.llm.invoke(prompt)
        return self.parser.parse(response.content)
