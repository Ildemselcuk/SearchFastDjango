from datetime import datetime

from pydantic import BaseModel


# from src.app.user.utils import UserUUID


class DriverBase(BaseModel):
    country_code: str
    country_name: str
    country_params: dict | None = None




class DriverSchema(DriverBase):
    country_uuid: str
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str | None = None

    class Config:
        from_attributes = True
