class upipayement:
    def pay(self):
        return "Paying through UPI"
class creditcardpayment:
    def pay(self):
        return "Paying through Credit Card"
class cashpayment:
    def pay(self):
        return "Paying through Cash"
upi = upipayement()
creditcard = creditcardpayment()
cash = cashpayment()
print(upi.pay())
print(creditcard.pay())
print(cash.pay())
