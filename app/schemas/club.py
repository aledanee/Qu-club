from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClubBase(BaseModel):
    name: str
    description: Optional[str] = None

class ClubCreate(ClubBase):
    pass

class ClubOut(ClubBase):
    club_id: int
    # created_at: datetime
    manager_id: Optional[int] = None

    class Config:
        from_attributes = True