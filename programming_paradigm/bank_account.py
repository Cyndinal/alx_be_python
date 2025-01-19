
class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance +=amount

    def withdraw(self,amount):
        if self.account_balance < amount:
            return "Insufficient funds ."
        else:
            return f"Withdrew: ${amount}"



    def display_balance(self):
        return f"Current Balance: ${float(self.account_balance)}"
