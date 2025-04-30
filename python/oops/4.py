class University:
    def __init__(self, uniName):
        self.uniName = uniName

    def display_university(self):
        print(f"University: {self.uniName}")

class College(University):
    def __init__(self, uniName, clgName, dept):
        super().__init__(uniName)
        self.clgName = clgName
        self.dept = dept

    def display_college(self):
        print(f"College: {self.clgName}, dept: {self.dept}")

class Class(College):
    def __init__(self, uniName, clgName, dept, className, students_count):
        super().__init__(uniName, clgName, dept)
        self.className = className
        self.students_count = students_count

    def display_class(self):
        print(f"Class: {self.className}, Students Count: {self.students_count}")

# Creating an object of Class
obj = Class("Kamarajar ", "SLCS College", "Computer Science", "CS101", 39)

# Displaying details
obj.display_university()
obj.display_college()
obj.display_class()
