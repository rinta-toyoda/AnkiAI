from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.api import api_router
from app.core.config import settings

app = FastAPI(
    title="AnkiAI Backend",
    description="Backend API for AnkiAI flashcard application",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health")
async def health_check():
    """Health check endpoint for Docker health checks"""
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "service": "ankiai-backend"}
    )

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "AnkiAI Backend API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }