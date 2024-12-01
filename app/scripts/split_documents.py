from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_documents(documents) -> list:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=30,
        length_function=len,
        add_start_index=True
    )
    
    return text_splitter.split_documents(documents)