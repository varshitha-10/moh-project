from .postgres import query_postgres
from .mysql import query_mysql
from .sqlite import query_sqlite
from .mongo import query_mongo

async def orchestrate_query(query, db_targets):
    results = {}
    if 'postgres' in db_targets:
        results['postgres'] = await query_postgres(query)
    if 'mysql' in db_targets:
        results['mysql'] = await query_mysql(query)
    if 'sqlite' in db_targets:
        results['sqlite'] = await query_sqlite(query)
    if 'mongo' in db_targets:
        results['mongo'] = await query_mongo(query)
    return results
