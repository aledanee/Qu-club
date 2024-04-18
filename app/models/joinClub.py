from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db import Base

class ClubMembership(Base):
    __tablename__ = "club_memberships"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    club_id = Column(Integer, ForeignKey('clubs.id'))
    is_active = Column(Boolean, default=True)  # You can add more fields as needed

    user = relationship("User", back_populates="memberships")
    club = relationship("Club", back_populates="members")
