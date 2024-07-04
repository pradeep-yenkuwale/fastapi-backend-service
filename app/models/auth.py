from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class LoginModel(BaseModel):
    email: str = Field(...)
    password:  str = Field(...)