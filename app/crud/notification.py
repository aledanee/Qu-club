from app.models.Notification import Notification
from sqlalchemy.ext.asyncio import AsyncSession

async def create_notification(db: AsyncSession, user_id: int, message: str):
    notification = Notification(user_id=user_id, message=message, read_status=False)
    db.add(notification)
    await db.commit()
    await db.refresh(notification)
    return notification
