from langchain_google_genai import ChatGoogleGenerativeAI
from retrieval import retrieve_chunks
from dotenv import load_dotenv
load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-flash-lite-latest",temperature=0.2)


def answer_question(user_question:str):
    context=retrieve_chunks(user_question)
    prompt=f"""
    you are an experienced AI assistant
    Use context for an answer 
    Do not create context on your own 
    and if context is not available or not related to query then say that available context is not useful for the query
    and do not use asterisk marks

    Context:
    {context}

    User question:
    {user_question}

    Answer:
    """

    response=llm.invoke(prompt)
     
    return response.content[0]["text"]

 
