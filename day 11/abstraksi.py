from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Membuat objek dari kelas Rectangle dan Circle
rectangle1 = Rectangle(4, 5)
circle1 = Circle(3)
print(rectangle1.area())  # Output: 20
print(circle1.area())  # Output: 28.26
