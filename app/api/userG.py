from venv import logger
from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.db.session import get_db
from app.models.user import User
from app.schemas.userG import UserOut

router = APIRouter()

@router.get("/get-users/", response_model=List[UserOut])
async def read_users(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users

@router.get("/get-user/{user_id}", response_model=UserOut)
async def read_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info(f"Fetching user with ID: {user_id}")
    async with db as session:
        result = await session.execute(select(User).filter(User.id == user_id))
        user = result.scalars().first()
        if user:
            return user
        else:
            logger.error("User not found")
            raise HTTPException(status_code=404, detail="User not found")
    