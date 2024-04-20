from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.session import get_db
from app.models.Notification import Notification  # Adjust import based on your model location
from app.schemas.notification import NotificationCreate, NotificationOut
from sqlalchemy.future import select

router = APIRouter()

@router.get("/notifications/", response_model=List[NotificationOut])
async def read_notifications(user_id: int, db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Notification).filter(Notification.user_id == user_id))
        notifications = result.scalars().all()
        return notifications

@router.post("/notifications/", response_model=NotificationOut)
async def create_notification(notification: NotificationCreate, user_id: int, db: AsyncSession = Depends(get_db)):
    async with db as session:
        # Here you might want to check if the user exists
        db_notification = Notification(user_id=user_id, **notification.dict())
        session.add(db_notification)
        await session.commit()
        await session.refresh(db_notification)
        return db_notification
