from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_critical_log():
    response = client.post(
        "/analyze",
        json={
            "service": "payment-service",
            "message": "Database connection refused"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["analysis"]["level"] == "critical"

def test_info_log():
    response = client.post(
        "/analyze",
        json={
            "service": "frontend",
            "message": "Application started successfully"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["analysis"]["level"] == "info"