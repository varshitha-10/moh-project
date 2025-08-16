# SQL Injection Prevention
from typing import Any, Tuple

def parameterize_query(query: str, params: Tuple[Any, ...]):
    # Use DB driver parameterization, not string formatting
    return query, params
