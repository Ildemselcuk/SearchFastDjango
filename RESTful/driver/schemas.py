from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class FilterParams(BaseModel):
    startDate: str
    endDate: str
    minScore: float
    maxScore: float
    limit: int
    offset: int


class RequestParams(BaseModel):
    skip: int = 0
    limit: int = 100
    filter_params: FilterParams


class DriverBase(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    driving_score: float
    age: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DriverSchema(BaseModel):
    code: int = Field(0, description="The status code of the response")
    msg: str = Field("Success", description="Description of the code")
    limit: int = Field(50, description="Limit parameter used for pagination")
    offset: int = Field(
        200, description="Offset parameter used for pagination")
    records: List[DriverBase] = Field(None, description="List of records")
