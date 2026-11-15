from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    redis_url: str
    database_url: str
