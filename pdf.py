 
from langchain_community.document_loaders import PyPDFLoader
def loader_pdf():

    loader=PyPDFLoader("jinal_resume_AIML_Engineer.pdf")
    docs=loader.load()
    return docs
