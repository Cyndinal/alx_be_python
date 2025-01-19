
class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance +=amount

    def withdraw(self,amount):
        self.account_balance -= amount
        if amount > self.account_balance:
            return "Insufficient funds"
        else:
            return f"Withdrew: ${amount}"



    def display_balance(self):
        # self.account_balance = float(self.account_balance)
        return f"Current Balance: ${float(self.account_balance)}"
