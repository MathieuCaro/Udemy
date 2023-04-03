# ===========================================================================
# Title: classe_intro.py
# Description: This script enables to review the basics og Class methods
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================


# -----------------------------Import of modules-----------------------------


# ---------------------------------Functions----------------------------------
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
        
    def average_grade(self):
        return sum(self.grades)/len(self.grades)

# ---------------------------------Main program-------------------------------
student_1 = Student("Mathieu",(12,20,15,17,13)) #creation de l'instance
student_2 = Student("Guillaume",(13,19,8,12,17)) #creation de l'instance

print(student_1.name)
print(student_1.average_grade())

print(student_2.name)
print(student_2.average_grade())


    