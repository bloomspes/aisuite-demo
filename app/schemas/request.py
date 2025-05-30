from typing import Optional
from pydantic import BaseModel

class ChatRequest(BaseModel):
    vendor: Optional[str] = ""
    message: str
    session_id: Optional[str] = None