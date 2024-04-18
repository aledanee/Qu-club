from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Activity(Base):
    __tablename__ = 'activities'

    activity_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    club_id = Column(Integer, ForeignKey('clubs.club_id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum('PENDING', 'APPROVED', 'REJECTED'), nullable=False, default='PENDING')
    created_at = Column(TIMESTAMP, nullable=False)
    
    club = relationship("Club", back_populates="activities")
