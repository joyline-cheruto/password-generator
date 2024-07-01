class Student:
    def __init__(self, name, gpa, graduated):
        self.name = name
        self.gpa = gpa
        self.graduated = graduated

from Test import Student
student1 = Student ("Kim","3.5","True")
student2 = Student ("Chech","3.9","False")
print(student2.gpa)
