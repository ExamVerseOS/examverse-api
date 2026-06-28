from app.db.repositories.topic_repo import get_topics_by_subject, get_topic

def list_topics(db, subject_id: str):
    return get_topics_by_subject(db, subject_id)

def fetch_topic(db, topic_id: str):
    return get_topic(db, topic_id)