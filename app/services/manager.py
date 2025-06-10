from app.models.car import Car
import app.utilities.helper as helper
from app.repositories.repository import CarRepository

class CarManager:
    def __init__(self):         
        self.repo = CarRepository()

    def add_car(self, car: Car): 
        self.repo.insert(car)

    def list_cars(self):
        return self.repo.get_all()
                                        
    def find_car_by_slug(self, slug: str):
        return self.repo.get_by_id(slug)

    def delete_car_by_slug(self, slug: int):
        car = self.find_car_by_slug(slug)
        if not car:
           return print(f"No car found with slug {slug}\n")            
        self.repo.delete_by_id(slug)    
    
    def generate_unique_slug(self, car_name, car_model, car_color, max_attempts=10):
        for _ in range(max_attempts):
            slug = helper.simple_slugify(
                f"{car_name} {car_model} {car_color} {helper.random_lower_alphanumeric()}"
            )
            if not self.find_car_by_slug(slug):
                return slug
        raise Exception("Failed to generate unique slug after multiple attempts.")
