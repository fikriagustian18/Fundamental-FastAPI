from app.core.settings import settings
from app.crud.users import CRUDUser
from datetime import datetime, timedelta
from pwdlib import PasswordHash
from typing import Optional
import jwt

password_hash = PasswordHash.recommended()

async def authenticate_user(username: str, password: str):
    user = CRUDUser().get_user_by_username(username)
    if not user or not password_hash.verify(password, user["hashed_password"]):
        return None
    return user

async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + expires_delta})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt