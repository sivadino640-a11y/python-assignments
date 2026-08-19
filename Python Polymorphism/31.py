class Rectangle:
    def area(self):
        print("Rectangle area")
class Circle:
    def area(self):
        print("Circle area")
class Triangle:
    def area(self):
        print("Triangle area")
def calculate_area(shape):
    shape.area()
calculate_area(Rectangle())
calculate_area(Circle())
calculate_area(Triangle())