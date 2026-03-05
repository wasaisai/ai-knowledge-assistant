from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

# FastAPI是web框架
app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Question(BaseModel):
    question: str
    
@app.get("/")
async def root():
    return {"message": "AI Knowledge Assistant is running 🚀"}
    
@app.post("/ask")
async def ask_ai(data: Question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个专业的知识助手"},
            {"role": "user", "content": data.question}
        ]
    )
    
    return {"answer": response.choices[0].message.content}