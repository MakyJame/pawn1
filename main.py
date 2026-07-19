from fastapi import FastAPI

from database import engine,Base

from models.user import User
from models.customer import Customer
from models.pawn import PawnItem


from routers.user_router import router as user_router

app = FastAPI()

# Base.metadata.create_all(bind=engine)

app.include_router(user_router)

@app.get("/")
def home():
    return {"msg":"test docker pull image:v2"}

@app.get("/login")
def login():
    return {
        "access_token":"abc123",
        "token_type":"bearer"
    }

@app.get("/profile")
def profile():
    return {
        "username": "Mr.Minh test CI/CD"
    }
