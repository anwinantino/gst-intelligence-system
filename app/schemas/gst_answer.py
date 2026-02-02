from pydantic import BaseModel
from typing import List


class GSTAnswer(BaseModel):
    answer: str
    sources: List[str]