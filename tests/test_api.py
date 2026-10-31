from fastapi.testclient import TestClient
from src.api import app


client=TestClient(app)

def test_health():
    response =client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"]== "healthy"

def test_database():
    response = client.get("/runbooks/search", params={"keyword":"database"})
    assert response.status_code == 200
    data = response.json()

    assert data["count"] == 1
    assert data["results"][0]["title"] == "Database Connection Error"


def test_rank_database():
    response = client.get("/runbooks/rank", params={"keyword":"database"})
    assert response.status_code == 200
    data = response.json()

    assert data["count"] ==1
    assert data["results"][0]["score"] == 15