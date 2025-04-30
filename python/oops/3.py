class Extras:
    def __init__(self):
        self.freeTimeDoings = "Sleeping"
        self.hobby = "Photography"

class Curricular:
    def __init__(self):
        self.level = "College"
        self.major = "CS"
        
class StudentProfile(Extras, Curricular):
    def __init__(self):
        Extras.__init__(self)
        Curricular.__init__(self)
        self.name = "Yugesh"
        self.age = 18
    
    def profile(self):
        print(f'''
Name = {self.name}
Age = {self.age}
Studying = {self.level}
Major = {self.major}
Hobby = {self.hobby}              
            ''')
    
obj = StudentProfile()
obj.profile()
