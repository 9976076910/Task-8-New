# 2) Private Member Variable with pi
class Circle:
    #Constructor
    def __init__(self, r):
        self.pi = 3.141  # private member variable
        self.r = r

   # Area of the Circle
    def area1(self):
        return self.pi * (self.r ** 2)
   # Circumference of the circle
    def circumference1(self):
        return 2 * self.pi * self.r

# Creating object for the class Circle
circle = Circle(5)
print("Area of the circle:", circle.area1())
# Printing the Area and Circumference
print("Circumference of the circle:", circle.circumference1())