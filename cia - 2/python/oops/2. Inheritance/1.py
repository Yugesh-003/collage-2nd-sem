#single inheritance
# Base class: Academic
class Academic:
    def __init__(self):
        self.marks = 100

    def display_academic(self):
        print(f"Marks: {self.marks}")

# Derived class: StudentProfile
class StudentProfile(Academic):
    def __init__(self):
        self.name = "Yugesh"
        super().__init__()
    def display(self):
        print(f"Student Name: {self.name}")
         
# Creating an object of StudentProfile
student = StudentProfile()

student.display_academic()
student.display()