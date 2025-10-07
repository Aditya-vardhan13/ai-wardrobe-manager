from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from auth import get_current_user
from config import settings
import uvicorn

app = FastAPI(
    title="Wardrobe Manager API",
    description="AI-powered wardrobe management system",
    version="1.0.0"
)

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Wardrobe Manager API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Protected routes
@app.get("/auth/me")
async def get_current_user_info(current_user: dict = Depends(get_current_user)):
    """Get current authenticated user information"""
    return {
        "user": current_user,
        "message": "Authentication successful"
    }

@app.get("/wardrobe/items")
async def get_wardrobe_items(current_user: dict = Depends(get_current_user)):
    """Get user's wardrobe items (placeholder for now)"""
    return {
        "user_id": current_user["user_id"],
        "items": [],  # Will be populated in Stage 3
        "message": "Wardrobe items endpoint ready"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
