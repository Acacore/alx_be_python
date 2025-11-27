class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        return self.account_balance + amount

    def withdraw(self, amount):
        balance = self.account_balance - amount
        
        if balance >= 0:
            return balance
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: ${self.account_balance}"
