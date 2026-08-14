from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account interest is 4%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account interest is 2%")


savings = SavingsAccount()
current = CurrentAccount()

savings.calculate_interest()
current.calculate_interest()