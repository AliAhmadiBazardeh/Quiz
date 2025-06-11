from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.car.schema import carIn, carOut
from app.car.application.manager import CarManager
from app.car.domain.car import Car
from app.car.infrastructure.db_connection import get_db_connection
from app.car.domain.exceptions.exception import CarNotFoundError,ErrorMessages
from app.car.infrastructure.repository import CarRepository

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
    new_car = Car(**car.model_dump())
    manager.add_car(new_car)
    return car

@router.get("/cars", response_model=list[carOut])
def list_cars():
    return [carOut.model_validate(c) for c in manager.list_cars()]

@router.get("/cars/{slug}", response_model=carOut)
def get_car(slug: str):
    try:
        car = manager.find_car_by_slug(slug)
        return carOut.model_validate(car)
    except CarNotFoundError:
        detail = ErrorMessages.CAR_NOT_FOUND.format(slug=slug)
        raise HTTPException(status_code=404, detail=detail)

@router.delete("/cars/{slug}")
def delete_car(slug: str):
    try:
        manager.delete_car_by_slug(slug)
        return {"detail": f"{slug} deleted successfully."}
    except CarNotFoundError:
        detail = ErrorMessages.CAR_NOT_FOUND.format(slug=slug)    
        raise HTTPException(status_code=404, detail=detail)