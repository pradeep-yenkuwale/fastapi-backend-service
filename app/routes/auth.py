from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder

from helpers.response_helpers import (
    ResponseModel,
)

from models.auth import (
    LoginModel,
)

auth_router = APIRouter()

@auth_router.post("/login", response_description="User logged in")
async def userLogin(loginData: LoginModel = Body(...)):
    print("loginData", loginData)
    loginData = jsonable_encoder(loginData)
    return ResponseModel(loginData, "User logged in successfully.")
