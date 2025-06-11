from fastapi.testclient import TestClient
from app.main import app  
import uuid
from app.car.domain.exceptions.exception import ErrorMessages

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
    non_exit_slug = 'non-existent-slug-123'
    response = client.get(f"/cars/{non_exit_slug}")
    assert response.status_code == 404
    expected_detail = ErrorMessages.CAR_NOT_FOUND.format(slug=non_exit_slug)
    assert response.json()["detail"] == expected_detail

    
def test_delete_car_not_found():
    fake_slug_to_delete = 'fake-slug-to-delete'
    response = client.delete(f"/cars/{fake_slug_to_delete}")
    assert response.status_code == 404
    expected_detail = ErrorMessages.CAR_NOT_FOUND.format(slug=fake_slug_to_delete)
    assert response.json()["detail"] == expected_detail
