import fastapi
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text
from app.db.session import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

from app.api import activity, auth, club, notification, userG, userR
# from app.api.V1.userR import router as userR_router
# from app.api.V1.auth import router as auth_router
# from app.api.V1.notification import router as notification_router
# from app.api.V1.userG import router as user_router
# from app.api.V1.club import router as club_router
# from app.api.V1.activity import router as activity_router
# from app.api.V1.joinClub import router as club_router  # Assuming this is your import path
# from app.api.V1 import joinClub as club_router
# from app.api.joinClub import router as join_club_router  # Ensure this is the router instance

app = fastapi.FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
async def read_root():
    return {"message": "Hello"}


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session




app.include_router(userG.router, tags=["v1-user"])
app.include_router(auth.router, tags=["v1-user"])
app.include_router(notification.router, tags=["v1-user"])
app.include_router(userR.router, tags=["v1-user"])
app.include_router(club.router, tags=["v1-club"])
app.include_router(activity.router, tags=["v1-user"])
# app.include_router(club_router, prefix="/api/v1/club", tags=["v1-club"])
# app.include_router(club_router, prefix="/api/v1/joinClub", tags=["v1-club"])

@app.get("/test_db")
async def test_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT CURRENT_TIMESTAMP"))
        current_time = result.fetchone()
        return {"status": "success", "current_time": current_time[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)


    
