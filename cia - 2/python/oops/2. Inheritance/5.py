# Base class
class A:
    def show_A(self):
        print("Class A")

# Derived class inheriting from A (Single Inheritance)
class B(A):
    def show_B(self):
        print("Class B")

# Another derived class inheriting from A (Single Inheritance)
class C(A):
    def show_C(self):
        print("Class C")

# A class inheriting from both B and C (Multiple Inheritance)
class D(B, C):
    def show_D(self):
        print("Class D")

# Object creation
obj = D()
obj.show_A()  # Inherited from A
obj.show_B()  # Inherited from B
obj.show_C()  # Inherited from C
obj.show_D()  # Defined in D
