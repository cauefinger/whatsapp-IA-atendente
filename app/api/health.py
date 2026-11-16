from fastapi import APIRouter
from app.db import engine
from sqlalchemy import text
from app.cache import redis_client 

health = APIRouter()

@health.get("/health")

postgres_status = "ok"

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

except Exception as e:
    postgres_status = str(e)

redis_status = "ok"

try:
    redis_client.ping()
    
except Exception as e:
    redis_status = str(e)