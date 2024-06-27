"""
Module service to made changes in accounts
"""

from fastapi import Depends, HTTPException, status
from typing import Annotated

from api.models.account import Account
from api.repositories.account_repository import (
    AccountRepository,
    get_account_repository,
)


class AccountService:
    """
    Handle change in accounts such increment and decrement values.
    """

    def __init__(self, account_repository: AccountRepository) -> None:
        if not isinstance(account_repository, AccountRepository):
            raise TypeError(
                f""""account_repository" argument must be "AccountRepository" type. \
                Found "{str(type(account_repository))}"!
                """
            )

        self.repository = account_repository

    def increment_account(self, account_id: str, amount: int) -> dict:
        """
        Increment account and returns its current state.
        Case account exists create a new one an save it.
        """
        account = self.repository.find_account(account_id) or Account(
            account_id, 0
        )
        account.balance += amount
        self.repository.save_account(account)

        return account.to_dict()

    def decrement_account(self, account_id: str, amount: int) -> dict:
        """
        Decrease account value if its is possible. Otherwise raise an exception
        """

        account = self.repository.find_account(account_id)
        if account is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        if account.balance < amount:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        account.balance -= amount
        self.repository.save_account(account)

        return account.to_dict()


def factory_account_service(
    account_repository: Annotated[
        AccountRepository, Depends(get_account_repository)
    ]
):
    return AccountService(account_repository)


AccountServiceDependecy = Annotated[
    AccountService, Depends(factory_account_service)
]
