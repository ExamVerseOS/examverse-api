from fastapi import APIRouter
from app.api.v1.routes import exams, search, ai, tools

api_router = APIRouter()

api_router.include_router(exams.router, prefix="/exams", tags=["Exams"])
api_router.include_router(search.router, prefix="/search", tags=["Search"])
api_router.include_router(ai.router, prefix="/ai", tags=["AI"])
api_router.include_router(tools.router, prefix="/tools", tags=["Tools"])