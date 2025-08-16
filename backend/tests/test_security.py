import pytest
from query_engine.security import injection, rbac
from fastapi.testclient import TestClient
from query_engine.main import app

client = TestClient(app)

def test_sql_injection():
    # Try SQL injection in NL query
    resp = client.post('/ask', json={'question': "1; DROP TABLE users;--"})
    assert resp.status_code == 200
    assert 'DROP TABLE' not in str(resp.json())

def test_unauthorized_access():
    # Simulate unauthorized user
    rbac.access_control.set_policy('bob', 'orders', ['id'], 'reader')
    assert not rbac.access_control.check_access('alice', 'orders', 'id', 'read')
