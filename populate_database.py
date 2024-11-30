import os

from dotenv import load_dotenv, find_dotenv

from app.scripts.load_documents import load_documents
from app.scripts.split_documents import split_documents

from app.scripts.save_to_chroma import save_to_chroma


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    documents = load_documents(os.getenv("DATA_PATH"))
    
    
    chunks = split_documents(documents)

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get('source', None)
        page = chunk.metadata.get('page', None)
        current_page_id = f'{source}:{page}'

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk.metadata['id'] = current_page_id
    
    chroma_path = os.getenv("CHROMA_PATH")
    
    result = save_to_chroma(chunks, chroma_path)

    if not result:
        print('Failed to save to chroma')
        exit(1)

    exit(0)