class Shape:
    def __init__(self):
        self.__pi = 3.14  # Private variable

    def circle_area(self, radius):
        return self.__pi * radius * radius  # Using private variable

    def rectangle_area(self, length, breadth):
        return length * breadth

    def triangle_area(self, base, height):
        return 0.5 * base * height

# Creating an object
s = Shape()

# Accessing methods
print("Area of Circle (r=5):", s.circle_area(5))
print("Area of Rectangle (l=4, b=6):", s.rectangle_area(4, 6))
print("Area of Triangle (b=4, h=5):", s.triangle_area(4, 5))

# Trying to access private variable directly (will cause an error)
# print(s.__pi)  # Uncommenting this line will raise an AttributeError
