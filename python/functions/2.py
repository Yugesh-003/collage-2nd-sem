import math

def calculate_area(radius):
    area = math.pi * radius * radius
    print(f"Area of the circle: {area:.2f}")

# Example usage
r = float(input("Enter the radius of the circle: "))
calculate_area(r)
