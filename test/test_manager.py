import pytest
from unittest.mock import MagicMock
from app.services.manager import CarManager
from app.models.car import Car
from unittest.mock import MagicMock
from app.exceptions.car_exceptions import CarNotFoundError
@pytest.fixture
def mock_manager():
    mock_repo = MagicMock()
    manager = CarManager(repository=mock_repo)
    return manager


def test_generate_unique_slug_returns_unique_slug(mock_manager):
    mock_manager.find_car_by_slug = MagicMock(return_value=None)  # هیچ ماشینی با این slug پیدا نشه

    slug = mock_manager.generate_unique_slug("Toyota", 2022, "Red")

    assert isinstance(slug, str)
    assert "toyota" in slug
    assert "red" in slug
    assert len(slug) > 0
    
    
    
    
def test_add_car_calls_repository_insert(mock_manager):
    mock_car = Car("slug123", "Toyota", 2022, "Red", "2024-01-01", "2025-01-01", "admin")
    
    mock_manager.add_car(mock_car)

    mock_manager.repo.insert.assert_called_once_with(mock_car)
    
def test_delete_car_raises_error_when_car_not_found(mock_manager):
    mock_manager.find_car_by_slug = MagicMock(side_effect=CarNotFoundError("slug123"))

    with pytest.raises(CarNotFoundError):
        mock_manager.delete_car_by_slug("slug123")