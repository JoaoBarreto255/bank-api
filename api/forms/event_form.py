"""
Module for form types
"""

from typing import Literal, Union, Annotated
from pydantic import BaseModel, Field


class AbstractEventInput(BaseModel):
    amount: int = Field(ge=0)


class DepositEventInput(AbstractEventInput):
    type: Literal["deposit"]
    destination: str = Field(min_length=1)


class WithdrawEventInput(AbstractEventInput):
    type: Literal["withdraw"]
    origin: str = Field(min_length=1)


class TranferEventInput(AbstractEventInput):
    type: Literal["transfer"]
    origin: str = Field(min_length=1)
    destination: str = Field(min_length=1)


EventType = Annotated[
    Union[TranferEventInput, WithdrawEventInput, DepositEventInput],
    Field(discriminator="type"),
]
