import os
import json
import redis.asyncio as redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
SESSION_PREFIX = "chat:"

redis_client = redis.from_url(REDIS_URL, decode_responses=True)

async def save_message(session_id: str, role: str, content: str):
    key = SESSION_PREFIX + session_id
    message = {"role": role, "content": content}
    await redis_client.rpush(key, json.dumps(message))

async def load_history(session_id: str) -> list[dict]:
    key = SESSION_PREFIX + session_id
    items = await redis_client.lrange(key, 0, -1)
    return [json.loads(item) for item in items]

async def reset_session(session_id: str):
    key = SESSION_PREFIX + session_id
    await redis_client.delete(key)
