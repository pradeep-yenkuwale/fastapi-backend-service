from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
import json
from helpers.response_helpers import (
    ResponseModel
)
from middleware.token_validation import create_access_token

from lib.user import get_user_by_email


from models.auth import (
    LoginModel,
)

auth_router = APIRouter()

@auth_router.post("/login", response_description="User logged in")
async def userLogin(request: Request ,loginData: LoginModel = Body(...)):
    request_payload = await get_body(request)
    request_payload = json.loads(request_payload)
    user_data = await get_user_by_email(request_payload['email'])
    token = create_access_token(request_payload)
    token_data = {
        "access_token": token,
        "type": "Bearer"
    }
    user_data['user_auth'] = token_data
    return ResponseModel(user_data, "User logged in successfully.")

async def get_body(request):
    return jsonable_encoder(await   request.body())