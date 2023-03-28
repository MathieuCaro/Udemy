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
root.geometry("570x600+100+200") #Size of the window(570*600)
#initial point (100px from de left and 200 from the top)
root.resizable(False,False)
#The size of the window can't be modified(by x or y)(False)
root.configure(bg="white")
root.columnconfigure(0, weight=1)

#Result of the calculator
result_frame=ttk.Frame(root,padding=(20, 10, 20, 0))
result_frame.grid(row=0, column=0, sticky="EW")
#result_frame.configure(bg='blue')
result_frame.rowconfigure(0,minsize=100)
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

button_C = tk.Button(button_frame, text="C",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#0090FC")
button_C.grid(row=1,column=0)
button_div = tk.Button(button_frame, text="/",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_div.grid(row=1,column=1)
button_percent = tk.Button(button_frame, text="%",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_percent.grid(row=1,column=2)
button_multi = tk.Button(button_frame, text="x",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_multi.grid(row=1,column=3)

button_C = tk.Button(button_frame, text="C",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#0090FC")
button_C.grid(row=2,column=0)
button_div = tk.Button(button_frame, text="/",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_div.grid(row=2,column=1)
button_percent = tk.Button(button_frame, text="%",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_percent.grid(row=2,column=2)
button_multi = tk.Button(button_frame, text="x",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_multi.grid(row=2,column=3)

button_C = tk.Button(button_frame, text="C",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#0090FC")
button_C.grid(row=3,column=0)
button_div = tk.Button(button_frame, text="/",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_div.grid(row=3,column=1)
button_percent = tk.Button(button_frame, text="%",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_percent.grid(row=3,column=2)
button_multi = tk.Button(button_frame, text="x",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_multi.grid(row=3,column=3)

button_C = tk.Button(button_frame, text="C",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#0090FC")
button_C.grid(row=3,column=0)
button_div = tk.Button(button_frame, text="/",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_div.grid(row=3,column=1)
button_percent = tk.Button(button_frame, text="%",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_percent.grid(row=3,column=2)
button_multi = tk.Button(button_frame, text="x",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_multi.grid(row=3,column=3)

button_C = tk.Button(button_frame, text="C",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#0090FC")
button_C.grid(row=4,column=0)
button_div = tk.Button(button_frame, text="/",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_div.grid(row=4,column=1)
button_percent = tk.Button(button_frame, text="%",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_percent.grid(row=4,column=2)
button_multi = tk.Button(button_frame, text="x",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_multi.grid(row=4,column=3,rowspan=2)

button_C = tk.Button(button_frame, text="C",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#0090FC")
button_C.grid(row=5,column=0,columnspan=2)
button_div = tk.Button(button_frame, text="/",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#FFFFFF",bg="#000000")
button_div.grid(row=5,column=2)





root.mainloop()