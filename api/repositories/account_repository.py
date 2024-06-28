"""
Repository of accounts
"""

from typing import Optional, Self, Annotated
from fastapi import Depends
from api.models.account import Account


class AccountRepository:
    """
    Manage account api storage
    """

    __instance = None

    def __init__(self):
        self.__accounts: dict[str, Account] = {}

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def find_account(self, account_id: str) -> Optional[Account]:
        """Get one account by id"""
        return self.__accounts.get(account_id)

    def save_account(self, account: Account) -> Self:
        """Save/Update account"""
        self.__accounts[account.account_id] = account
        return self

    def reset_accounts(self) -> Self:
        """Clean all accounts"""

        self.__accounts = {}
        return self


def get_account_repository() -> AccountRepository:
    return AccountRepository.get_instance()


AccountRepositoryManager = Annotated[
    AccountRepository, Depends(get_account_repository)
]
