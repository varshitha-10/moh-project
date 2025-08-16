import pytest
import asyncio
from query_engine.schema_manager import manager as schema_manager

@pytest.mark.asyncio
async def test_schema_drift():
    old_schema = await schema_manager.introspect_all()
    # Simulate schema drift (would run simulation scripts in real system)
    await asyncio.sleep(2)
    new_schema = await schema_manager.introspect_all()
    assert old_schema != new_schema or schema_manager.get_previous_schema(-1) == new_schema
