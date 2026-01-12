import math
#Create the Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return f"({self.x}, {self.y})"

#Create the Circle class that uses Point
class Circle:
    def __init__(self, center, radius):
        self.center = center    # Point object
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def display(self):
        return (
            f"Center: {self.center.display()}\n"
            f"Radius: {self.radius}\n"
            f"Area: {self.area():.2f}\n"
            f"Circumference: {self.circumference():.2f}"
        )
