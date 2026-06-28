from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_exams():
    return [
        {"id": "upsc", "name": "UPSC Civil Services"},
        {"id": "ssc", "name": "SSC CGL"}
    ]

@router.get("/{exam_id}")
def get_exam(exam_id: str):
    return {
        "id": exam_id,
        "name": "Mock Exam",
        "status": "active"
    }