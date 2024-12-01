import logging

from langchain_chroma import Chroma

from app.scripts.get_embedding_function import get_embedding_function


def save_to_chroma(chunks_with_ids, chroma_path) -> bool:
    try:
        db = Chroma(
            embedding_function=get_embedding_function(),
            persist_directory=chroma_path,
        )

        # Get existing document ids
        existing_documents = db.get(include=[])
        existing_ids = set(existing_documents['ids'])
        logging.info(f'Number of existing documents in Chroma: {len(existing_ids)}')
    
        # Filter out duplicate chunks
        new_chunks = [chunk for chunk in chunks_with_ids if chunk.metadata['id'] not in existing_ids]

        if not new_chunks:
            logging.info('No new chunks to save to Chroma')
            return True

        # Only add new chunks
        new_chunks_ids = [chunk.metadata['id'] for chunk in new_chunks]

        logging.info(f'Saving {len(new_chunks)} new documents to Chroma')
        db.add_documents(new_chunks, ids=new_chunks_ids)

        logging.info(f'Saved {len(new_chunks)} documents to Chroma')
        return True
    except Exception as e:
        logging.error(e)
        return False