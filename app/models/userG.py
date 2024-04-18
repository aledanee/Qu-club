from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.db.session import get_db
from app.models.user import User
from app.schemas.userG import UserOut

router = APIRouter()

@router.get("/users/", response_model=List[UserOut])
async def read_users(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users
