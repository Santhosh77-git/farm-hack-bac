from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Order
from pydantic import BaseModel
from datetime import date

router = APIRouter(prefix="/orders", tags=["Orders"])

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request schema
class OrderCreate(BaseModel):
    crop_id: int
    buyer_id: int
    quantity: int
    pickup_date: date

# Create order
@router.post("/")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(
        crop_id=order.crop_id,
        buyer_id=order.buyer_id,
        quantity=order.quantity,
        pickup_date=order.pickup_date,
        status="pending"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

# Get all orders
@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()
