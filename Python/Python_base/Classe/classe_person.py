# ===========================================================================
# Title: classe_person.py
# Description: This script enables to review the basics og Class methods
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================


# -----------------------------Import of modules-----------------------------


# ---------------------------------Functions----------------------------------
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"This person is called {self.name} and is {self.age} years old "
    
    def __repr__(self):
        return f"<Person('{self.name}',{self.age})>"

# ---------------------------------Main program-------------------------------
person_1=Person("Bob",25)
print(person_1)