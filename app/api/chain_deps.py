
from app.crud.database import SessionLocal
from app.crud.users import CRUDUser
from app.api.authentication_deps import create_hashed_password
from fastapi import Depends

# Dependency to get the DB session per request
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def form_user(username: str, password: str, role_type: str):
    return { "username": username, "password": password, "role_type": role_type }

async def create_user(user: dict = Depends(form_user), db: dict = Depends(get_db)):
    user["hashed_password"] = await create_hashed_password(user["password"])
    return CRUDUser().create_user(db, user)

async def get_user(username: str, db = Depends(get_db)):
    return CRUDUser().get_user_by_username(db, username)
