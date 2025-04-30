#to illustrate hierarchical concept student details as base class from student
# details, personal details to academic details area derived class 
#hierarchical inheritance
class Students:
    def __init__(self):
        self.name = "Yugesh"
        self.rno = 242237
        self.cls = "CS(DSA)"
        self.hobby = "Photography"
        self.mark = 100

class PersonalDetails(Students):
    def personal(self):
        print("Personal Details")
        print("Name : ",self.name)

class AcademicDetails(Students):
    def academic(self):
        print("Academics")
        
        print("Mark : ",self.mark)
        
obj = PersonalDetails()
obj2 = AcademicDetails()

obj.personal()
obj2.academic()