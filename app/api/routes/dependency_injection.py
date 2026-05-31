from fastapi import APIRouter, Depends
from app.api.simple_deps import common_params

router = APIRouter()

@router.get("/items/")
async def read_items(commons: dict = Depends(common_params)):
    return commons