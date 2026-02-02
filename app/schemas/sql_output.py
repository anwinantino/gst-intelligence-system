from pydantic import BaseModel
from typing import List


class SQLStatement(BaseModel):
    table: str
    operation: str  # insert | select
    values: dict | None = None
    where: dict | None = None


class SQLPlan(BaseModel):
    statements: List[SQLStatement]
