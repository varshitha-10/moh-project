import aiosqlite
import os

async def query_sqlite(query):
    db_path = os.getenv('SQLITE_PATH', '/data/sqlite.db')
    async with aiosqlite.connect(db_path) as db:
        async with db.execute(query) as cursor:
            rows = await cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
