"""
Controller setting for not used responses
"""

from fastapi import Response, status
from fastapi.routing import APIRouter
from api.repositories.account_repository import AccountRepositoryManager

BALANCES_ROUTER = APIRouter()


@BALANCES_ROUTER.post("/reset", response_class=Response)
async def reset(account_repository: AccountRepositoryManager):
    account_repository.reset_accounts()
    return "OK"


@BALANCES_ROUTER.get("/balances", status_code=200, response_class=Response)
async def balances(
    account_repository: AccountRepositoryManager,
    response: Response,
    account_id: str = None,
) -> str:
    if result := account_repository.find_account(account_id):
        return str(result.balance)

    response.status_code = status.HTTP_404_NOT_FOUND
    return "0"
