from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import db_dep
from app.services.pyq_service import list_pyqs_by_exam

router = APIRouter()

@router.get("/{exam_id}")
def pyqs(exam_id: str, db: Session = Depends(db_dep)):
    return list_pyqs_by_exam(db, exam_id)