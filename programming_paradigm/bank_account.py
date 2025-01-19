
class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = account_balance

    def deposit(self,amount):
        self.account_balance +=amount
    def withdraw(self,amount):
        self.account_balance -= amount
    def display_balance(self):
        self.account_balance = float(self.account_balance)
        print(f"The account balance is {self.account_balance}")
