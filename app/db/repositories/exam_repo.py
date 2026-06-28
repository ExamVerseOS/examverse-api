from sqlalchemy.orm import Session
from app.db.models.exam import Exam

def get_all_exams(db: Session):
    return db.query(Exam).all()

def get_exam_by_id(db: Session, exam_id: str):
    return db.query(Exam).filter(Exam.id == exam_id).first()