import os
import shutil

from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter

from dotenv import load_dotenv, find_dotenv


def load_documents(DATA_PATH):
    loader = PyPDFDirectoryLoader(DATA_PATH)
    documents = loader.load()

    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=30,
        length_function=len,
        add_start_index=True
    )
    return text_splitter.split_documents(documents)


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