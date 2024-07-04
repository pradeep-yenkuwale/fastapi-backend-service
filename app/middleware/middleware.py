from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from middleware.token_validation import verify_access_token
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Middleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            # Call the verify_access_token function to validate the token
            user_data = await verify_access_token(request)
            print("user_data ce", user_data)
            # If token validation succeeds, continue to the next middleware or route handler
            response = await call_next(request)
            return response
        except HTTPException as exc:
            # If token validation fails due to HTTPException, return the error response
            return JSONResponse(content={"detail": exc.detail}, status_code=exc.status_code)
        except Exception as exc:
            # If token validation fails due to other exceptions, return a generic error response
            return JSONResponse(content={"detail": f"Error: {str(exc)}"}, status_code=500)
