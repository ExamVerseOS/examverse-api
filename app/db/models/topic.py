from sqlalchemy import Column, String, ForeignKey, Text, Integer
from app.db.base import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(String, primary_key=True, index=True)
    subject_id = Column(String, ForeignKey("subjects.id"), nullable=False)

    parent_topic_id = Column(String, nullable=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    difficulty = Column(String, default="medium")
    sequence = Column(Integer, default=0)