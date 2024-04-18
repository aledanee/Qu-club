from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base





class Club(Base):
    __tablename__ = 'clubs'

    club_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    manager_id = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    
    manager = relationship("User", back_populates="managed_clubs")
    activities = relationship("Activity", back_populates="club")