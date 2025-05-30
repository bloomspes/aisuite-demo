from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.request import ChatRequest
from app.services.llm_router import get_llm_response_stream


router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    generator = get_llm_response_stream(request.vendor, request.message)
    return StreamingResponse(generator, media_type="text/event-stream")