from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.manager import CarManager
from app.models.car import Car
from typing import Optional

router = APIRouter()
manager = CarManager()

class carIn(BaseModel):
    slug: Optional[str] = None
    car_name: str
    car_model: int
    car_color: str
    from_date: Optional[str] = None
    to_date: Optional[str] = None
    creator_code: str

class carOut(carIn):
    pass

@router.post("/cars", response_model=carOut)
def create_car(car: carIn):
    car.slug = manager.generate_unique_slug(car.car_name, car.car_model, car.car_color)
    manager.add_car(car)
    return car

@router.get("/cars", response_model=list[carOut])
def list_cars():
    cars = manager.list_cars()    
    return [] if not cars else [vars(s) for s in cars]

@router.get("/cars/{slug}", response_model=carOut)
def get_car(slug: str):
    car = manager.find_car_by_slug(slug)
    if not car:
        raise HTTPException(status_code=404, detail="car not found.")
    return vars(car)

@router.delete("/cars/{slug}")
def delete_car(slug: str):
    car = manager.find_car_by_slug(slug)
    if not car:
        raise HTTPException(status_code=404, detail="car not found.")
    manager.delete_car_by_slug(slug)
    return {"detail": "car deleted successfully."}
