from fastapi import HTTPException


class RecordNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Records not found")