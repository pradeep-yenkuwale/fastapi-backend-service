import os
import jwt
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta, timezone
from lib.user import get_user_by_email
import json

# Retrieve the secret key and algorithm from environment variables
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Function to verify the access token extracted from the request
async def verify_access_token(request):
    # Extract the token from the request
    try:
        # Decode and verify the token using the secret key and algorithm
        url = get_route(request)
        if "auth/login" in str(url):
            return request
        else:
            user_token = get_token_from_request(request)
            payload = decode_access_token(user_token)
            return payload
    except jwt.ExpiredSignatureError:
        # Raise an HTTPException with status code 401 if the token has expired
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        # Raise an HTTPException with status code 401 if the token is invalid
        raise HTTPException(status_code=401, detail="Invalid token",)


def get_token_from_request(request):
    try:
        return request.headers["authorization"]
    except:
        raise jwt.InvalidTokenError


def get_route(request):
    return request.url


async def get_body(request):
    return jsonable_encoder(await request.body())
    # return await request.body()


def create_access_token(data: dict):
    to_encode = data.copy()
    print("to_encode", to_encode)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expires_delta = access_token_expires
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        split_token = token.split(" ")
        if (len(split_token) < 2):
            raise jwt.InvalidTokenError
        else:
            token_type = split_token[0]
            token = split_token[1]

        if token_type.lower() == "bearer":
            return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        else:
            raise jwt.InvalidTokenError
    except:
        raise jwt.InvalidTokenError
