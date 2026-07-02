from fastapi import FastAPI

from app.core.config import get_settings

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