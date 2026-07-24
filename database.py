from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
#ENV_FILE = os.getenv("ENV_FILE", ".env")
#load_dotenv(ENV_FILE, override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("ERROR:Environment variable DATABASE_URL not found")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
)

Base = declarative_base()
