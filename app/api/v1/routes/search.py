from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import db_dep
from app.services.topic_service import list_topics, fetch_topic

router = APIRouter()

@router.get("/topics/{subject_id}")
def topics(subject_id: str, db: Session = Depends(db_dep)):
    return list_topics(db, subject_id)

@router.get("/topic/{topic_id}")
def topic(topic_id: str, db: Session = Depends(db_dep)):
    return fetch_topic(db, topic_id)