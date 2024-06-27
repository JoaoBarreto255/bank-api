"""
Test module for balance controllers.
"""

from fastapi.testclient import TestClient
from api.controllers.balances_controller import BALANCES_ROUTER
from api.models.account import Account
from api.repositories.account_repository import get_account_repository

client = TestClient(BALANCES_ROUTER)
accounts = get_account_repository()


def test_post_reset() -> None:
    accounts.save_account(Account("foo", 20))
    assert accounts.find_account("foo") is not None

    response = client.post("/reset")
    assert response.status_code == 200
    assert response.text == "OK"

    assert accounts.find_account("foo") is None
    
def test_get_balances() -> None:
    response = client.get("/balances?account_id=baz")
    assert response.status_code == 404
    assert response.text == "0"
    
    accounts.save_account(Account("baz", 20))
    response = client.get("/balances?account_id=baz")
    assert response.status_code == 200
    assert response.text == "20"
    accounts.reset_accounts()
