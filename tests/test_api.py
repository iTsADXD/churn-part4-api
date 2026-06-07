from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict():
    payload = {
        "recencydays": 10,
        "frequency180d": 5,
        "monetary180d": 200.0,
        "sessions30d": 3,
        "lastvisitdaysago": 2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200

def test_batch_predict():
    payload = [
        {
            "recencydays": 10,
            "frequency180d": 5,
            "monetary180d": 200.0,
            "sessions30d": 3,
            "lastvisitdaysago": 2
        }
    ]
    response = client.post("/batch_predict", json=payload)
    assert response.status_code == 200