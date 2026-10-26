from fastapi import FastAPI
from pydantic import BaseModel
from rag import answer_question

app=FastAPI()

class UserQuestion(BaseModel):
    query:str

@app.get("/")
def Home():
    return {
        "message":"Hello buddy"
    }


@app.post("/chat")
def Chatt(query:UserQuestion):
    
    answer=answer_question(query.query)
    return {
        "answer":answer
    }
    