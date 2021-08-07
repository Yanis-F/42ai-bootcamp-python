
from typing import Union


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount



class Bank:
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        if type(account) is not Account:
            raise TypeError("account must be an instance of Account")
        if self.is_corrupted(account):
            raise Exception("account is corrupted")

        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """

        try:
            origin_acc = self._get_account(origin)
            dest_acc = self._get_account(dest)
        except Exception:
            return False

        if self.is_corrupted(origin_acc) or self.is_corrupted(dest_acc):
            return False

        if origin_acc.value < amount:
            return False

        origin_acc.transfer(-amount)
        dest_acc.transfer(amount)

        return True

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        try:
            acc = self._get_account(account)
        except Exception:
            return False

        acc.value = 0

    def is_corrupted(self, account: Account) -> bool:
        attributes = dir(account)

        return len(attributes) % 2 == 0 \
            and any(a for a in attributes if a.startswith("b"))\
            and not any(a for a in attributes if a.startswith("zip") or a.startswith("addr"))\
            and "name" not in attributes\
            and "id" not in attributes\
            and "value" not in attributes

    def _get_account(self, account: Union[str, int]):
        if type(account) is int:
            return self.account[account]
        elif type(account) is str:
            return next(acc for acc in self.account if acc.name == account)
        else:
            raise TypeError()