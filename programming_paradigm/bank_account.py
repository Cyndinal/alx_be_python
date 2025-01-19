
class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance +=amount

    def withdraw(self,amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return "Insufficient balance"




    def display_balance(self):
        return f"Current Balance: ${self.account_balance}.2f"
