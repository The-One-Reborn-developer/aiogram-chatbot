import os
import shutil

from langchain_chroma import Chroma

from app.scripts.get_embedding_function import get_embedding_function


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