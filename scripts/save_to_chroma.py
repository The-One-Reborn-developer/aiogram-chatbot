import os
import shutil

from langchain_chroma import Chroma

from dotenv import load_dotenv, find_dotenv

from load_documents import load_documents
from split_documents import split_documents
from get_embedding_function import get_embedding_function


def save_to_chroma(chunks, chroma_path) -> bool:
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)

    try:
        Chroma.from_documents(
            chunks,
            embedding=get_embedding_function(),
            persist_directory=chroma_path,
        )
    except Exception as e:
        print(e)
        return False

    print(f'Saved {len(chunks)} chunks to {chroma_path}')
    return True


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    documents = load_documents(os.getenv("DATA_PATH"))
    chunks = split_documents(documents)
    chroma_path = os.getenv("CHROMA_PATH")
    
    result = save_to_chroma(chunks, chroma_path)

    if not result:
        print('Failed to save to chroma')
        exit(1)

    exit(0)