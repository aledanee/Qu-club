from pydantic import BaseModel
from typing import Optional
# from datetime import datetime

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str
    role: Optional[str] = None

    class Config:
        from_attributes = True