class UPIPayment:
    def pay(self):
        print("Payment using UPI")
class CardPayment:
    def pay(self):
        print("Payment using Card")
def process_payment(payment):
    payment.pay()
upi = UPIPayment()
card = CardPayment()
process_payment(upi)
process_payment(card)