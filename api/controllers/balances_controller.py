"""
Controller setting for not used responses
"""

from fastapi.routing import APIRouter

BALANCES_ROUTER = APIRouter()


@BALANCES_ROUTER.post("/reset")
async def reset():
    return "OK"


@BALANCES_ROUTER.get("/balances")
async def balances(account_id: int | str = None) -> int:
    return 0
