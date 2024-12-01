import os
import logging

from dotenv import load_dotenv, find_dotenv

from app.scripts.load_documents import load_documents
from app.scripts.split_documents import split_documents

from app.scripts.save_to_chroma import save_to_chroma


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logging.info("Loading environment variables")
    load_dotenv(find_dotenv())

    logging.info("Loading data")
    documents = load_documents(os.getenv("DATA_PATH"))
    
    logging.info("Splitting documents")
    chunks_with_ids = split_documents(documents)

    last_page_id = None
    current_chunk_index = 0

    logging.info("Adding metadata to chunks")
    for index, chunk in enumerate(chunks_with_ids):
        source = chunk.metadata.get('source', 'unknown_source')
        page = chunk.metadata.get('page', -1)
        chunk.metadata['id'] = f'{source}:{page}:{index}'
    
    logging.info("Saving to chroma")
    chroma_path = os.getenv("CHROMA_PATH")
    
    result = save_to_chroma(chunks_with_ids, chroma_path)

    if not result:
        logging.error("Failed to save to chroma")
        exit(1)

    exit(0)