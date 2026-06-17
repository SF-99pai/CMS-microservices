from fastapi import FastAPI

from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Department Service")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Department Service Running"}