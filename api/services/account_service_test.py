"""
Account Service Test Module
"""

from fastapi import HTTPException
from pytest import raises

from api.models.account import Account
from api.repositories.account_repository import AccountRepository
from api.services.account_service import AccountService


def build_fresh_service_and_repo() -> tuple[AccountService, AccountRepository]:
    repository = AccountRepository()
    return AccountService(repository), repository


def test_create_and_save_new_account() -> None:
    service, repository = build_fresh_service_and_repo()
    repodata: dict = repository._AccountRepository__accounts
    assert len(repodata.items()) == 0
    service.increment_account("foo", 10)
    assert len(repodata.items()) == 1
    assert "foo" in repodata
    assert isinstance(repodata["foo"], Account)
    assert repodata["foo"].account_id == "foo"
    assert repodata["foo"].balance == 10


def test_increment_account() -> None:
    service, repository = build_fresh_service_and_repo()
    repository.save_account(account := Account("bar", 20))
    service.increment_account("bar", 30)
    assert repository.find_account("bar") is account
    assert account.account_id == "bar"
    assert account.balance == 50


def test_decrement_account_success() -> None:
    service, repository = build_fresh_service_and_repo()
    repository.save_account(account := Account("bar", 20))
    service.decrement_account("bar", 10)
    assert repository.find_account("bar") is account
    assert account.account_id == "bar"
    assert account.balance == 10

    service.decrement_account("bar", 10)
    assert repository.find_account("bar") is account
    assert account.account_id == "bar"
    assert account.balance == 0


def test_fail_decrement_account_non_existent() -> None:
    service, repository = build_fresh_service_and_repo()
    with raises(HTTPException) as error_info:
        service.decrement_account("baz", 10)
        assert error_info.value.status_code == 404


def test_fail_decrement_account_more_than_its_balance() -> None:
    service, repository = build_fresh_service_and_repo()
    repository.save_account(account := Account("baz", 20))
    with raises(HTTPException) as error_info:
        service.decrement_account("baz", 30)
        assert error_info.value.status_code == 403
