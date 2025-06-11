from app.car.domain.car import Car
from app.car.infrastructure.repository import CarRepository
from typing import Callable
import app.utilities.helper as helper
from app.car.domain.exceptions.exception import CarNotFoundError

class CarManager:
    def __init__(self, repository: CarRepository, slug_generator: Callable = None):         
        self.repo = repository
        self.slug_generator = slug_generator or self.default_slug_generator

    def add_car(self, car: Car): 
        self.repo.insert(car)

    def list_cars(self):
        return self.repo.get_all()
                                        
    def find_car_by_slug(self, slug: str):
        return self.repo.get_by_slug(slug)

    def delete_car_by_slug(self, slug: str):
        car = self.find_car_by_slug(slug)
        if not car:
            raise CarNotFoundError(slug)
        self.repo.delete_by_slug(slug)    
    
    def generate_unique_slug(self, car_name, car_model, car_color, max_attempts=10):
        for _ in range(max_attempts):
            slug = self.slug_generator(car_name, car_model, car_color)
            if not self.find_car_by_slug(slug):
                return slug
        raise Exception("Failed to generate unique slug after multiple attempts.")

    @staticmethod
    def default_slug_generator(car_name, car_model, car_color):
        return helper.simple_slugify(
            f"{car_name} {car_model} {car_color} {helper.random_lower_alphanumeric()}"
        )
