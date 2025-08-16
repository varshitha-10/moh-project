import spacy
from typing import List, Dict, Any

# Load spaCy model (en_core_web_trf for transformer-based parsing)
nlp = spacy.load("en_core_web_trf")

class QueryContext:
    def __init__(self):
        self.last_query = None
        self.clarifications = []

    def update(self, query: str):
        self.last_query = query
        self.clarifications = []

    def add_clarification(self, question: str):
        self.clarifications.append(question)

context = QueryContext()

def parse_multi_intent(query: str) -> List[str]:
    # Simple split on 'and', can be improved with dependency parsing
    doc = nlp(query)
    intents = []
    current = []
    for token in doc:
        if token.text.lower() == 'and':
            if current:
                intents.append(' '.join(current))
                current = []
        else:
            current.append(token.text)
    if current:
        intents.append(' '.join(current))
    return [i.strip() for i in intents if i.strip()]

def detect_temporal_phrases(query: str) -> List[str]:
    # Look for temporal expressions
    doc = nlp(query)
    return [ent.text for ent in doc.ents if ent.label_ in ('DATE', 'TIME', 'DURATION')]

def resolve_ambiguity(query: str) -> Any:
    # Placeholder: if query is ambiguous, return a clarifying question
    if 'thing' in query or 'stuff' in query:
        clarification = "Which specific entity do you mean by 'thing' or 'stuff'?"
        context.add_clarification(clarification)
        return clarification
    return None

def maintain_context(query: str):
    context.update(query)

def generate_dialect_sql(intent: str, db_type: str) -> str:
    # Placeholder: generate SQL for the given DB dialect
    if db_type == 'postgres':
        return f"-- PostgreSQL SQL for: {intent}"
    elif db_type == 'mysql':
        return f"-- MySQL SQL for: {intent}"
    elif db_type == 'sqlite':
        return f"-- SQLite SQL for: {intent}"
    else:
        return f"-- Unknown DB dialect for: {intent}"

def generate_mongo_pipeline(intent: str) -> dict:
    # Placeholder: generate MongoDB aggregation pipeline
    return {"pipeline": f"// Mongo pipeline for: {intent}"}

def advanced_parse(query: str, db_types: List[str]) -> Dict[str, Any]:
    maintain_context(query)
    ambiguity = resolve_ambiguity(query)
    if ambiguity:
        return {"clarification": ambiguity}
    intents = parse_multi_intent(query)
    temporal = [detect_temporal_phrases(i) for i in intents]
    results = {}
    for idx, intent in enumerate(intents):
        for db in db_types:
            if db == 'mongo':
                results[f"mongo_{idx}"] = generate_mongo_pipeline(intent)
            else:
                results[f"{db}_{idx}"] = generate_dialect_sql(intent, db)
    return {"parsed": results, "temporal": temporal, "context": context.last_query}
