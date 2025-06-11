# app/api/routes.py
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.presentation.schemas.schema import carIn, carOut
from app.services.manager import CarManager
from app.models.car import Car
from app.repositories.db_connection import get_db_connection
from app.repositories.repository import CarRepository

router = APIRouter()
repo = CarRepository(get_db_connection())
manager = CarManager(repo)

@router.get("/")
async def read_index():
    return FileResponse("app/static/index.html")

@router.get("/register")
async def read_register():
    return FileResponse("app/static/register.html")

@router.post("/cars", response_model=carOut)
def create_car(car: carIn):
    slug = manager.generate_unique_slug(car.car_name, car.car_model, car.car_color)
    car.slug = slug
    new_car = Car(**car.dict())
    manager.add_car(new_car)
    return car

@router.get("/cars", response_model=list[carOut])
def list_cars():
    return [carOut.model_validate(c) for c in manager.list_cars()]

@router.get("/cars/{slug}", response_model=carOut)
def get_car(slug: str):
    car = manager.find_car_by_slug(slug)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found.")
    return carOut.model_validate(car)

@router.delete("/cars/{slug}")
def delete_car(slug: str):
    car = manager.find_car_by_slug(slug)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found.")
    manager.delete_car_by_slug(slug)
    return {"detail": "Car deleted successfully."}
