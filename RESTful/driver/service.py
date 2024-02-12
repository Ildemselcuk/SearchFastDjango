from fastapi import HTTPException
from sqlalchemy.orm import Session

from RESTful.driver.exceptions import RecordNotFoundException
from RESTful.driver.models import Driver
from RESTful.driver.schemas import DriverSchema


def get_drivers(db: Session, offset: int = 0, limit: int = 100, start_date: str = "1970-01-01", end_date: str = "2024-01-01", min_score: float = 0.0, max_score: float = 0.0):
    """
    Fetches drivers from the database and filters them.

    :param db: Database session
    :param offset: Start position of the results
    :param limit: Maximum number of records to fetch
    :param start_date: Start date for filtered records
    :param end_date: End date for filtered records
    :param min_score: Minimum driving score
    :param max_score: Maximum driving score
    :return: Filtered driver records
    """
    try:
        db_drivers = db.query(Driver).filter(
            Driver.updated_at.between(start_date, end_date),
            Driver.driving_score.between(min_score, max_score)
        ).offset(offset).limit(limit).all()
        if not db_drivers:
            raise RecordNotFoundException()
        return db_drivers
    except Exception as e:
        # Here you can set the appropriate HTTP status code and error message
        raise HTTPException(status_code=500, detail="Internal Server Error")
