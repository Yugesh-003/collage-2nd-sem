class Shapes:
    def __init__(self,radius, side, length, breath):
        self.r = radius
        self.s = side
        self.l = length
        self.b = breath

class Areas(Shapes):
    def circle(self):
        print("Area of the Circle is ", 3.14 * self.r * self.r)
    def rectangle(self):
        print("Area of Rectangle is ", self.l * self.b)
    def square(self):
        print("Area of Square is ", self.s * self.s)


radius, side, length, breath = 5, 2, 4, 6

obj = Areas(radius, side, length, breath)

obj.circle()
obj.square()
obj.rectangle()