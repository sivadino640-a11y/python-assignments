class Payment:
    def pay(self):
        print("Payment")
class UPI(Payment):
    def pay(self):
        print("Payment using UPI")
class CreditCard(Payment):
    def pay(self):
        print("Payment using Credit Card")
class NetBanking(Payment):
    def pay(self):
        print("Payment using Net Banking")
u = UPI()
c = CreditCard()
n = NetBanking()
u.pay()
c.pay()
n.pay()