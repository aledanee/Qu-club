from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.session import get_db
from app.models.club import Club
from app.schemas.club import ClubCreate, ClubOut
from sqlalchemy.future import select

router = APIRouter()

@router.get("/clubs/", response_model=List[ClubOut])
async def read_clubs(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Club))
        clubs = result.scalars().all()
        return clubs

@router.post("/clubs/", response_model=ClubOut)
async def create_club(club: ClubCreate, db: AsyncSession = Depends(get_db)):
    async with db as session:
        db_club = Club(**club.dict())
        session.add(db_club)
        await session.commit()
        await session.refresh(db_club)
        return db_club

@router.get("/clubs/{club_id}", response_model=ClubOut)
async def read_club_by_id(club_id: int, db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Club).filter(Club.id == club_id))
        club = result.scalars().first()
        if club:
            return club
        else:
            raise HTTPException(status_code=404, detail="Club not found")
