from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf import loader_pdf

splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)

def chunker():
    docs=loader_pdf()
    splitted_chunks=splitter.split_documents(docs)
    if not splitted_chunks:
        raise ValueError("No texts to be found in document")
    return splitted_chunks