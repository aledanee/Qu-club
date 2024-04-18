from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class ActivityStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class ActivityBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[ActivityStatus] = "PENDING"

class ActivityCreate(ActivityBase):
    club_id: int

class ActivityUpdate(ActivityBase):
    pass

class ActivityOut(ActivityBase):
    activity_id: int
    club_id: int
    # reated_at: datetime

    class Config:
        from_attributes = True