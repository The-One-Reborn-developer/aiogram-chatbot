import os
import shutil

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from dotenv import load_dotenv, find_dotenv

from scripts.load_documents import load_documents
from scripts.split_documents import split_documents


def save_to_chroma(chunks, chroma_path):
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)

    db = Chroma.from_documents(
        chunks,
        OllamaEmbeddings(model="nomic-embed-text"),
        persist_directory=chroma_path,
    )

    print(f'Saved {len(chunks)} chunks to {chroma_path}')


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    documents = load_documents(os.getenv("DATA_PATH"))
    chunks = split_documents(documents)
    chroma_path = os.getenv("CHROMA_PATH")
    
    try:
        save_to_chroma(chunks, chroma_path)
    except Exception as e:
        print(e)