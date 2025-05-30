from aisuite.llms import ClientFactory

factory = ClientFactory()

def get_llm_client(vendor: str):
    return factory.create(vendor)
