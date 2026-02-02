from pydantic import BaseModel
from typing import Literal


class IntentResult(BaseModel):
    intent: Literal[
        "invoice_parse",
        "gst_query",
        "gst_calculation",
        "unknown",
    ]
