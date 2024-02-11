import uuid as uuid_pkg
from datetime import datetime

from sqlalchemy import JSON, DateTime, Column, String, Index

from RESTful.db_constants import PREFIX_COUNTRY_UUID, PREFIX_COUNTRY_TABLE
from RESTful.database import Base


class Driver(Base):
    __tablename__ = "driver_driver"
    id = Column(String, primary_key=True, index=True, nullable=False, unique=True)
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(JSON, nullable=True)
    last_name = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

