from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_say_hello():
    response = client.get("/hello/Name")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello Name from flux-gha-app demo project"}
