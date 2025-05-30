from fastapi import Request
from sse_starlette.sse import EventSourceResponse
from typing import AsyncGenerator

def sse_format(data: str, event: str = "message") -> str:
    return f"event: {event}\ndata: {data}\n\n"

async def stream_as_sse(generator: AsyncGenerator[str, None], request: Request):
    async def event_publisher():
        async for chunk in generator:
            yield {"event": "message", "data": chunk}
            if await request.is_disconnected():
                break
    return EventSourceResponse(event_publisher())
