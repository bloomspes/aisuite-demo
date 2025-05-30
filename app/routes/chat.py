from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from app.schemas.request import ChatRequest
from app.services.llm_router import call_with_fallback
from app.utils.streaming import sse_format, stream_as_sse

router = APIRouter(prefix="/chat")

@router.post("/stream")
async def stream_chat(request: Request, chat: ChatRequest):
    if not chat.message:
        def error_stream():
            yield "data: ❗ 메시지가 비어있습니다.\n\n"
        return StreamingResponse(error_stream(), media_type="text/event-stream")

    generator = call_with_fallback(chat.message, chat.vendor, chat.session_id)
    return await stream_as_sse(generator, request)