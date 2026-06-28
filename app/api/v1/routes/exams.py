from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import db_dep
from app.services.exam_service import list_exams, fetch_exam

router = APIRouter()

@router.get("/")
def get_exams(db: Session = Depends(db_dep)):
    return list_exams(db)

@router.get("/{exam_id}")
def get_exam(exam_id: str, db: Session = Depends(db_dep)):
    return fetch_exam(db, exam_id)