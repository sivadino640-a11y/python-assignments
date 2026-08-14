from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def calculate_interest(self):
        interest = self.balance * 0.04
        print("Savings Account Interest:", interest)


class CurrentAccount(Account):
    def calculate_interest(self):
        interest = self.balance * 0.02
        print("Current Account Interest:", interest)


savings = SavingsAccount("SA101", 50000)
current = CurrentAccount("CA102", 100000)

print("Account Number:", savings.account_number)
print("Balance:", savings.balance)
savings.calculate_interest()

print("Account Number:", current.account_number)
print("Balance:", current.balance)
current.calculate_interest()