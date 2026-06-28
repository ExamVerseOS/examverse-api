from app.db.repositories.exam_repo import get_all_exams, get_exam_by_id

def list_exams(db):
    return get_all_exams(db)

def fetch_exam(db, exam_id: str):
    return get_exam_by_id(db, exam_id)