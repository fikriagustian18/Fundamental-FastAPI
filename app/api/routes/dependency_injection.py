from app.api.simple_deps import common_params, form_data_params
from app.api.authentication_deps import authenticate_user, create_access_token
from app.core.exceptions import Unauthorized
from fastapi import APIRouter, Depends
from datetime import timedelta

router = APIRouter()

@router.get("/items/")
async def read_items(commons: dict = Depends(common_params)):
    return commons


@router.post("/login")
async def read_items(form_data: dict = Depends(form_data_params)):
    user = await authenticate_user(
        form_data["username"],
        form_data["password"]
    )
    if not user:
        raise Unauthorized(detail="Incorrect username or password")
    access_token = await create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=30)
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }