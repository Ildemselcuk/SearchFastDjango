from fastapi import Depends, APIRouter, HTTPException
from fastapi_versioning import version
from sqlalchemy.orm import Session
from RESTful.common.dependencies import get_db
from RESTful.driver import service
from RESTful.driver.schemas import  DriverSchema, RequestParams

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

@router.get("/drivers", response_model=DriverSchema)
@version(1)
def get_drivers(request_params: RequestParams,
                db: Session = Depends(get_db)):
    try:
        # Extract filter parameters from request_params
        start_date = request_params.filter_params.startDate
        end_date = request_params.filter_params.endDate
        min_score = request_params.filter_params.minScore
        max_score = request_params.filter_params.maxScore
        limit = request_params.filter_params.limit
        offset = request_params.filter_params.offset

        # Run the query to get drivers from the database
        records = service.get_drivers(
                        db, 
                        offset=offset, 
                        limit=limit,
                        start_date=start_date,
                        end_date=end_date,
                        min_score=min_score,
                        max_score=max_score
                        )
        
        # If records are found, return them with success message
        if records:
            return {
                "code": 0,
                "msg": "Success",
                "limit": limit,
                "offset": offset,
                "records": records
            }
        else:
            # If no records found, raise HTTPException with 404 status code
            raise HTTPException(status_code=404, detail="No records found")
    except Exception as e:
        # If any exception occurs, return error message in JSON format
        return {
            "code": 500,
            "msg": "Internal Server Error",
            "error_detail": str(e)
        }
