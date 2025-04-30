class Cylinder:
    def __init__(self, radius, height):
        self.pi = 3.14  # Public variable
        self.radius = radius  # Public variable
        self.height = height  # Public variable

    def volume(self):
        return self.pi * self.radius * self.radius * self.height  # Using public variables

# Creating an object
cyl = Cylinder(5, 10)

# Accessing public variables
print("Pi value:", cyl.pi)
print("Radius:", cyl.radius)
print("Height:", cyl.height)

# Calculating volume
print("Volume of Cylinder:", cyl.volume())
