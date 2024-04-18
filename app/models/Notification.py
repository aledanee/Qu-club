from sqlalchemy import Column, Integer, Boolean, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Notification(Base):
    __tablename__ = 'notifications'

    notification_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    message = Column(Text, nullable=False)
    read_status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    
    user = relationship("User", back_populates="notifications")
