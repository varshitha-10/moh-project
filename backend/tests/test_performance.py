import pytest
import asyncio
from httpx import AsyncClient
from query_engine.main import app

@pytest.mark.asyncio
async def test_concurrent_queries():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        tasks = [ac.post('/ask', json={'question': f'query {i}'}) for i in range(1000)]
        responses = await asyncio.gather(*tasks)
        assert all(r.status_code == 200 for r in responses)
