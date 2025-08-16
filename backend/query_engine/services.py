from .db.orchestrator import orchestrate_query
from .llm.langchain_adapter import nl_to_query
from .cache.redis_cache import get_cached_result, set_cached_result
from .db.schema_introspect import get_current_schema

class AskService:
    async def handle_ask(self, request, user):
        question = request.get("question")
        cache_key = f"ask:{question}"
        cached = await get_cached_result(cache_key)
        if cached:
            return {"cached": True, "result": cached}
        # Introspect schema
        schema = await get_current_schema()
        # Use LLM to generate query
        query, db_targets = await nl_to_query(question, schema)
        # Orchestrate query execution
        result = await orchestrate_query(query, db_targets)
        await set_cached_result(cache_key, result)
        return {"cached": False, "result": result}

ask_service = AskService()
