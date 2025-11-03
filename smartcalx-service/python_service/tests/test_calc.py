import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

import pytest

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_add_default(client):
    resp = client.get('/add')
    assert resp.status_code == 200
    assert resp.json['result'] == 0

def test_add_values(client):
    resp = client.get('/add?a=2.5&b=3.5')
    assert resp.status_code == 200
    assert resp.json['result'] == 6.0
