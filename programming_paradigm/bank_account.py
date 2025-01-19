
class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance +=amount

    def withdraw(self,amount):
        if amount > self.account_balance:
            print(f"Insufficient funds.")
        else:
            print(f"Withdrew: ${amount:.2f}")

    def display_balance(self):
        self.account_balance = float(self.account_balance)
        print(f"Current Balance: ${self.account_balance}")
