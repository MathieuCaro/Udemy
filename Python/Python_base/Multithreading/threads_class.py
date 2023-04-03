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

my_lock = threading.RLock() #creation of the lock
class My_process(threading.Thread): #here threading.Thread is the parent class
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        i=0
        while i<3:
            with my_lock:
            #The lock here enables to wait that the first thread(1 or 2) finish until the end
            #Then the second one (1 or 2)do the same until i=2    
                letters = "ABC"
                for letter in letters:
                    print(letter)
                    time.sleep(0.3)
            i+=1
        
# ---------------------------------Main program-------------------------------
"""We create here two thread linnked to the both functions each one """
th1 = My_process() #first thread declaration
th2 = My_process() #second thread declaration

th1.start() #beginning of the first thread
th2.start() #beginning of the second thread

th1.join()
th2.join()

#When they both finish(join), the program do the print

print("Fin du programme")

#Each time we execute the program there is a different order of the threads

# Result : ABCABCABCABCABCABC
