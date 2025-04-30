class Shape:
    def area(self, *args):
        if len(args) == 1:  # Circle (radius)
            r = args[0]
            return 3.14 * r * r
        elif len(args) == 2:  # Rectangle (length, breadth)
            l, b = args
            return l * b
        else:
            return "Invalid number of arguments"

# Create an object
s = Shape()

# Calling area method with different arguments
print("Area of Circle (r=5):", s.area(5))
print("Area of Rectangle (l= 4, b=6):", s.area(4, 6))
