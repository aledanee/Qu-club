import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app.core.config import settings
from app.models.user import User  # Importing user model for testing
import sys
sys.path.append('/Users/ibrahimihsan/Documents/N-QuClub')

async def test_db_connection():
    # Construct the SQLALchemy engine/connection string
    SQLALCHEMY_DATABASE_URL = f"mysql+aiomysql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}"
    engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

    # Creating a session
    async with sessionmaker(engine, class_=AsyncSession)() as session:
        # Simple SELECT query to test the connection
        result = await session.execute(select(User))
        users = result.scalars().all()
        print(f"Users: {users}")

if __name__ == "__main__":
    asyncio.run(test_db_connection())
