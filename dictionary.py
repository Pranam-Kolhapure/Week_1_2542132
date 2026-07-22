class Student:
    college_name='abc college'

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print(self.marks,"welcome student",self.name)

    def get_marks(self):
        return self.marks


s1=Student("Pranam",98)
s1.welcome()
print(s1.get_marks())
        













