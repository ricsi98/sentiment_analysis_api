from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "up"


def test_metadata():
    response = client.get("/metadata")
    assert response.status_code == 200
    json = response.json()
    for key in ["model_version", "model_type", "model_training_date"]:
        assert key in json

    
def test_sentiment():
    response = client.post("/predict", content='{"text": "I am very happy!"}', headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"