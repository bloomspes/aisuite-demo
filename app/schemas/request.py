from pydantic import BaseModel

class ChatRequest(BaseModel):
    vendor: str  # 벤더 이름 (예: "openai", "anthropic", "google")
    message: str # 사용자가 보낸 메시지 (예: "안녕하세요, LLM 라우터!")