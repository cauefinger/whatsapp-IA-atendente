from pydantic_settings import BaseSettings


# adicionar tipo para o pydantic validar

class Settings(BaseSettings):
    redis_url: str
    database_url: str
