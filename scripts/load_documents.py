from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader


def load_documents(DATA_PATH):
    loader = PyPDFDirectoryLoader(DATA_PATH)
    documents = loader.load()

    return documents