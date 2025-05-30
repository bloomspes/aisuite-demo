from typing import AsyncGenerator
from aisuite import Client
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 API 키를 로드하도록 설정

client = Client()  # API 키는 환경변수 또는 .env 파일에서 로드됨

# 간단한 모델 선택 전략
def select_model(vendor: str, message: str) -> str:
    if vendor:
        return f"{vendor}:gpt-4o" if vendor == "openai" else f"{vendor}:claude-3-5-sonnet-20240620"
    if len(message) < 50:
        return "anthropic:claude-3-5-sonnet-20240620"
    return "openai:gpt-4o"

# 벤더에 따라 chunk 파싱 방식이 다르므로 헬퍼 함수로 분리
def extract_content(vendor: str, chunk) -> str:
    if vendor.startswith("openai"):
        return chunk.choices[0].delta.content or ""
    elif vendor.startswith("anthropic"):
        return chunk.delta.content or ""
    return ""

# 메인 함수
async def call_with_fallback(
    message: str, vendor: str = "", session_id: str = ""
) -> AsyncGenerator[str, None]:
    model = select_model(vendor, message)
    chosen_vendor = model.split(":")[0]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": message}],
            stream=True,
        )
        async for chunk in response:
            yield extract_content(chosen_vendor, chunk)

    except Exception as e:
        print(f"❗ Primary vendor failed: {e}")
        fallback_model = (
            "openai:gpt-4o" if chosen_vendor == "anthropic" else "anthropic:claude-3-5-sonnet-20240620"
        )
        fallback_vendor = fallback_model.split(":")[0]
        try:
            response = client.chat.completions.create(
                model=fallback_model,
                messages=[{"role": "user", "content": message}],
                stream=True,
            )
            async for chunk in response:
                yield extract_content(fallback_vendor, chunk)
        except Exception as fallback_error:
            print(f"❌ Fallback vendor failed: {fallback_error}")
            yield "❗ 모든 LLM 벤더 요청에 실패했습니다."
