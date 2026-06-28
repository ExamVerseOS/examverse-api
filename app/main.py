from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(
    title="ExamVerseOS API",
    version="1.0.0",
    description="Universal AI-powered Exam Intelligence API"
)

app.include_router(api_router, prefix="/v1")

@app.get("/")
def root():
    return {
        "status": "ExamVerseOS API running",
        "version": "1.0.0"
    }