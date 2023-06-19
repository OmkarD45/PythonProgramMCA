'''
Write python program to create superclass named “Shapes” has a method 
called “area()”. Subclasses of “Shapes” can be “Triangle”, “circle”, 
“Rectangle”, etc. Each subclass has its way of calculating area. Using 
Inheritance and Polymorphism means, the subclasses can use the “area()” 
method to find the area's formula for that shape
'''
import math

class Shapes:
    def area(self):
        pass

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Create instances of the subclasses
triangle = Triangle(4, 5)
circle = Circle(3)
rectangle = Rectangle(6, 7)

# Calculate and display the areas of different shapes
print("Area of the triangle:", triangle.area())
print("Area of the circle:", circle.area())
print("Area of the rectangle:", rectangle.area())
