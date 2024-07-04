from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserModel(BaseModel):
    name: str = Field(...)
    last_name:  str = Field(...)
    email: EmailStr = Field(...)
    phone_number: str = Field(...)

class UpdateUserModel(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
