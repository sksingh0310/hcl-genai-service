from fastapi.testclient import TestClient
from app import app

# Create a TestClient using the FastAPI app
client = TestClient(app)



def test_root():
    # Test the root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Langchain Microservice"}

def test_generate_text():
    # Test the text generation endpoint
    prompt = "What is openAI?"
    response = client.post("/generate-text/", json={"prompt": prompt})
    assert response.status_code == 200
    assert "generated_text" in response.json()
    assert isinstance(response.json()["generated_text"], str)

  


