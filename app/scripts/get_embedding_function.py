from langchain_ollama import OllamaEmbeddings


def get_embedding_function() -> OllamaEmbeddings:
    return OllamaEmbeddings(model="bge-m3")