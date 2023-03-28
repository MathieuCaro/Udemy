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
# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------
def digit_button_init(value):
    pass
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
label_result = tk.Label(result_frame,text="").grid(row=0,column=0,sticky="EW")

separator = ttk.Separator(root,orient="horizontal")
separator.grid(column=0, row=1, sticky='ew', padx=10)
#First line of digit
#Button_C
button_frame=ttk.Frame(root,padding=(20,10))
button_frame.grid(row=1,column=0,sticky="EW")
#button_frame.configure(background="black")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

button_C = tk.Button(button_frame, text="C",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#0090FC",pady=1)
button_C.grid(row=1,column=0)
button_div = tk.Button(button_frame, text="/",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_div.grid(row=1,column=1)
button_percent = tk.Button(button_frame, text="%",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_percent.grid(row=1,column=2)
button_multi = tk.Button(button_frame, text="x",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_multi.grid(row=1,column=3)

button_7 = tk.Button(button_frame, text="7",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_7.grid(row=2,column=0)
button_8 = tk.Button(button_frame, text="8",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_8.grid(row=2,column=1)
button_9 = tk.Button(button_frame, text="9",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_9.grid(row=2,column=2)
button_min = tk.Button(button_frame, text="-",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_min.grid(row=2,column=3)

button_4 = tk.Button(button_frame, text="4",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_4.grid(row=3,column=0)
button_5 = tk.Button(button_frame, text="5",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_5.grid(row=3,column=1)
button_6 = tk.Button(button_frame, text="6",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_6.grid(row=3,column=2)
button_plus = tk.Button(button_frame, text="+",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_plus.grid(row=3,column=3)

button_1 = tk.Button(button_frame, text="1",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_1.grid(row=4,column=0)
button_2 = tk.Button(button_frame, text="2",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_2.grid(row=4,column=1)
button_3 = tk.Button(button_frame, text="3",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_3.grid(row=4,column=2)
button_equal = tk.Button(button_frame, text="=",width=4,height=4,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#FF7900",pady=1)
button_equal.grid(row=4,column=3,rowspan=2)

button_0 = tk.Button(button_frame, text="0",width=10,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_0.grid(row=5,column=0,columnspan=2)
button_pt = tk.Button(button_frame, text=".",width=4,height=2,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000",pady=1)
button_pt.grid(row=5,column=2)





root.mainloop()