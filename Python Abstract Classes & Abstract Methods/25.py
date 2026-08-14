from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass


class Electronics(Product):
    def calculate_discount(self):
        discount = self.price * 0.10
        print("Discount:", discount)
        print("Final Price:", self.price - discount)


class Clothing(Product):
    def calculate_discount(self):
        discount = self.price * 0.20
        print("Discount:", discount)
        print("Final Price:", self.price - discount)


laptop = Electronics("Laptop", 50000)
shirt = Clothing("Shirt", 2000)

print(laptop.product_name, laptop.price)
laptop.calculate_discount()

print(shirt.product_name, shirt.price)
shirt.calculate_discount()