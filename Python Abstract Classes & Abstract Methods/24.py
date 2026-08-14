from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account Interest: 4%")


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account Interest: 2%")


savings = SavingsAccount("Ravi", "SA101")
current = CurrentAccount("Anjali", "CA102")

print(savings.account_holder, savings.account_number)
savings.calculate_interest()

print(current.account_holder, current.account_number)
current.calculate_interest()