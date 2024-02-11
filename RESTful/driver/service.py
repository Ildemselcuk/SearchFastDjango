from fastapi import HTTPException
from sqlalchemy.orm import Session

from RESTful.driver.exceptions import CountryNotFoundWithUUIDException, CountryAlreadyExistsException
from RESTful.driver.models import Driver
from RESTful.driver.schemas import DriverSchema


def get_drivers(db: Session, country_uuid: CountryUUID):
    db_country = db.query(Driver).filter(Driver.country_uuid == str(country_uuid)).first()
    if db_country is None:
        raise CountryNotFoundWithUUIDException(country_uuid)
    return db_country

def get_user_identities(db: Session, skip: int = 0, limit: int = 100):
    return (db.query(Driver)
            .filter(Driver.is_deleted == 0)
            .offset(skip)
            .limit(limit)
            .all())

    db.query(DriverTable).filter(
        Driver.updated_at.between(start_date, end_date),
        Driver.driving_score.between(min_score, max_score)
    ).offset(offset).limit(limit).all()