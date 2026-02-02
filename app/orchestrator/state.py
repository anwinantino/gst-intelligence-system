from typing import Optional, Dict, Any
from pydantic import BaseModel


class OrchestratorState(BaseModel):
    user_query: str

    intent: Optional[str] = None  # invoice | gst | combined

    invoice_result: Optional[Dict[str, Any]] = None
    gst_result: Optional[Dict[str, Any]] = None

    final_response: Optional[str] = None