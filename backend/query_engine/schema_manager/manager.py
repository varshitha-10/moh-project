import asyncio
import time
from typing import Dict, Any
from ..db import postgres, mysql, sqlite, mongo

class SchemaManager:
    def __init__(self):
        self.cache = {}
        self.last_update = 0
        self.schema_history = []
        self.lock = asyncio.Lock()

    async def introspect_all(self) -> Dict[str, Any]:
        async with self.lock:
            now = time.time()
            # Refresh every 60 seconds
            if now - self.last_update > 60 or not self.cache:
                schemas = await asyncio.gather(
                    self.introspect_postgres(),
                    self.introspect_mysql(),
                    self.introspect_sqlite(),
                    self.introspect_mongo()
                )
                new_schema = {
                    'postgres': schemas[0],
                    'mysql': schemas[1],
                    'sqlite': schemas[2],
                    'mongo': schemas[3]
                }
                self.detect_changes(new_schema)
                self.cache = new_schema
                self.last_update = now
            return self.cache

    async def introspect_postgres(self):
        # Query PostgreSQL information_schema
        query = """
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public';
        """
        return await postgres.query_postgres(query)

    async def introspect_mysql(self):
        query = """
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = DATABASE();
        """
        return await mysql.query_mysql(query)

    async def introspect_sqlite(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = await sqlite.query_sqlite(query)
        schema = {}
        for t in tables:
            tname = t['name']
            cols = await sqlite.query_sqlite(f"PRAGMA table_info({tname});")
            schema[tname] = cols
        return schema

    async def introspect_mongo(self):
        # List collections and sample docs
        collections = ['user_profiles', 'product_catalogs', 'activity_logs', 'recommendations']
        schema = {}
        for c in collections:
            sample = await mongo.query_mongo({'collection': c, 'filter': {}, 'projection': {}})
            schema[c] = sample[:1] if sample else []
        return schema

    def detect_changes(self, new_schema):
        if not self.schema_history or self.schema_history[-1] != new_schema:
            self.schema_history.append(new_schema)
            # Here you could add logic to diff schemas and trigger updates

    def get_previous_schema(self, version=-1):
        if self.schema_history:
            return self.schema_history[version]
        return None

schema_manager = SchemaManager()
