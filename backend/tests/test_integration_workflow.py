import pytest
from fastapi.testclient import TestClient
from query_engine.main import app

client = TestClient(app)

def test_ask_endpoint():
    resp = client.post('/ask', json={'question': 'show all customers'})
    assert resp.status_code == 200
    assert 'result' in resp.json()
