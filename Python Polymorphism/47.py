class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __eq__(self, r):
        return self.length * self.width == r.length * r.width
r1 = Rectangle(5, 4)
r2 = Rectangle(10, 2)
print(r1 == r2)