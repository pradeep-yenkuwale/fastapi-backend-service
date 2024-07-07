
from fastapi.responses import JSONResponse

def ResponseModel(data, message):
    return {
        "data": data,
        "status": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    error_dict = {
        "error": error,
        "message": message,
        "status_code": code

    }
    return JSONResponse(status_code=code, content=error_dict)
