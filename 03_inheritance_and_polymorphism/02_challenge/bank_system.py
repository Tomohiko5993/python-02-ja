from abc import ABC, abstractmethod

# 抽象基底クラス Account
class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    @abstractmethod
    def can_withdraw(self, amount):
        pass

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Withdrawal denied. Insufficient funds."

    def apply_interest(self):
        pass

    def get_transaction_history(self):
        return self.transaction_history

    def __str__(self):
        return f"Account {self.account_number}: Balance {self.balance}"

# サブクラス SavingsAccount
class SavingsAccount(Account):
    INTEREST_RATE = 0.02

    def can_withdraw(self, amount):
        return self.balance >= amount

    def apply_interest(self):
        interest = self.balance * SavingsAccount.INTEREST_RATE
        self.balance += interest
        self.transaction_history.append(f"Interest applied: {interest}")
        return f"Interest applied: {interest}. New balance: {self.balance}"

# サブクラス CheckingAccount
class CheckingAccount(Account):
    OVERDRAFT_LIMIT = -100

    def can_withdraw(self, amount):
        return self.balance - amount >= CheckingAccount.OVERDRAFT_LIMIT

    def apply_interest(self):
        # Checking accounts do not typically earn interest
        return "No interest applied for checking accounts."

# Example usage:
if __name__ == "__main__":
    alice_savings = SavingsAccount("123456", 1000)
    bob_checking = CheckingAccount("987654", 500)

    accounts = [alice_savings, bob_checking]

    print("Initial Account Details:")
    print(alice_savings)
    print(bob_checking)

    print(alice_savings.deposit(200))
    print(alice_savings.withdraw(500))
    print(bob_checking.deposit(300))
    print(bob_checking.withdraw(1000))

    print(alice_savings.get_transaction_history())
    print(bob_checking.get_transaction_history())

    print(alice_savings)
    print(bob_checking)