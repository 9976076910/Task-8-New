#Area and Perimeter

class Rectangle:
    #Constructor
    def __init__(self, *sides):
        self.sides = sides

    @classmethod
    def calculate_area(cls, *sides):
        if len(sides) != 2:
            raise ValueError("Cannot be calculated")
        return sides[0] * sides[1]

    @classmethod
    def calculate_perimeter(cls, *sides):
        return sum(sides)

# given list:
list = [10, 50, 22, 37, 100, 999, 87, 351]
#rec = rectangle
rec = [(list[i], list[i+1]) for i in range(0, len(list), 2)]

for rec in rec:
    area = Rectangle.calculate_area(*rec)
    perimeter = Rectangle.calculate_perimeter(*rec)
    print("sides of the rectangle", rec, "area of the rectangle:", area, "perimeter of the rectangle:", perimeter)