#Circle which take the given list as arguments
#Importing math module
import math

class Circle:
    # constructor
    def __init__(self, list):
        self.list = list
# Area of the circle
    def area(self):
        A = []
        for radius in self.list:
            area = math.pi * (radius ** 2)
            A.append(area)
        return A
# Circumference of the circle
    def circumference(self):
        circum = []
        for radius in self.list:
            circumference = 2 * math.pi * radius
            circum.append(circumference)
        return circum

# declaration of the given list
list = [10, 501, 22, 37, 100, 999, 87, 351]
# Creating Object for the class
circle = Circle(list)
A = circle.area()
circum = circle.circumference()
# Printing the Values
print("Area of the Circles:", A)
print("Circumferences of the circles:", circum)