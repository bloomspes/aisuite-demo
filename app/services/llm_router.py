from typing import AsyncGenerator
from app.llms.client_factory import get_llm_client

async def get_llm_response_stream(message: str) -> AsyncGenerator[str, None]:
   client = get_llm_client()
   async for chunk in client.chat_stream(message):
       yield f"data: {chunk}\n\n"