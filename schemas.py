from pydantic import BaseModel
from datetime import date

class CropCreate(BaseModel):
    farmer_id: int
    crop_name: str
    quantity: int
    harvest_date: date
    shelf_life_days: int
    location: str
