# ===========================================================================
# Title: inheritance_example.py
# Description: This script enables to review the basics of inheritance with 
#   class
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================


# -----------------------------Import of modules-----------------------------


# ---------------------------------Functions----------------------------------
class Device:
    def __init__(self,name, connected_by):
        self.name=name
        self.connected_by= connected_by
        self.connected = True #here all are connected no need to put as parameter
    
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})" 
        #"!r" -> put with '...'
        
    def disconnect(self):
        self.connected=False
        print("Disconnected")


class Printer(Device):
    def __init__(self,name,connected_by,capacity):
        super().__init__(name,connected_by) 
        #get the __init__ method of the parent class(Device)
        
        #Parameters we had only for children class(Printer)
        self.capacity=capacity
        self.remaining_pages = capacity
        
    def __str__(self):
        return f"{super().__str__()}({self.remaining_pages} pages remaining )"
    
    def print(self,pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages        
        

# ---------------------------------Main program-------------------------------

#Device class
#phone = Device("Printer","USB")
#print(phone) #Device 'Printer' (USB)
#phone.disconnect() #Disconnected

#Printer class
printer=Printer("Printer","USB", 500)
printer.print(20)
print(printer)

printer.disconnect() #Disconnected
# if the method is not found in the Printer class, it looks for in the parent class
# so they take by inheritance the disconnected methos from Device class
# First Printer class will be checked
# Second the Device class will be checked
# Then the object will be checked

printer.print(30) #Your printer is not connected!