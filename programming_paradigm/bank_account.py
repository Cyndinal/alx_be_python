
class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance +=amount
    def withdraw(self,amount):
        self.account_balance -= amount
        print(f"Withdrew {amount}")
        if amount > self.account_balance:
            print("Insufficient balance")
    def display_balance(self):
        self.account_balance = float(self.account_balance)
        print(f"Current Balance: ${self.account_balance}")
