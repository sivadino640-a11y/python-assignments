from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        print("Circle Area:", 3.14 * self.radius * self.radius)


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle Area:", self.length * self.width)


circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 10, 5)

print("Color:", circle.color)
circle.area()

print("Color:", rectangle.color)
rectangle.area()