from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
import json
from helpers.response_helpers import (
    ResponseModel, ErrorResponseModel
)
from middleware.token_validation import create_access_token
from helpers.user_helpers import verify_password
from fastapi import HTTPException
from lib.user import get_user_by_email

from models.auth import (
    LoginModel,
)

auth_router = APIRouter()


@auth_router.post("/login", response_description="User logged in")
async def userLogin(request: Request, loginData: LoginModel = Body(...)):
    request_payload = await get_body(request)
    request_payload = json.loads(request_payload)
    user_password = request_payload["password"]
    user_data = await get_user_by_email(request_payload['email'], True)
    check_password = verify_password(user_password, user_data["password"])
    if check_password is True:
        token = create_access_token(request_payload)
        token_data = {
            "access_token": token,
            "type": "Bearer"
        }
        user_data['user_auth'] = token_data
        del user_data['password']
        return ResponseModel(user_data, "User logged in successfully.")
    else:
        return ErrorResponseModel("Forbidden", 403, "The password you have entered is not matching")


async def get_body(request):
    return jsonable_encoder(await request.body())
