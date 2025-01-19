
class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance +=amount

    def withdraw(self,amount):
        if self.account_balance < amount:
            if not self.account_balance > amount:
                return f"Withdrew: ${amount}"
        return "Insufficient funds ."




    def display_balance(self):
        return f"Current Balance: ${self.account_balance}.2f"
