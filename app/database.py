from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST=os.getenv("POSTGRES_HOST")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")
SQLALCHEMY_DATABASE_URL=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/todolist"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
except Exception as e:
    print(f"Error while connecting to the database: {e}")
    raise

SessionLocal= sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base= declarative_base()