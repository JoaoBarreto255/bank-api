"""
Test Module for account repository.
"""

from api.models.account import Account
from .account_repository import AccountRepository


def test_account_repository_get_instance() -> None:
    first = AccountRepository.get_instance()
    assert first is not None
    assert isinstance(first, AccountRepository)
    
    second = AccountRepository.get_instance()
    assert second is not None
    assert isinstance(first, AccountRepository)
    assert first is second


def test_account_repository_save_and_find_account() -> None:
    instance = AccountRepository.get_instance()
    assert instance is not None
    assert isinstance(instance, AccountRepository)
    
    assert instance.find_account("foo") is None

    assert isinstance(instance.save_account(Account("foo", 10)), AccountRepository)
    result = instance.find_account("foo")
    assert result is not None
    assert isinstance(result, Account)
    assert result.account_id == "foo"
    assert result.balance == 10
    
    instance.save_account(Account("foo", 11))
    result = instance.find_account("foo")
    assert result is not None
    assert isinstance(result, Account)
    assert result.account_id == "foo"
    assert result.balance == 11


def test_account_repository_reset_accounts():
    instance = AccountRepository.get_instance()
    assert instance is not None
    assert isinstance(instance, AccountRepository)
    
    instance.save_account(Account("foo", 10))
    instance.save_account(Account("bar", 10))
    instance.save_account(Account("baz", 10))
    
    assert instance.find_account("foo") is not None
    assert instance.find_account("bar") is not None
    assert instance.find_account("baz") is not None
    assert isinstance(instance.reset_accounts(), AccountRepository)
    assert instance.find_account("foo") is None
    assert instance.find_account("bar") is None
    assert instance.find_account("baz") is None
    