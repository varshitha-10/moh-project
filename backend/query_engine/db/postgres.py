import asyncpg
import os

async def query_postgres(query):
    conn = await asyncpg.connect(
        user=os.getenv('POSTGRES_USER', 'user'),
        password=os.getenv('POSTGRES_PASSWORD', 'password'),
        database=os.getenv('POSTGRES_DB', 'testdb'),
        host=os.getenv('POSTGRES_HOST', 'postgres')
    )
    try:
        result = await conn.fetch(query)
        return [dict(r) for r in result]
    finally:
        await conn.close()
