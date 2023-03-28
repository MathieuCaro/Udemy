# ===========================================================================
# Title: calculator.py
# Description: This program is a calculator
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
import tkinter.font as font
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
# ----------------------------------Constants---------------------------------
ORANGE = "#FF7900"
BLACK = "#000000"
WHITE = "#FFFFFF"
BLUE = "#0090FC"
# -----------------------------Global Variables--------------------------------
equation=""
# ---------------------------------Functions----------------------------------
def show(value):
    """This function enables to set the value of each button on screen"""
    global equation
    equation+=value #we add each button value to the string equation
    label_result.set(equation) 
    #for each additional button value it updates the value of the equation
    
def clear():
    """This function simply clear the equation after using the "C" button"""
    global equation
    equation=""
    label_result.set(equation)
    
def calculate():
    """This function calculate from the string "equation" """
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        #here eval enables from a string to transform into a calcul
        #in that way, eval send back the result of the operation
        except:
            result = "error"
            equation=""
        #in case the operation is not calculable, there is a error
        label_result.set(result)
    
def buttons_parameters(text_,width_,height_,foreground_color,backgroundcolor_,char,row_,column_):
    button=tk.Button(button_frame,fg=foreground_color,bg=backgroundcolor_,command=lambda: show(char),bd=1,pady=1,font=("arial",30,"bold"),height=height_,width=width_,text=text_)
    button.grid(row=row_,column=column_)


# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
root.title("Simple Calculator")
root.geometry("650x750+100+200") #Size of the window(570*600)
#initial point (100px from de left and 200 from the top)
root.resizable(False,False)
#The size of the window can't be modified(by x or y)(False)
root.configure(bg="white")
root.columnconfigure(0, weight=1)

#Result of the calculator
result_frame=ttk.Frame(root,padding=(20, 10, 20, 0))
result_frame.grid(row=0, column=0, sticky="EW")
#result_frame.configure(bg='blue')
result_frame.rowconfigure(0,minsize=200)
#label_result = ttk.Label(result_frame,textvariable=equation).grid(row=0,column=0,sticky="EW")
label_result = tk.StringVar()
label=ttk.Label(result_frame,textvariable=label_result,anchor="e")
label.config(font=("Segoe UI",70))
label.grid(row=0,column=0,sticky="EW")


separator = ttk.Separator(root,orient="horizontal")
separator.grid(column=0, row=1, sticky='ew', padx=10)



button_frame=ttk.Frame(root,padding=(20,10))
button_frame.grid(row=1,column=0,sticky="EW")
#button_frame.configure(background="black")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

#First line of digits
button_C = tk.Button(button_frame, text="C",width=4,height=2,font=("arial",30,"bold"),bd=1,fg=WHITE,bg=BLUE,pady=1,command=lambda: clear())
button_C.grid(row=1,column=0)

button_div = buttons_parameters("/", 4, 2, WHITE, BLACK, "/", 1, 1)
button_percent=buttons_parameters("%", 4, 2, WHITE,BLACK, "%", 1, 2)
button_X = buttons_parameters("x", 4, 2, WHITE, BLACK, "x", 1, 3)

#Second line of digits
button_7 = buttons_parameters("7", 4, 2, WHITE, BLACK, "7", 2, 0)
button_8 = buttons_parameters("8", 4, 2, WHITE, BLACK, "8", 2, 1)
button_9 = buttons_parameters("9", 4, 2, WHITE, BLACK, "9", 2, 2)
button_min = buttons_parameters("-", 4, 2, WHITE, BLACK, "-", 2, 3)

#Third line of digits
button_4 = buttons_parameters("4", 4, 2, WHITE, BLACK, "4", 3, 0)
button_5 = buttons_parameters("5", 4, 2, WHITE, BLACK, "5", 3, 1)
button_6 = buttons_parameters("6", 4, 2, WHITE, BLACK, "6", 3, 2)
button_plus = buttons_parameters("+", 4, 2, WHITE, BLACK, "+", 3, 3)

#Forth line of digits
button_1 = buttons_parameters("1", 4, 2, WHITE, BLACK, "1", 4, 0)
button_2 = buttons_parameters("2", 4, 2, WHITE, BLACK, "2", 4, 1)
button_3 = buttons_parameters("3", 4, 2, WHITE, BLACK, "3", 4, 2)
button_equal = tk.Button(button_frame, text="=",width=4,height=4,font=("arial",30,"bold"),bd=1,fg=WHITE,bg=ORANGE,pady=1,command=lambda: calculate())
button_equal.grid(row=4,column=3,rowspan=2)

#Fifth line of digits
button_0 = tk.Button(button_frame, text="0",width=10,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",command=lambda: show("0"))
button_0.grid(row=5,column=0,columnspan=2)
button_pt = buttons_parameters(".", 4, 2, WHITE, BLACK, ".", 5, 2)



root.mainloop()