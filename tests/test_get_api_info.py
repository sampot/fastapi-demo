from fastapi.testclient import TestClient

from openapi.app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
