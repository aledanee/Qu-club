# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from app.models.user import User
# from app.schemas.user import UserCreate, UserOut
# from app.core.security import get_password_hash
# from app.db.session import get_db

# router = APIRouter()

# @router.post("/users/", response_model=UserOut)
# async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
#     # Check if username or email already exists
#     existing_user = await db.execute(select(User).filter((User.username == user.username) | (User.email == user.email)))
#     if existing_user.scalars().first():
#         raise HTTPException(status_code=400, detail="Username or email already registered")

#     # Hash password
#     hashed_password = get_password_hash(user.password)

#     # Create new user instance and add to the database
#     db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
#     db.add(db_user)
#     await db.commit()
#     await db.refresh(db_user)

#     return db_user

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.user import User  # Ensure your model is correctly defined based on the schema
from app.schemas.userR import UserCreate, UserOut
from app.core.security import get_password_hash
from sqlalchemy.future import select

router = APIRouter()

@router.post("/users/rig", response_model=UserOut)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    async with db as session:
        # Check if the username or email already exists
        user_query = await session.execute(select(User).filter((User.username == user.username) | (User.email == user.email)))
        user_in_db = user_query.scalars().first()
        if user_in_db:
            raise HTTPException(status_code=400, detail="Username or email already registered")

        hashed_password = get_password_hash(user.password)
        # Assuming `hashed_password` is the result of hashing the user's password
        db_user = User(username=user.username, email=user.email, password_hash=hashed_password, role=user.role)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user
