"""
Account model
"""

from dataclasses import dataclass


@dataclass
class Account:
    """Client accounts"""

    account_id: str
    balance: int
