from typing import Literal
from pydantic import BaseModel

class ChatRequest(BaseModel):
    vendor: Literal["openai", "anthropic"]
    message: str