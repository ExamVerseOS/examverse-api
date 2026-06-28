from sqlalchemy import Column, String, Text, Integer, ForeignKey, DateTime
from datetime import datetime
from app.db.base import Base

class PYQ(Base):
    __tablename__ = "pyqs"

    id = Column(String, primary_key=True, index=True)

    exam_id = Column(String, ForeignKey("exams.id"), nullable=False)
    subject_id = Column(String, ForeignKey("subjects.id"), nullable=True)
    topic_id = Column(String, ForeignKey("topics.id"), nullable=True)

    year = Column(Integer, nullable=False)
    paper = Column(String, nullable=True)

    question_text = Column(Text, nullable=False)
    answer_key = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)

    marks = Column(Integer, default=0)
    difficulty = Column(String, default="medium")

    created_at = Column(DateTime, default=datetime.utcnow)