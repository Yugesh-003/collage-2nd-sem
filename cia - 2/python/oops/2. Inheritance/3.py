#multi level inherentance
class I_Ds:
    def __init__(self):
        self.sem1Mark = 90
    def firstSemMark(self):
        print("1st semester mark :",self.sem1Mark)

class II_Ds(I_Ds):
    def __init__(self):
        super().__init__()
        self.sem2Mark = 80
    def secondSemMark(self):
        print("2nd semester mark :",self.sem2Mark)

class III_Ds(II_Ds):
    def __init__(self):
        super().__init__()
        self.sem3Mark = 99
    def thirdSemMark(self):
        print("3rd semester mark :",self.sem3Mark)

obj = III_Ds()

obj.firstSemMark()
obj.secondSemMark()
obj.thirdSemMark()