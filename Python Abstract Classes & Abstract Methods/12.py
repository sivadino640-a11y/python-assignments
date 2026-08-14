from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle Area:", self.length * self.width)

    def perimeter(self):
        print("Rectangle Perimeter:", 2 * (self.length + self.width))


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", math.pi * self.radius ** 2)

    def perimeter(self):
        print("Circle Perimeter:", 2 * math.pi * self.radius)


rectangle = Rectangle(10, 5)
circle = Circle(7)

rectangle.area()
rectangle.perimeter()

circle.area()
circle.perimeter()