from fastapi import FastAPI
import uvicorn
from langchain_openai import ChatOpenAI
import os

app = FastAPI()

# openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_key = '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'

os.environ["OPENAI_API_KEY"] = openai_api_key

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Langchain Microservice"}

@app.post("/generate-text/")
async def generate_text(prompt: str):
    chat = ChatOpenAI(model="gpt-4o", max_tokens = 150)
    msg = chat.invoke(prompt)
    return f"generated_text: {msg.content}"
   
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)