import redis.asyncio as redis
import os

_redis = None
async def get_redis():
    global _redis
    if _redis is None:
        _redis = await redis.from_url(os.getenv('REDIS_URL', 'redis://redis:6379/0'))
    return _redis

async def get_cached_result(key):
    r = await get_redis()
    val = await r.get(key)
    if val:
        return val.decode() if isinstance(val, bytes) else val
    return None

async def set_cached_result(key, value):
    r = await get_redis()
    await r.set(key, str(value), ex=3600)
