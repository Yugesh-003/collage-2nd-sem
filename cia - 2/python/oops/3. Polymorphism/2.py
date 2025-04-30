class Student:
    def calculate_marks(self, marks):
        return sum(marks)  # Default total marks calculation

class EngineeringStudent(Student):
    def calculate_marks(self, marks):
        return sum(marks) / len(marks)  # Average marks for an engineering student

class MedicalStudent(Student):
    def calculate_marks(self, marks):
        return max(marks)  # Highest mark for a medical student

# Creating objects
engStd = EngineeringStudent()
medStd = MedicalStudent()
genStd = Student()

marks = [80, 90, 85, 70, 95]

# Calling overridden methods
print("Total Marks (General Student):", genStd.calculate_marks(marks))
print("Average Marks (Engineering Student):", engStd.calculate_marks(marks))
print("Highest Marks (Medical Student):", medStd.calculate_marks(marks))
