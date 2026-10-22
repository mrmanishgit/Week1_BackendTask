from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Task Management System API is running"
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_tasks_requires_authentication():
    response = client.get("/tasks/")

    assert response.status_code == 401


def test_create_task_requires_authentication():
    response = client.post(
        "/tasks/",
        json={
            "title": "Test task",
            "description": "Testing task creation",
            "status": "PENDING",
            "priority": "MEDIUM",
            "due_date": None,
        },
    )

    assert response.status_code == 401


def test_get_task_by_id_requires_authentication():
    response = client.get("/tasks/1")

    assert response.status_code == 401


def test_update_task_requires_authentication():
    response = client.put(
        "/tasks/1",
        json={"title": "Updated task"},
    )

    assert response.status_code == 401


def test_delete_task_requires_authentication():
    response = client.delete("/tasks/1")

    assert response.status_code == 401