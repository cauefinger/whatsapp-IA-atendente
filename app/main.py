from fastapi import FastAPI
from app.api.health import health

app = FastAPI()

app.include_router(health)