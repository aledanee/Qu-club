from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.session import get_db
from app.models.activity import Activity
from app.schemas.activity import ActivityCreate, ActivityOut
from sqlalchemy.future import select
from app.models import Notification, user

router = APIRouter()

@router.post("/activities/", response_model=ActivityOut)
async def create_activity(activity: ActivityCreate, db: AsyncSession = Depends(get_db)):
    async with db as session:
        db_activity = Activity(**activity.dict())
        session.add(db_activity)
        await session.commit()
        await session.refresh(db_activity)
        return db_activity
    
    

@router.get("/activities/", response_model=List[ActivityOut])
async def read_activities(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Activity))
        activities = result.scalars().all()
        return activities

@router.post("/activitiesN/", response_model=ActivityOut)
async def create_activity_for_club(activity: ActivityCreate, db: AsyncSession = Depends(get_db)):
      async with db as session:
        db_activity = Activity(**activity.dict())
        session.add(db_activity)
        await session.commit()
        await session.refresh(db_activity)
        
        # Assuming you have a way to get club members, fetch them
        # This is a placeholder for your logic to get users associated with `activity.club_id`
        club_members_query = await session.execute(select(user).filter(user.clubs.any(club_id=Activity.club_id)))
        club_members = club_members_query.scalars().all()

        # Notify each club member about the new activity
        notifications = [
            Notification(
                user_id=member.user_id,
                message=f"New activity '{activity.title}' available in your club.",
                read_status=False,
            ) for member in club_members
        ]
        session.add_all(notifications)
        await session.commit()

        return db_activity
