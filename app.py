from fastapi import FastAPI
import uvicorn
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
  prompt: str
# Initialize OpenAI with your API key
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = api_key

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Langchain Microservice"}

@app.post("/generate-text/")
async def generate_text(request: PromptRequest):
    """
    Endpoint to generate text based on a given prompt using OpenAI's language model.

    Args:
        prompt (str): The input prompt for text generation.

    Returns:
        str: The generated text from the language model.
    """
    chat = ChatOpenAI(model="gpt-4o-mini", max_tokens = 150)
    msg = chat.invoke(request.prompt)
    return f"generated_text: {msg.content}"
   
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)