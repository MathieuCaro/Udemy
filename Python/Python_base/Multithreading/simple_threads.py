# ===========================================================================
# Title: simple_threads.py
# Description: This script enables to review the basics of threads
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================


# -----------------------------Import of modules-----------------------------
import time # library to mesure the time of execution of program or do pause
# in the program(here)
import threading #use threads here

# ---------------------------------Functions----------------------------------
"""There is here two functions who do the same thing or almost with the print"""
def process_one():
    i=0
    while i<3:
        print("ooooooo")
        time.sleep(0.1)
        i+=1
        
def process_two():
    i=0
    while i<3:
        print("xxxxxxx")
        time.sleep(0.1)
        i+=1
        
# ---------------------------------Main program-------------------------------
"""We create here two thread linnked to the both functions each one """
th1 = threading.Thread(target=process_one) #first thread declaration
th2 = threading.Thread(target=process_two) #second thread declaration

th1.start() #beginning of the first thread
th2.start() #beginning of the second thread

#In reality there is no order with thread it means that they both start and
# execute their function

th1.join()
th2.join()

#When they both finish(join), the program do the print
print("Fin du programme")