from fastapi import FastAPI

from database import engine, Base


Base.metadata.drop_all(bind=engine)

print("Remove all table")

