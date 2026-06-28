from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from app.db.base import Base

class Exam(Base):
    __tablename__ = "exams"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    organization = Column(String, nullable=True)
    country = Column(String, nullable=True)
    category = Column(String, nullable=True)

    description = Column(Text, nullable=True)

    status = Column(String, default="active")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)