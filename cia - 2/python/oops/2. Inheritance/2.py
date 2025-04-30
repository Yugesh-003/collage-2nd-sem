#Multiple inheritance
class Acedamic:
    def __init__(self):
        self.subMarks = 80
    def mark(self):
        print("Mark :" ,self.subMarks)

class Extras:
    def __init__(self):
        self.hobby = "Photography"
    def hobbies(self):
        print("Hobby :",self.hobby)
        
class Student(Acedamic, Extras):
    def __init__(self):
        Acedamic.__init__(self)
        Extras.__init__(self)
        self.name = "Yugesh"
    def names(self):
        print("Name : ",self.name)
        
obj = Student()

obj.names()
obj.mark()
obj.hobbies()
    
    