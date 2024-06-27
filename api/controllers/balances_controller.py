"""
Controller setting for not used responses
"""

from fastapi import Depends
from fastapi.routing import APIRouter
from api.repositories.account_repository import get_account_repository

BALANCES_ROUTER = APIRouter()


@BALANCES_ROUTER.post("/reset")
async def reset(account_repository=Depends(get_account_repository)):
    account_repository.reset_accounts()
    return "OK"


@BALANCES_ROUTER.get("/balances")
async def balances(
    account_id: str = None, account_repository=Depends(get_account_repository)
) -> int:
    account_repository.find_account(account_id)
    return 0
