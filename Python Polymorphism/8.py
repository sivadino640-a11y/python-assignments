class upipayement:
    def pay(self):
        return "Paying UPI"
class creditcardpayment:
    def pay(self):
        return "Paying Credit Card"
class cashpayment:
    def pay(self):
        return "Paying Cash"
upi = upipayement()
creditcard = creditcardpayment()
cash = cashpayment()
print(upi.pay())
print(creditcard.pay())
print(cash.pay())
