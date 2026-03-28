# app/core/security.py
from fastapi import HTTPException
from app.core.config import settings

def validate_email(email: str):
    if not email.endswith(f"@{settings.ALLOWED_DOMAIN}"):
        raise HTTPException(status_code=403, detail="Unauthorized domain")