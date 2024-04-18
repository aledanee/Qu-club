from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NotificationBase(BaseModel):
    message: str
    read_status: Optional[bool] = False

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    notification_id: int
    user_id: int
    # created_at: datetime

    class Config:
        from_attributes = True