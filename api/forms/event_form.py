"""
Module for form types
"""

from typing import Literal, Union, Annotated
from pydantic import BaseModel, Field
from fastapi import HTTPException

from api.services.account_service import AccountService


class AbstractEventInput(BaseModel):
    amount: int = Field(ge=0)

    def event_action(self, account_service: AccountService) -> dict:
        raise NotImplementedError()


class DepositEventInput(AbstractEventInput):
    type: Literal["deposit"]
    destination: str = Field(min_length=1)

    def event_action(self, account_service: AccountService) -> dict:
        account_state = account_service.increment_account(
            self.destination, self.amount
        )
        return {"destination": account_state}


class WithdrawEventInput(AbstractEventInput):
    type: Literal["withdraw"]
    origin: str = Field(min_length=1)

    def event_action(self, account_service: AccountService) -> dict:
        account_state = account_service.decrement_account(
            self.origin, self.amount
        )
        return {"origin": account_state}


class TranferEventInput(AbstractEventInput):
    type: Literal["transfer"]
    origin: str = Field(min_length=1)
    destination: str = Field(min_length=1)

    def event_action(self, account_service: AccountService) -> dict:
        origin_account_state = account_service.decrement_account(
            self.origin, self.amount
        )
        destin_account_state = account_service.increment_account(
            self.destination, self.amount
        )

        return {
            "origin": origin_account_state,
            "destination": destin_account_state,
        }


EventType = Annotated[
    Union[TranferEventInput, WithdrawEventInput, DepositEventInput],
    Field(discriminator="type"),
]
