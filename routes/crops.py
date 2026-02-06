from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Crop
from schemas import CropCreate

router = APIRouter(prefix="/crops", tags=["Crops"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_crop(crop: CropCreate, db: Session = Depends(get_db)):
    new_crop = Crop(**crop.dict())
    db.add(new_crop)
    db.commit()
    db.refresh(new_crop)
    return new_crop
