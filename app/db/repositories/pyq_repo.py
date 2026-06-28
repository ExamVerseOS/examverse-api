from sqlalchemy.orm import Session
from app.db.models.pyq import PYQ

def get_pyqs_by_exam(db: Session, exam_id: str):
    return db.query(PYQ).filter(PYQ.exam_id == exam_id).all()

def get_pyqs_by_topic(db: Session, topic_id: str):
    return db.query(PYQ).filter(PYQ.topic_id == topic_id).all()