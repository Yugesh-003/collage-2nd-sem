# Base class
class CsDept:
    def show_CsDept(self):
        print("Department of Computer Science")

# Derived class inheriting from A (Single Inheritance)
class Ds(CsDept):
    def show_Ds(self):
        print("Data Science and Analytics")

# Another derived class inheriting from A (Single Inheritance)
class Sss(CsDept):
    def show_Sss(self):
        print("Cyber Security")

# A class inheriting from both B and C (Multiple Inheritance)
class Winners(Ds,Sss):
    def show_winners(self):
        print("Winners of Ds and Sss")

# Object creation
obj = Winners()
obj.show_CsDept()  
obj.show_Ds()  
obj.show_Sss() 
obj.show_winners()  
