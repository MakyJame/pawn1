from fastapi import APIRouter

from database import SessionLocal
from pydantic import BaseModel
from models.user import User
from models.pawn import PawnItem
from models.customer import Customer

from datetime import date
from repositories.user_repository import (
    get_all_user,
    create_user,
    delete_user,
    get_all_pawn,
    create_pawn,
    get_all_customer,
    create_customer
)
from services.user_service import (
    create_user_service
)
router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    age: int
class PawnItemCreate(BaseModel):
    date: date
    vehicle_num: str
    pawn_price: int
    storage: str
    brand: str
    customer_id: int

class CustomerCreate(BaseModel):
    name: str
    phone: str

#@router.get("/")
#def home():
#    return {"msg":"hello from home"}

@router.get("/users")
def get_all_the_user():
    db = SessionLocal()
    return get_all_user(db)

@router.post("/user")
def create(user: UserCreate):
    db = SessionLocal()
    return create_user_service(db,user.username,user.email)

@router.delete("/users/{user_id}")
def delete(user_id: int):
    db = SessionLocal()
    user = delete_user(db,user_id)
    if not user:
        return {"error":"user not found"}
    return {"msg":"deleted user"}

@router.get("/pawn")
def get_all_the_pawn():
    db = SessionLocal()
    return get_all_pawn(db)

@router.post("/pawn")
def create_new_pawn(item: PawnItemCreate):
    db = SessionLocal()
    return create_pawn(db,item.date,item.vehicle_num,item.pawn_price,item.storage,item.brand,item.customer_id)

@router.get("/customer")
def get_all_the_customer():
    db = SessionLocal()
    return get_all_customer(db)

@router.post("/customer")
def create_new_customer(customer: CustomerCreate):
    db = SessionLocal()
    return create_customer(db,customer.name,customer.phone)

