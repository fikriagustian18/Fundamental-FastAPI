from app.core.settings import settings
from datetime import datetime, timedelta
from pwdlib import PasswordHash
from typing import Optional
import jwt

password_hash = PasswordHash.recommended()

async def authenticate_user(password: str, hashed_password: str):
    return password_hash.verify(password, hashed_password)

async def create_access_token(data: dict, expires_delta: Optional[timedelta]):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + expires_delta})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

async def create_hashed_password(password: str):
    return password_hash.hash(password)
