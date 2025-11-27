class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        return self.account_balance + amount

    def withdraw(self, amount):
        return self.account_balance - amount

    def display_balance(self):
        return f"Current Balance:{self.account_balance}"
