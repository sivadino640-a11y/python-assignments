class Product:
    def __init__(self, price):
        self.price = price
    def __add__(self, p):
        return self.price + p.price
p1 = Product(100)
p2 = Product(200)
print(p1 + p2)