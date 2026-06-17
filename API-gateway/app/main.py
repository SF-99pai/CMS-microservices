from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="College Management API Gateway",
    description="Single Entry Point for Student, Teacher and Department Services",
    version="1.0"
)

app.include_router(router)