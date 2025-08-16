import pytest
from query_engine.services import ask_service
from query_engine.nlp import query_parser
from query_engine.security import injection, rbac, masking

def test_multi_intent_parsing():
    q = "show revenue and top products"
    intents = query_parser.parse_multi_intent(q)
    assert len(intents) == 2

def test_temporal_detection():
    q = "sales in last 6 months"
    temporal = query_parser.detect_temporal_phrases(q)
    assert temporal

def test_masking():
    row = {'email': 'user@example.com', 'phone': '1234567890'}
    masked = masking.mask_row(row)
    assert masked['email'] != row['email']
    assert masked['phone'] != row['phone']

def test_rbac():
    rbac.access_control.set_policy('alice', 'customers', ['email'], 'reader')
    assert rbac.access_control.check_access('alice', 'customers', 'email', 'read')
    assert not rbac.access_control.check_access('bob', 'customers', 'email', 'read')

def test_sql_injection_prevention():
    q, params = injection.parameterize_query('SELECT * FROM users WHERE id=%s', (1,))
    assert '%s' in q or '?' in q
