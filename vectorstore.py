from embedding import embedder
from langchain_chroma import Chroma
from chunking import chunker

vectorstoree=Chroma(collection_name="document_store",persist_directory="./vector_store",embedding_function=embedder)

chunks=chunker()
vectorstoree.add_documents(chunks)
 

