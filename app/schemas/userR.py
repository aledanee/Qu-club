from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = "REGISTERED_USER"

class UserOut(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    role: str

    class Config:
       from_attributes = True
