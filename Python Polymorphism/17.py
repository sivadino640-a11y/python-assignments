class BankAccount:
    def calculate_interest(self):
        print("Bank account interest")
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings account interest")
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current account has no interest")
s = SavingsAccount()
c = CurrentAccount()
s.calculate_interest()
c.calculate_interest()