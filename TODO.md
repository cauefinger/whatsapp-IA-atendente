# TODO (próximos passos imediatos)
# 1. Subir o projeto com "docker compose up --build" e abrir http://localhost:8000/health.
# 2. Conferir se a resposta vem com postgres e redis marcados como "ok".
# 3. Parar o Redis com "docker compose stop redis" e ver se o /health responde 503 com o redis como falha.
# 4. Juntar os dois imports de app.db em uma linha só no health.py.
# 5. Renomear o router de "health" para "router" no health.py e ajustar o main.py.
# 6. Mover o redis_client do db.py para um arquivo próprio, app/cache.py.