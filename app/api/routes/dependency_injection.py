from app.api.simple_deps import common_params, form_data_params
from app.api.authentication_deps import authenticate_user, create_access_token
from app.api.chain_deps import create_user, get_user, get_db
from app.core.exceptions import Unauthorized
from fastapi import APIRouter, Depends
from datetime import timedelta

router = APIRouter()

@router.get("/items/")
async def read_items(commons: dict = Depends(common_params)):
    return commons

@router.post("/login")
async def validat_items(form_data: dict = Depends(form_data_params), db = Depends(get_db)):
    user = await get_user(form_data["username"], db)
    if not user or not await authenticate_user(form_data["password"], user.hashed_password):
        raise Unauthorized(detail="Incorrect username or password")

    access_token = await create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=30)
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# Create an Users
@router.post("/users/")
async def create_item(result: dict = Depends(create_user)):
    return result