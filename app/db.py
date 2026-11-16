from app.core.config import settings
from sqlalchemy import create_engine
from redis import Redis

engine = create_engine(settings.database_url)

redis_client = Redis.from_url(settings.redis_url)