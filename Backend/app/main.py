from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.config import settings
from app.db.session import get_db

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/")
def read_root():
    return {
        "message": f"{settings.PROJECT_NAME} is running",
        "environment": settings.ENV,
    }

@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {
        "status": "ok",
        "database": "connected",
    }