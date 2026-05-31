from fastapi import FastAPI, APIRouter
from app.core.settings import settings
from app.api.routes.dependency_injection import router as di_router
import uvicorn

app = FastAPI(
    title="Understanding FastAPI Fundamentals: Dependency Injection, Pydantic, and Background Tasks",
    description="Understanding the fundamentals of FastAPI, especially three important concepts: Dependency Injection, Pydantic Models, and Background Tasks. The explanation includes concepts and implementation examples to simplify understanding and provide a clear overview of their usage.",
    version=settings.version
)

# Parent router
parent_router = APIRouter(prefix=settings.prefix_version)
parent_router.include_router(di_router, prefix="/dependency-injection", tags=["Dependency Injection"])

# Router / Endpoint Integration
app.include_router(parent_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)