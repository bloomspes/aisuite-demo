from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.schemas.request import ChatRequest
from app.services.llm_router import get_llm_response_stream
from app.core.exceptions import LLMServiceError

import logging


router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    """채팅 요청을 처리하고 스트리밍 응답을 반환합니다."""
    try:
        stream = await get_llm_response_stream(request.vendor, request.message)
        return StreamingResponse(stream, media_type="text/event-stream")
    except LLMServiceError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.log.error(f"Chat stream error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")