from fastapi import APIRouter
from app.api.content_generation import router as content_router

api_router = APIRouter()

# Include the content generation router
api_router.include_router(content_router, tags=["content-generation"])