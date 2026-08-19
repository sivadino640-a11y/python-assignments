class UPI:
    def pay(self):
        print("Payment using UPI")
class CreditCard:
    def pay(self):
        print("Payment using Credit Card")
class Cash:
    def pay(self):
        print("Payment using Cash")
def process_payment(payment):
    payment.pay()
process_payment(UPI())
process_payment(CreditCard())
process_payment(Cash())