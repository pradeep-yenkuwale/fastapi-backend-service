from fastapi import FastAPI
from fastapi import FastAPI
from routes.user import router as UserRouter
from routes.auth import auth_router as AuthRouter
from middleware.middleware import Middleware

app = FastAPI()
app.include_router(UserRouter, tags=["User"], prefix="/api/v1")
app.include_router(AuthRouter, tags=["User", "Auth"], prefix="/api/v1/user/auth")
# app.add_middleware(Middleware)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this FastAPI Backend app!"}