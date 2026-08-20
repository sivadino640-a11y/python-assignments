class Money:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, m):
        return Money(self.amount + m.amount)
m1 = Money(100)
m2 = Money(200)
m3 = m1 + m2
print(m3.amount)