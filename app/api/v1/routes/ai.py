from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    exam_id: str
    mode: str = "hybrid"

@router.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": "AI response will be generated using RAG + LLM layer",
        "sources": [],
        "followups": []
    }