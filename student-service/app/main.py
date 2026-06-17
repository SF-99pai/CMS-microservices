from fastapi import FastAPI

from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Service")

app.include_router(router)

@app.get("/")
def health_check():
    return {"message": "Student Service Running"}