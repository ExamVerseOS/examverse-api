from sqlalchemy import Column, String, ForeignKey, Integer
from app.db.base import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(String, primary_key=True, index=True)
    exam_id = Column(String, ForeignKey("exams.id"), nullable=False)

    name = Column(String, nullable=False)
    sequence = Column(Integer, default=0)