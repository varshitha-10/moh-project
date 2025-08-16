import aiomysql
import os

async def query_mysql(query):
    conn = await aiomysql.connect(
        user=os.getenv('MYSQL_USER', 'user'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        db=os.getenv('MYSQL_DATABASE', 'testdb'),
        host=os.getenv('MYSQL_HOST', 'mysql')
    )
    try:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            result = await cur.fetchall()
            return result
    finally:
        conn.close()
