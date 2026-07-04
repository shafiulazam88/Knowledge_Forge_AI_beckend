from datetime import datetime, timedelta , UTC
from typing import Any
import jwt 

from app.core.config import get_settings

settings = get_settings()

def create_access_token(
        subject:str,
        extra_data: dict[str, Any] | None = None,
     )-> str:
    expire = datetime.now(UTC)+ timedelta(minutes=settings.access_token_expire_minutes)

    payload = {
        "sub": subject,
        "exp": expire,
    }

    if extra_data:
        payload.update(extra_data)
    
    return jwt.encode(payload, 
                      settings.jwt_secret_key, 
                      algorithm=settings.jwt_algorithm
                      )


