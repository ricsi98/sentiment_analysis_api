from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    """We expect the response for the GET /health endpoint to return status: up"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "up"


def test_metadata():
    """We expect the response for the GET /metadata endpoint to contain certain keys"""
    response = client.get("/metadata")
    assert response.status_code == 200
    json = response.json()
    for key in ["model_version", "model_type", "model_training_date"]:
        assert key in json

    
def test_sentiment():
    """We expect that the sentiment of a happy sentence is positive"""
    response = client.post("/predict", content='{"text": "I am very happy!"}', headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"
