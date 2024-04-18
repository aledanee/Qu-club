from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.db.base_class import Base
from sqlalchemy.orm import relationship





class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # Ensure this matches the column name
    role = Column(Enum('SKS_ADMIN', 'CLUB_MANAGER', 'REGISTERED_USER'), nullable=False)
    created_at = Column(TIMESTAMP)
    notifications = relationship("Notification", back_populates="user")
    managed_clubs = relationship("Club", back_populates="manager")
