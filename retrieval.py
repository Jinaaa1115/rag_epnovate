from vectorstore import vectorstoree
from embedding import embedder
def retrieve_chunks(query:str,k:int=4):
    

    retrieved_chunks=vectorstoree.similarity_search(query,k)

    return retrieved_chunks

 