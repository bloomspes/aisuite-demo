from aisuite import Client
import os

_client_cache = {}

def get_client(vendor: str) -> Client:
    if vendor in _client_cache:
        return _client_cache[vendor]

    if vendor == "openai":
        client = Client(
            vendor="openai",
            config={"api_key": os.getenv("OPENAI_API_KEY")}
        )
    elif vendor == "anthropic":
        client = Client(
            vendor="anthropic",
            config={"api_key": os.getenv("ANTHROPIC_API_KEY")}
        )
    else:
        raise ValueError(f"지원하지 않는 vendor: {vendor}")

    _client_cache[vendor] = client
    return client
