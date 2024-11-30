import os
import argparse

from langchain_chroma import Chroma

from dotenv import load_dotenv, find_dotenv

from scripts.get_embedding_function import get_embedding_function


def load_query_from_chroma(chroma_path, query_text) -> list:
    load_dotenv(find_dotenv())

    chroma_path = os.getenv("CHROMA_PATH")

    parser = argparse.ArgumentParser()
    parser.add_argument('query_text', type=str, help='Query text')
    args = parser.parse_args()
    query_text = args.query_text

    db = Chroma(persist_directory=chroma_path, embedding_function=get_embedding_function())

    result = db.similarity_search_with_relevance_scores(
        query_text,
        k=3
    )

    if len(result) == 0 or result[0][1] < 0.3:
        print('Unable to find matching results')
        return

    return result