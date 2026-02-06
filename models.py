from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, DECIMAL
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)  # farmer / buyer
    location = Column(String(100), nullable=False)

class Crop(Base):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True)
    farmer_id = Column(Integer, ForeignKey("users.id"))
    crop_name = Column(String(50))
    quantity = Column(Integer)
    harvest_date = Column(Date)
    shelf_life_days = Column(Integer)
    location = Column(String(100))
    best_week = Column(String(50))
    expected_price = Column(DECIMAL(6,2))

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    crop_id = Column(Integer, ForeignKey("crops.id"))
    buyer_id = Column(Integer, ForeignKey("users.id"))
    quantity = Column(Integer)
    pickup_date = Column(Date)
    status = Column(Enum("pending", "accepted", "completed"))
