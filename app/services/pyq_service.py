from app.db.repositories.pyq_repo import (
    get_pyqs_by_exam,
    get_pyqs_by_topic
)

def list_pyqs_by_exam(db, exam_id: str):
    return get_pyqs_by_exam(db, exam_id)

def list_pyqs_by_topic(db, topic_id: str):
    return get_pyqs_by_topic(db, topic_id)