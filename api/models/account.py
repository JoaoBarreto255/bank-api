"""
Account model
"""


@dataclasses
class Account:
    """Client accounts"""
    
    account_id: str
    balance: int

