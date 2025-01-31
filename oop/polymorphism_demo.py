import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example usage
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is {shape.area()}")
