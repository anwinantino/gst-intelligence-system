from pydantic import BaseModel
from typing import List


class GSTRuleChunk(BaseModel):
    source: str           # e.g. "CGST Act"
    section: str          # e.g. "Section 9"
    description: str      # Short rule description
    content: str          # Actual text


class GSTAnswer(BaseModel):
    answer: str
    cited_rules: List[str]   # Human-readable citations
