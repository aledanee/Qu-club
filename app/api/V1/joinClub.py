# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from app.models.user import User  # Adjust the import to the correct path
# from app import models
# from app.schemas import Msg  # This should now work if you have the above definition in placefrom app.core import security
# from app.db.session import get_db
# from app.core.security import get_current_user
# from app.models.club import Club  # Ensure this import is correct

# router = APIRouter()

# @router.post("/clubs/{club_id}/join")
# async def join_club(club_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     # Make sure to handle the case where club_id is not found
#     club = db.query(models.Club).filter(models.Club.id == club_id).first()
#     if not club:
#         raise HTTPException(status_code=404, detail="Club not found")

#     # Check if the user is already a member
#     if db.query(models.club_members).filter_by(user_id=current_user.id, club_id=club_id).first():
#         raise HTTPException(status_code=400, detail="User already a member of the club")
    
#     # Add user to the club_members association table
#     club_member = models.club_members(user_id=current_user.id, club_id=club_id)
#     db.add(club_member)
#     db.commit()
#     return {"msg": "User successfully joined the club"}




# @router.post("/clubs/{club_id}/users/{user_id}/join")
# async def join_club(club_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
#     async with db as session:
#         # Fetch the club using an asynchronous query
#         club_result = await session.execute(select(models.club).filter(models.club.id == club_id))
#         club = club_result.scalars().first()
#         if not club:
#             raise HTTPException(status_code=404, detail="Club not found")

#         # Fetch the user using an asynchronous query
#         user_result = await session.execute(select(models.user).filter(models.user.id == user_id))
#         user = user_result.scalars().first()
#         if not user:
#             raise HTTPException(status_code=404, detail="User not found")

#         # Check if the user is already a member of the club
#         member_result = await session.execute(select(models.joinClub).filter_by(user_id=user_id, club_id=club_id))
#         is_member = member_result.scalars().first() is not None
#         if is_member:
#             raise HTTPException(status_code=400, detail="User already a member of the club")
        
#         # Insert new club member
#         new_member = models.joinClub.insert().values(user_id=user_id, club_id=club_id)
#         await session.execute(new_member)
#         await session.commit()

#         return {"msg": "User successfully joined the club"}


# //////////////////////////////////////////////////////////////////////////


# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from app.models import User, Club, ClubMember
# from app.db.session import get_db
# from app.core.security import get_current_user
# from app.models import Notification


# router = APIRouter()

# @router.post("/clubs/{club_id}/join", status_code=status.HTTP_201_CREATED)
# async def join_club(club_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
#     async with db as session:
#         # Check if club exists
#         club = await session.get(Club, club_id)
#         if not club:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Club not found")

#         # Check if user is already a member
#         existing_membership = await session.execute(select(ClubMember).filter_by(user_id=current_user.id, club_id=club_id))
#         if existing_membership.scalars().first():
#             raise HTTPException(status_code=status.HTTP_400_BAD_BAD_REQUEST, detail="User already a member of this club")
        
#         # Add user to the club
#         new_member = ClubMember(user_id=current_user.id, club_id=club_id)
#         session.add(new_member)
#         await session.commit()
        
#         return {"msg": "Successfully joined the club"}




# @router.post("/clubs/{club_id}/notify", status_code=status.HTTP_201_CREATED)
# async def send_notification(club_id: int, message: str, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
#     async with db as session:
#         # Verify if current_user is the club manager here
#         # ...

#         # Fetch all club members
#         club_members = await session.execute(select(ClubMember.user_id).filter_by(club_id=club_id))
#         member_ids = [result.user_id for result in club_members.scalars().all()]

#         # Create notifications for each member
#         notifications = [Notification(user_id=user_id, message=message) for user_id in member_ids]
#         session.add_all(notifications)
#         await session.commit()

#         return {"msg": "Notifications sent to all club members"}



# //////////////////////////////////////////////////////////////////////////



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, dependencies

router = APIRouter()

@router.post("/clubs/{club_id}/join", response_model=schemas.ClubMembership)
def join_club(club_id: int, db: Session = Depends(dependencies.get_db),
              current_user: models.User = Depends(dependencies.get_current_active_user)):
    # Check if the club exists
    club = crud.get_club(db, club_id=club_id)
    if not club:
        raise HTTPException(status_code=404, detail="Club not found")
    # Check if the user is already a member
    if crud.is_member(db, club_id=club_id, user_id=current_user.id):
        raise HTTPException(status_code=400, detail="Already a member of the club")
    return crud.join_club(db=db, club_id=club_id, user_id=current_user.id)



@router.post("/clubs/{club_id}/leave", response_model=schemas.ClubMembership)
def leave_club(club_id: int, db: Session = Depends(dependencies.get_db),
               current_user: models.User = Depends(dependencies.get_current_active_user)):
    membership = crud.leave_club(db=db, club_id=club_id, user_id=current_user.id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found or already inactive")
    return membership
