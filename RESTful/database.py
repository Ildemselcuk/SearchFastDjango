import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, event

from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
SQLALCHEMY_ECHO = False

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=SQLALCHEMY_ECHO
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


