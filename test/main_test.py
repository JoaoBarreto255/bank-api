""" Module for test Api """
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_app() -> None:
    response = client.post("/reset")
    assert response.status_code == 200
    assert response.text == "OK"
    
    response = client.get("/balances?account_id=1234")
    assert response.status_code == 404
    assert response.text == "0"
    
    response = client.post(
        "/event",
        content='{"type":"deposit", "destination":"100", "amount":10}',
    )
    assert response.status_code == 201
    assert response.json() == {"destination": {"id": "100", "balance": 10}}

    response = client.post(
        "/event",
        content='{"type":"deposit", "destination":"100", "amount":10}',
    )
    assert response.status_code == 201
    assert response.json() == {"destination": {"id": "100", "balance": 20}}
    
    response = client.get("/balances?account_id=100")
    assert response.status_code == 200
    assert response.text == "20"

    response = client.post(
        "/event", content='{"type":"withdraw", "origin":"200", "amount":10}'
    )
    assert response.status_code == 404
    assert response.text == "0"

    response = client.post(
        "/event", content='{"type":"withdraw", "origin":"100", "amount":5}'
    )
    assert response.status_code == 201
    assert response.json() == {"origin": {"id": "100", "balance": 15}}

    response = client.post(
        "/event",
        content='{"type":"transfer", "origin":"100", "amount":15, "destination":"300"}',
    )
    assert response.status_code == 201
    assert response.json() == {
        "origin": {"id": "100", "balance": 0},
        "destination": {"id": "300", "balance": 15},
    }

    response = client.post(
        "/event",
        content='{"type":"transfer", "origin":"200", "amount":15, "destination":"300"}',
    )
    assert response.status_code == 404
    assert response.text == "0"
