from pydantic import BaseModel, ConfigDict
from typing import Optional

class carIn(BaseModel):
    slug: Optional[str] = None
    car_name: str
    car_model: int
    car_color: str
    from_date: Optional[str] = None
    to_date: Optional[str] = None
    creator_code: str

class carOut(carIn):
    model_config = ConfigDict(from_attributes=True)
