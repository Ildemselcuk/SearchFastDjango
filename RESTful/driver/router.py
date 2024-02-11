from fastapi import Depends, APIRouter
from fastapi_versioning import version

from RESTful.common.dependencies import get_db
from RESTful.driver import service
from RESTful.driver.dependencies import get_country_uuid
from RESTful.driver.schemas import CountrySchema
from RESTful.uuids.country import CountryUUID

router = APIRouter(
    prefix="/driver",
    tags=["driver"],
    responses={
        403: {
            "description": "Forbidden (Don't have enough permission or "
                           "<code>x-user-uuid</code> or <code>x-user-identity_uuid</code> keys in header "
                           "are missing or invalid!)"},
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"}}
)

class FilterParams(BaseModel):
    startDate: str
    endDate: str
    minScore: float
    maxScore: float
    limit: int
    offset: int

@router.get("/drivers", response_model=list[CountrySchema])
@version(1)
def get_drivers(filter_params: FilterParams):
    start_date = filter_params.startDate
    end_date = filter_params.endDate
    min_score = filter_params.minScore
    max_score = filter_params.maxScore
    limit = filter_params.limit
    offset = filter_params.offset

   
    
    # Sorgu yap
    records = db.query(DriverTable).filter(
        Driver.updated_at.between(start_date, end_date),
        Driver.driving_score.between(min_score, max_score)
    ).offset(offset).limit(limit).all()
    

    
    return {
        "startDate": start_date,
        "endDate": end_date,
        "minScore": min_score,
        "maxScore": max_score,
        "limit": limit,
        "offset": offset,
        "records": records
    }
    return service.get_countries(db, skip=skip, limit=limit)






