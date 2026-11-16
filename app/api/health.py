from fastapi import APIRouter
from app.db import engine

health = APIRouter()

@health.get("/health")

postgres_status = "ok"

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

except postgres_status as e:
    postgres_status = str(e)

