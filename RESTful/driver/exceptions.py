from fastapi import HTTPException


class DriverNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Country not found")


class DriverNotFoundWithUUIDException(HTTPException):
    def __init__(self, country_uuid):
        super().__init__(status_code=404, detail=f"No country found with UUID {country_uuid}")




class InvalidDriverUUIDException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Invalid CountryUUID format.")
