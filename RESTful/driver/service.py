from fastapi import HTTPException
from sqlalchemy.orm import Session

from RESTful.driver.exceptions import RecordNotFoundException
from RESTful.driver.models import Driver
from RESTful.driver.schemas import DriverSchema


def get_drivers(db: Session, offset: int = 0, limit: int = 100, start_date: str = "1970-01-01", end_date: str = "2024-01-01", min_score: float = 0.0, max_score: float = 0.0):
    db_drivers = (db.query(Driver)
                  .filter(
        Driver.updated_at.between(start_date, end_date),
        Driver.driving_score.between(min_score, max_score))
        .offset(offset)
        .limit(limit)
        .all())
    if db_drivers is None:
        raise RecordNotFoundException()
    return db_drivers
