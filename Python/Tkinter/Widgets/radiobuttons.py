# ===========================================================================
# Title: radiobuttons.py
# Description: This program allows you to discover a non-exhaustive list 
#   of radiobuttons
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------

def print_current_option():
    print(f"The best language to use Tkinter is {storage_variable.get()}")

# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
root.geometry("600x400")
root.resizable(False,False)
root.title("RadioButton Widget example")

storage_variable = tk.StringVar() 
#create a string variable

Text_label=ttk.Label(root,text="What is the language to use for Tkinter ?")
Text_label.pack()
option_1 = ttk.Radiobutton(
    root,
    text="C",
    variable=storage_variable,
    value="C",
    padding=(200,0,0,0),
    command=print_current_option
    ).pack(anchor=tk.W)

option_2 = ttk.Radiobutton(
    root,
    text="C++",
    variable=storage_variable,
    value="C++",
    padding=(200,0,0,0),
    command=print_current_option
    ).pack(anchor=tk.W)

option_3 = ttk.Radiobutton(
    root,
    text="Python",
    variable=storage_variable,
    value="Python",
    padding=(200,0,0,0),
    command=print_current_option
    ).pack(anchor=tk.W)

#variable: correspond to the string variable(selected_option)
#command : function run when the button is checked or unchecked
#onvalue/offvalue : determined what value the variable take



root.mainloop() 