class ShoppingCart:
    def __init__(self, items):
        self.items = items
    def __add__(self, cart):
        return ShoppingCart(self.items + cart.items)
c1 = ShoppingCart(["Pen", "Book"])
c2 = ShoppingCart(["Bag", "Pencil"])
c3 = c1 + c2
print(c3.items)