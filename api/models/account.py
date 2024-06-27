"""
Account model
"""

from dataclasses import dataclass


@dataclass
class Account:
    """Client accounts"""

    account_id: str
    balance: int

    def to_dict(self):
        return {"id": self.account_id, "balance": self.balance}
