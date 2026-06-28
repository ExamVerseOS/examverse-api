from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    exam_id: str
    mode: str = "hybrid"

@router.post("/")
def search(req: SearchRequest):
    return {
        "query": req.query,
        "results": {
            "topics": [],
            "pyqs": [],
            "concepts": []
        },
        "mode": req.mode
    }