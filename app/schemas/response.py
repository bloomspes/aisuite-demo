from pydantic import BaseModel

class ChatChunkDto(BaseModel):
    content: str