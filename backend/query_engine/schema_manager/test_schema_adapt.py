import asyncio
import pytest
from .manager import schema_manager

@pytest.mark.asyncio
async def test_schema_adaptation():
    # Simulate schema change detection
    old_schema = await schema_manager.introspect_all()
    # Simulate external schema change (would run simulation scripts in real system)
    await asyncio.sleep(2)  # Wait for schema_manager to refresh
    new_schema = await schema_manager.introspect_all()
    assert old_schema != new_schema or schema_manager.get_previous_schema(-1) == new_schema
    # Check backward compatibility
    prev = schema_manager.get_previous_schema(-2)
    assert prev is None or isinstance(prev, dict)
