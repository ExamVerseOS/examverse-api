from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    role = Column(String, default="student")

    created_at = Column(DateTime, default=datetime.utcnow)