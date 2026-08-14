from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self):
        pass


class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)


class CreditCardPayment(Payment):
    def pay(self):
        print("Paid using Credit Card")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)


class NetBankingPayment(Payment):
    def pay(self):
        print("Paid using Net Banking")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)


upi = UPIPayment(1000, "UPI101")
card = CreditCardPayment(2000, "CARD102")
netbanking = NetBankingPayment(3000, "NET103")

upi.pay()
card.pay()
netbanking.pay()