'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f"{self.length} X {self.width} rectangle with area of {self.area()} and perimeter of {self.perimeter()}"

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"{self.radius*2} diameter circle with area of {round(self.area(), 2)} \
        and circumference of {round(self.circumference(), 2)}"

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return math.pi * 2*self.radius

rect = Rectangle(4, 8)
circle = Circle(2)
print(rect)
print(circle)