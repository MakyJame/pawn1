from fastapi import FastAPI
from models.user import User
from models.customer import Customer
from models.pawn import PawnItem

from database import engine, Base


Base.metadata.drop_all(bind=engine)

print("Remove all table")

