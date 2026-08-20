class Payment:
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Payment using UPI")
class Card(Payment):
    def pay(self):
        print("Payment using Card")
class NetBanking(Payment):
    def pay(self):
        print("Payment using Net Banking")
UPI().pay()
Card().pay()
NetBanking().pay()