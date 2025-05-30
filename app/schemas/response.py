from pydantic import BaseModel

class ChatChunkDto(BaseModel):
    chunk: str  # LLM 응답의 청크