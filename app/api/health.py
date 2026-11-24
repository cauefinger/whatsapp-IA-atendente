from fastapi import APIRouter
from app.db import engine, redis_client
from sqlalchemy import text
from fastapi.responses import JSONResponse


# navegador → localhost:8000 (PC) → Docker → container api:8000 → uvicorn

router = APIRouter()

@router.get("/health")
def health_check():
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

    resultado = {"postgres": postgres_status, "redis": redis_status}

    if postgres_status == "ok" and redis_status == "ok":
        return JSONResponse(content=resultado, status_code=200)

    return JSONResponse(content=resultado, status_code=503)