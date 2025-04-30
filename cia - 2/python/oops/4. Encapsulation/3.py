class Cone:
    def __init__(self, radius, height):
        self._pi = 3.14  # Protected variable
        self._radius = radius  # Protected variable
        self._height = height  # Protected variable

    def volume(self):
        return (1/3) * self._pi * self._radius * self._radius * self._height  # Using protected variables

# Creating an object
cone = Cone(5, 10)

# Accessing protected variables (allowed but not recommended)
print("Pi value:", cone._pi)
print("Radius:", cone._radius)
print("Height:", cone._height)

# Calculating volume
print("Volume of Cone:", cone.volume())
