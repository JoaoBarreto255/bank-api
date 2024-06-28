"""
Test module for event_controller
"""

from fastapi.testclient import TestClient
from api.controllers.event_controller import EVENT_ROUTER
from api.repositories.account_repository import get_account_repository

client = TestClient(EVENT_ROUTER)
repository = get_account_repository()


def test_events_controller() -> None:
    repository.reset_accounts()

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
