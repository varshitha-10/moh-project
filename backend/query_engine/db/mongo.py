import motor.motor_asyncio
import os

async def query_mongo(query):
    # query: {collection, filter, projection}
    uri = f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME','user')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD','password')}@{os.getenv('MONGO_HOST','mongo')}:27017"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['testdb']
    collection = db[query['collection']]
    cursor = collection.find(query.get('filter', {}), query.get('projection'))
    result = await cursor.to_list(length=100)
    return result
