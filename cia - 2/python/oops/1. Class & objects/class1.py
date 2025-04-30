# Class & Object: Student Class
class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

student1 = Student("Yugesh", 18, "242237")

student1.display()