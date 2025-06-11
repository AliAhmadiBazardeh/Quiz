from fastapi.testclient import TestClient
from app.main import app  
import uuid

client = TestClient(app)

def test_create_car():
    slug = str(uuid.uuid4())[:8]  # Unique
    payload = {
        "slug": slug,
        "car_name": "BMW",
        "car_model": 2022,
        "car_color": "Black",
        "from_date": "2023-01-01",
        "to_date": "2024-01-01",
        "creator_code": "admin123"
    }

    response = client.post("/cars", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["car_name"] == "BMW"
    assert "slug" in data


def test_get_all_cars():
    response = client.get("/cars")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_car_by_slug_not_found():
    response = client.get("/cars/non-existent-slug-123")
    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found."


def test_delete_car_not_found():
    response = client.delete("/cars/fake-slug-to-delete")
    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found."
