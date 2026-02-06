from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from pydantic import BaseModel, Field
from security import hash_password   # 🔐 password hashing
from typing_extensions import Annotated
router = APIRouter(prefix="/users", tags=["Users"])

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request schema
class UserCreate(BaseModel):
    name: str
    phone_number: Annotated[str, Field(min_length=10, max_length=15)]
    password: str
    role: str
    location: str

# Create user
@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name=user.name,
        phone_number=user.phone_number,
        password=hash_password(user.password),  # 🔐 hashed
        role=user.role,
        location=user.location
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # ❌ never return password
    return {
        "id": new_user.id,
        "name": new_user.name,
        "phone_number": new_user.phone_number,
        "role": new_user.role,
        "location": new_user.location
    }

# Get all users
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [
        {
            "id": u.id,
            "name": u.name,
            "phone_number": u.phone_number,
            "role": u.role,
            "location": u.location
        }
        for u in users
    ]
