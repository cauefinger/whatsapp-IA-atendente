from app.core.config import settings
from sqlalchemy import create_engine
from redis import Redis

engine = create_engine(settings.database_url) # engine e database_url = postgres

'''
create_engine(settings.banco_exemplo_url)
create engine utiliza o url fornecido pelo settings para criar uma conexão entre o banco e engine

'''


redis_client = Redis.from_url(settings.redis_url) # redis_client e redis_url = redis