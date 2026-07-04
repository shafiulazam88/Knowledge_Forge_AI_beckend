from fastapi import FastAPI

from app.core.config import get_settings
from app.modules.users.router import router as user_router

settings = get_settings()

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
)

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.app_name}!"}

@app.get("/health")

def health():
    return{
        "status": "healthy",
    }

@app.get("/config")

def config():
    return{
        "database":"settings.database_url",   
    }

app.include_router(user_router)