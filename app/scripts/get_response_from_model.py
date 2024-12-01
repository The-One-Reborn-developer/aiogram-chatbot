import os

from dotenv import load_dotenv, find_dotenv

from app.scripts.load_query_from_chroma import load_query_from_chroma
from app.scripts.pass_prompt_to_model import pass_prompt_to_model


def get_response_from_model(message) -> str:
    load_dotenv(find_dotenv())

    chroma_path = os.getenv("CHROMA_PATH")

    result = load_query_from_chroma(chroma_path, message)

    context_text = '\n\n---\n\n'.join([
        document.page_content for document, _score in result
    ])
    sources = [
        document.metadata.get('source', None) for document, _score in result
    ]

    model_response = pass_prompt_to_model(
        context_text,
        message,
        sources
    )

    return model_response