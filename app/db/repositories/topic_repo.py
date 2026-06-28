from sqlalchemy.orm import Session
from app.db.models.topic import Topic

def get_topics_by_subject(db: Session, subject_id: str):
    return db.query(Topic).filter(Topic.subject_id == subject_id).all()

def get_topic(db: Session, topic_id: str):
    return db.query(Topic).filter(Topic.id == topic_id).first()