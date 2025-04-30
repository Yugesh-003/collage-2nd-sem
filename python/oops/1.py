class Students:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

name, age = "Yugesh", 18

obj = Students(name, age)

obj.display()