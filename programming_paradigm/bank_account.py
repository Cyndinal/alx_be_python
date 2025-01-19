#
# class BankAccount:
#     def __init__(self,initial_balance=0):
#         self.account_balance = initial_balance
#
#     def deposit(self,amount):
#         self.account_balance +=amount
#
#     def withdraw(self,amount):
#         if 0 < amount <= self.account_balance:
#             self.account_balance -= amount
#         return "Insufficient funds."
#
#     def display_balance(self):
#         return f"Current Balance: ${self.account_balance}"


class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current balance: ${self._account_balance:.2f}")