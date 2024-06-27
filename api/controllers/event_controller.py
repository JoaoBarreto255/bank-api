"""
Router Module for Control Event path
"""

from fastapi import Response, status, HTTPException
from fastapi.routing import APIRouter
from api.services.account_service import AccountServiceDependecy
from api.forms.event_form import EventType

EVENT_ROUTER = APIRouter()


@EVENT_ROUTER.post("/event", status_code=status.HTTP_201_CREATED)
async def event(
    event_input: EventType, account_service_manager: AccountServiceDependecy
):
    try:
        return event_input.event_action(account_service_manager)
    except HTTPException as error:
        return Response('0', error.status_code)