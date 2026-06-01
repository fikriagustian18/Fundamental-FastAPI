from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi import status

class Unauthorized(Exception):
    def __init__(self, detail: str):
        self.detail = detail

def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(Unauthorized)
    async def item_not_found_exception_handler(request: Request, exc: Unauthorized):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "success": False,
                "error_code": "Unauthorized",
                "message": exc.detail
            }
        )