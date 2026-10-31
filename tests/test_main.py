
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "AWS Cloud Task API is running!"
    }


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["database"] == "connected"


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Testing API",
            "completed": False
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_task():
    response = client.get("/tasks/999999")

    assert response.status_code == 404
