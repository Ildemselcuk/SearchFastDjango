from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Defines the parameters for filtering drivers


class FilterParams(BaseModel):
    startDate: str  # Start date for filtering
    endDate: str    # End date for filtering
    minScore: float  # Minimum driving score for filtering
    maxScore: float  # Maximum driving score for filtering
    limit: int       # Limit parameter for pagination
    offset: int      # Offset parameter for pagination

# Defines the request parameters including skip, limit, and filter parameters


class RequestParams(BaseModel):
    skip: int = 0             # Number of records to skip
    limit: int = 100          # Maximum number of records to fetch
    filter_params: FilterParams  # Filter parameters for the request

# Defines the base structure for a driver


class DriverBase(BaseModel):
    id: int                 # Driver ID
    email: str              # Email of the driver
    first_name: str         # First name of the driver
    last_name: str          # Last name of the driver
    driving_score: float    # Driving score of the driver
    age: Optional[int] = None  # Age of the driver (optional)
    # Creation date of the driver (optional)
    created_at: Optional[datetime] = None
    # Last update date of the driver (optional)
    updated_at: Optional[datetime] = None

# Defines the schema for the response payload


class DriverSchema(BaseModel):
    # Status code of the response
    code: int = Field(0, description="The status code of the response")
    # Description of the code
    msg: str = Field("Success", description="Description of the code")
    limit: int
