# ===========================================================================
# Title: classe_method_example.py
# Description: This script enables to review the differents types of class
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------General comments-----------------------------
"""
Instance methods are used for most things,when you want :
-produce action that use the data inside the object
-modify data inside self or the object
Class methods are used for:
- create mathode for the class and not for an instance or object
- link a method directly to the class 
Static methods are used :
- to place a method inside a class

"""
# -----------------------------Import of modules-----------------------------


# ---------------------------------Functions----------------------------------
class ClassTest:
    def instance_method(self): #definition of the method
    # an instance method has always self(object) as first parameter    
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
    #with a @classmethod cls represent the ClassTest itself
    #cls = ClassTest
        print(f"Called class_method of {cls}")
        
    @staticmethod
    def static_method():
        print("Called static_method.")
# ---------------------------------Main program-------------------------------

#instance method 

#test = ClassTest() #creating an object of ClassTest or instance 
#test.instance_method()  #Called instance_method of <__main__.ClassTest object at 0x7fd2725f31f0>

#class method

#ClassTest.class_method() #Called class_method of <class '__main__.ClassTest'>

#static method

ClassTest.static_method()