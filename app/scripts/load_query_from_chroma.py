import logging

from langchain_chroma import Chroma

from dotenv import load_dotenv, find_dotenv

from app.scripts.get_embedding_function import get_embedding_function


def load_query_from_chroma(chroma_path, query_text, threshold=0.5) -> list:
    load_dotenv(find_dotenv())

    db = Chroma(persist_directory=chroma_path, embedding_function=get_embedding_function())

    result = db.similarity_search_with_relevance_scores(
        query_text,
        k=5
    )

    if len(result) == 0 or result[0][1] < threshold:
        logging.info("No relevant documents found")
        return []

    return result