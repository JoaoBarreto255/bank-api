"""
Router Module for Control Event path
"""

from fastapi import Depends, Response, status
from fastapi.routing import APIRouter
from api.repositories.account_repository import get_account_repository

EVENT_ROUTER = APIRouter()


@EVENT_ROUTER.post("/event", status_code=status.HTTP_201_CREATED)
async def event(account_repository=Depends(get_account_repository)):
    account_repository.find_account("foo")
    return Response("0", status.HTTP_404_NOT_FOUND)
